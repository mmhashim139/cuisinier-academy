from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.contrib import messages
from workshops.models import Workshop
from .forms import OrderForm
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from .models import Order, OrderLineItem
from django.conf import settings
from .webhook_handler import StripeWH_Handler
from django.core.mail import send_mail
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'order': json.dumps(request.session.get('order', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def reservation(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.phone_number,
                'country': profile.country,
                'postcode': profile.postcode,
                'town_or_city': profile.town_or_city,
                'street_address1': profile.street_address1,
                'street_address2': profile.street_address2,
                'county': profile.county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_total = round(workshop.price * 100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    context = {
        'workshop': workshop,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'reservations/reservations.html', context)


def create_reservation(request, workshop_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        workshop = get_object_or_404(Workshop, pk=workshop_id)
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            workshop = Workshop.objects.get(id=workshop_id)
            order.order_total = workshop.price
            order.workshop = workshop
            order.save()
            order_line_item = OrderLineItem(
                order=order,
                workshop=workshop,
                lineitem_total=workshop.price,
                )
            order_line_item.save()
            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')


    template = 'reservations/reservations.html'
    price = workshop.price
    stripe_total = round(price * 100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    context = {
        'workshop': workshop,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'full_name': order.full_name,
                'phone_number': order.phone_number,
                'country': order.country,
                'postcode': order.postcode,
                'town_or_city': order.town_or_city,
                'street_address1': order.street_address1,
                'street_address2': order.street_address2,
                'county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Send the user a confirmation email
    cust_email = order.email
    subject = render_to_string(
        'reservations/confirmation_emails/confirmation_email_subject.txt',
        {'order': order})
    body = render_to_string(
        'reservations/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    if 'oreder' in request.session:
        del request.session['order']

    template = 'reservations/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

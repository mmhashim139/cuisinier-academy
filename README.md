![device viewings](documentation/readmeheader.png)
# [Cuisinier-Academy](https://cuisinier-academy.herokuapp.com/)
## Table of Contents
1. [Overview](#overview)
2. [UX/UI](#ux)
    - [Project Goals](#project-goals)
    - [User stories](#user-stories)
    - [Design choices](#design-choices)
    - [Wirframe](#wirframe)
3. [Information Architecture](#information-architecture)
    - [Database](#database)
    - [Applications](#applications)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
    - [User Story Testing](#user-story-testing)
    - [Manual Testing](#manual-testing)
    - [Code Validation](#code-validation)
7. [Deployment](#deployment)

8. [Credits](#credit)


## Overview
Cuisinier Academy Is a Training Provider specialize in Food Making hands-on workshops.

With the top experts in the food Industry , Cuisinier Academy provide 3 days workshops thats take the skills level of participants from beginner to experts .
Either a Foodi , or an entrepreneur or trying to discover the depth of Food making Cuisinier Academy is the place to go .

Cuisinier Academy Website show the available workshops & Experts details ,
By visiting the workshop page you will learn about the workshop details like agenda , location & price
and you will be able to register in the class and make the payment.

Feel Free to visit 
[Cuisinier-Academy](https://cuisinier-academy.herokuapp.com/) Live Website 

## UX

### Project Goals
- Development Goals:

Cuisinier Academy Is a Demo website built as a milestone 4 project for Coding Institute to demonstrate my coding knowledge as a Full stack web developer.
The goal of the website is to solve a Business need for the client help them sell and collect payment from the website along with other goals.

- Business Goals

The Cuisinier Academy managers require a website with nice user experience thats represent the company brand , help the users to learn about the workshops details and who is our experts and what is the available workshops with more details of each workshop.
Also , the ability of the users to register for the workshop and make the payment .
For the website admin , They need the ability to track registration and add or remove workshops. 

- visitors goals


For website users , They know about the company & the available workshops
They need easy navigation through the website and be able to make secure payment with their profile details


### User stories

- Users


| Status | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
|&checkmark;| user | I would like to Have a nice user experience , responsive ,rich media , simple navbar | for better UX/UI  |
|&checkmark;| user | I would like to Have Easy navigate through website | So i can understand what this website provide |
|&checkmark;| user | I would like to view a list of available workshops | So i can find workshops best for me |
|&checkmark;| user | I would like to View the trainers and their details | So i can have confedance of the training |
|&checkmark;| user | I would like Learn about the company | So i can make sure of the quality of the products |
|&checkmark;| user | I would like view workshop details , agenda , trainer, date , location , price| So i can make dicide ifi will book|
|&checkmark;| user | I would like to register for an account using my email| to keep my orders history |
|&checkmark;| user | I would like to register for an account using my google account| for easy access |
|&checkmark;| user | I would like to login or logout easy| for easy access |
|&checkmark;| user | I would like to reset my password | for security reasons |
|&checkmark;| user | I would like to rcieve eamils to confirm my actions in my account | for security reasons |
|&checkmark;| user | I would like to have a user profile, with my orders history | to track my regestrations and payments |
|&checkmark;| user | I would like to Easy book my seat with my account info | save time of filling the form |
|&checkmark;| user | I would like to view my order details / cost  before buy| make sure of the details |
|&checkmark;| user | I would like to order in Secure, easy to fill form | easy booking |
|&checkmark;| user | I would like to view an order confirmation  , Thanks page after checkout | booking confirmation |
|&checkmark;| user | I would like to receive an email confirmation after checking out | booking confirmation  |

- Admin

| Status | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
|&checkmark;| Admin | I would like to Have a super user account | To access dashboard and manage the site  |
|&checkmark;| Admin | I would like to be able to add workshop and workshop details | To achive the website goal of selling workshops seats |
|&checkmark;| Admin | I would like to be able to edit workshop details | To change and update workshop details |
|&checkmark;| Admin | I would like to be able to delete workshops or make it un published | To manage our schedule and prevent booking outdated workshops |
|&checkmark;| Admin | I would like to be able to add trainers and create trainers profile with their info | To provide more details on our workshops trainer |
|&checkmark;| Admin | I would like to be able to edit trainer details | To manage any changes in trainers info |
|&checkmark;| Admin | I would like to be able to delete trainer profiles | To manage any changes in our trainers and workshops schedule |
|&checkmark;| Admin | I would like to be able to View workshops registration | To manage workshops regestration & sales |
|&checkmark;| Admin | I would like verification emails for new account to be sent | To prevent bots and fake account |
|&checkmark;| Admin | I would like confirmation emails for new orders to be sent | To give our customers record of regestration |


### Design choices

The main theme of the design is to be Dark & Clean with rich media views
The website will provide the same user experiance in diffrent screem sizes
##### Color Scheme
![device viewings](documentation/colors.png)

##### Typography

From Google fonts I picked the following fonts:

- Flamenco
- Lato

### wirframe
In the beginig of the project the wireframes were created using [Balsamiq](https://balsamiq.com/)
here are the links :

- [Home Desktop](https://i.ibb.co/R3sZb4x/home-desktop.png)
- [Home Tablet](https://i.ibb.co/r0fjVgf/home-tablet.png)
- [Home Mobile](https://i.ibb.co/3zC1KNK/home-mobile.png)


- [Workshops Desktop](https://i.ibb.co/4fJs163/workshop-desktop.png)
- [Workshops Tablet](https://i.ibb.co/s624F6R/workshop-mobile.png)
- [Workshops Mobile](https://i.ibb.co/5T5VMgJ/workshop-tablet.png)



## Information Architecture

### Database
![device viewings](documentation/database_diagram/db.png)
### Main Applications
- Experts
- home
- reservations
- profiles
- workshops



## Features
#### Existing Features

- Home page hero 

larg hero with background image that have dark gradiant lines & Text  header
with diffrent styles for some text and call to action .
The header will tak all the screen and navbar icon at the top left to let the focus
only in the hero section texts.

- Navbar 

for the navbar , the design is not to add top links in the page only the navbar icon
once the user click in the icon the top links menue will show in full screen with black background
and centered menue lists .
by hovering on the link the color will change from the white to red .


- Workshop Section

The workshop section seperated to two coloms in big screens .
one with about workshops section and the other with workshop cards


- Workshops Cards

workshop cards with background image from the workshop main image and dark gradiant.
by hovering the workshop card, the size of the cards will reduced and croser pointer will show.

- Home page buttons 

buttons with red border backgrounds , by hovering the button will changed to yellow.

- Experts cards

each expert have an image and name card , with slightly dark opacity .
if user hover on the card the croser become pointer and opacity reduced to create visual interaction.

- Footer
With black background and white color 
the footer contain the name of the website and social media icons


####  Features for Future



## Technologies Used

* HTML5

* CSS3

* JavaScript

* [Bootstrap](https://www.bootstrapcdn.com/)

* [Google fonts](https://fonts.google.com/)

* [Font Awesome](https://fontawesome.com/)

* [Python](https://www.python.org/)

* [Django](https://www.djangoproject.com/) 

* [AWS S3](https://aws.amazon.com/)

* [Stripe](https://stripe.com/gb)

* [GitHub](https://github.com/)

* [Gitpod](https://www.gitpod.io/) As an IDE

* [Balsamiq](https://balsamiq.cloud/) To create wireframes

* [PostgreSQL](https://www.postgresql.org/) 

* [IMGBB ](https://imgbb.com/) 




## Testing

### User Story Testing

| User Story | Status|
| ----------------------------- | --------------- |
| user can Have a nice user experience , responsive ,rich media , simple navbar | pass |
| user can Have Easy navigate through website | pass |
| user can view a list of available workshops | pass |
| user can View the trainers and their details | pass |
| user can larn about the company | pass |
| user can view new workshop details , agenda , trainer, date , location , price| pass |
| user can register for an account using email| pass |
| user can register for an account using google account | pass |
| user can login or logout | pass |
| user can reset the password if forget| pass |
| user can rceive eamils to confirm actions in user account | pass |
| user can have a user profile, with orders history | pass |
| user can Easy book workshop seat with the account info | pass |
| user can view order details, cost before buy | pass |
| user can order in Secure, easy to fill form | pass |
| user can view an order confirmation  , Thanks page after checkout | pass |
| user can receive an email confirmation after checking out | pass |
| Admin Have a super user account | pass |
| Admin be able to add workshop and workshop details | pass |
| Admin be able to edit workshop details | pass |
| Admin be able to delete workshops or make it un published | pass |
| Admin be able to add trainers and create trainers profile with their info | pass |
| Admin be able to edit trainer details | pass |
| Admin be able to delete trainer profiles | pass |
| Admin be able to View workshops registration | pass |
| Admin can receive verification emails for new account to be sent | pass |
| Admin can receive confirmation emails for new orders to be sent | pass |

### Manual Testing

- Home page

Home page layout responsive as the required layout

- Navbar

Navabr icon and links worked .
user can see links to login
If user logedin will see link to his account and log out link
If user is Admin will see link to the dashboard.

- Workshop cards

background image and resized by if hovered ,
links for each workshop working .

- Expert Cards

Expert card images showed , links for expert profile is working.
in all expert page , each expert have links to related workshops.


- Workshop page 

links working correctly , details of each workshop showes ,
reservation button both in the top and button of the page are working.


- Order Details.

reservation links renders workshop details above the info form correctly

- Reservation form 

the form easy to filled , if user registered profile data will be renderd.
and validation message will show for any error

- Thanks page 

with order details  rendered correcctly for each workshop and link to other workshops.
email confirmation sent once the order filled.

- My account

Order history and profile information are rendered correctly .

### Code Validation
For HTML & CSS Testing I used 

* [W3C Mark-up Validation Service](https://validator.w3.org/) HTML Validator
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) CSS Validator


## Deployment
#### Heroku 

The Deployment through Heroku was through the following steps
- Create an app in Herouku
- after push the code to github 
- in deploy section
- link Heroku with github account
- choose the project repo. 
- in Manual deploy 
- Choose a master branch to deploy
- click to deploy

#### AWS - S3
for media and static files storage i created S3 bucket 
- following the step in [Create an S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)

## Credit
- The main model and functions in this project inspired and customized from Code Institute Boutique Ado project .

#### Media 
The images used in this website are :
- Photo by [Phil Hearing](https://unsplash.com/@philhearing?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Photo by [Tamara Gak](https://unsplash.com/@tamara_photography?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Photo by [Nicholas Barbaros](https://unsplash.com/@nicubarbaros?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Photo by [Bermix Studio](https://unsplash.com/@bermixstudio?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)


- Photo by [Sole D'Alessandro G.](https://unsplash.com/@s___d___g?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Photo by [Alex Hu](https://unsplash.com/@alexandwich?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Photo by [Pigi Mazzoli](https://unsplash.com/@pigibear?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Photo by [Gabriella Clare Marino](https://unsplash.com/@gabiontheroad?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

- Photo by [Monika Grabkowska](https://unsplash.com/@moniqa?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Photo by [Erik Odiin](https://unsplash.com/@odiin?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Photo by [Augustine Fou on](https://unsplash.com/@augustinefou?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) [Unsplash](https://unsplash.com/s/photos/bread-making?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

#### Acknowledgements
Special thanks to Code Institute community & mentors , My colleagues in #slack & People in stack-overflow community where I found many of my questions answered there.
#### Disclaimer

**The content of this website is for educational purposes only.**



Test allauth -


login with email  :
                    Done , received email confirmation in the template
login with Google :


                    error : Authorization Error , Error 400: redirect_uri_mismatch
                    The redirect URI in the request, http://localhost:8000/accounts/google/login/callback/, 
                    does not match the ones authorized for the OAuth client. To update the authorized redirect URIs,
                    visit: https://console.developers.google.com/apis/credentials/oauthclient/${your_client_id}?project=${your_project_number}


                    SOLVED :
                     chane the callback in Authorized redirect URIs 
                     from:
                     http://127.0.0.1:8000/accounts/google/login/callback/ as mention in the document 
                     To
                     http://localhost:8000/accounts/google/login/callback/


                     error:
                     after login with google redirect to success page not working "localhost refused to connect."

                     http://localhost:8000/accounts/google/login/callback/?state=vU4o1kjqcJ0o&code=4%2F0AY0e-g7oX8qHqthlTIj1eZH0AsmtL6fmhA2Q2yCPcJj83f_-OwbGVz4VS6xHxQuqu41Gmw&scope=email+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+openid&authuser=0&prompt=consent#

- --------------------------- 
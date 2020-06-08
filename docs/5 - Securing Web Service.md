# Securing a RESTful web service

Currently, the service is open to anybody, and that is a bad thing.

We havea complete web service that can manage our todo list, but the service in its current state is open to any client. If a strange figures out how our API works he or she can write a new client that can access our service and mess with our data.

Security is a serious problem that should always be addressed.

The easiest way to secure our web service is to require clients to provide a username and a password. In a regular web application you would have a logic form that posts the credentials, and at that point the server would create a session for the logged in user to continue working, with the session id stored in a cookie in the client browser. Unfortunately, doing that here would violate the stateless requirement of REST, so instead we have toask clients to send their authentication information with every request they send to us.

With REST we always try to adhere to the HTTP protocol as much as we can. Now that we need to implement authentication we should do so in the context of HTTP, which provides two forms of authentication called Basic and Digest.

To ensure the login information is secure the web service should be exposed in a HTTP Secure server (i.e. https://...) as this encrypts all the communications between client and server and prevents a third party from seeing the authentication credentials in transit.

Unfortunately, web browsers have the nasty habit of showing an ugly login dialog box when a request comes back with a 401 error code. This happens even for background requests, so if we were to implement a web browser client with our current web server we would need to jump through hoops to prevent users from showing their authentication dialogs and let our client application handle the login.

A simple trick to distract web browsers is to return an erorr code other than 401. An alternative error code favored by many is 403, which is the "Forbidden" error. While this is a close enough error, it sort of violates the HTTP standard, so it is not the proper thing ti do if full compliance is necessary. In particular, this would be a bad idea if the client application is not a web browser. But for cases where server and client are developed together it saves a lot of trouble. The simple change that we can make to implement this trick is to replace the 401 with a 403.
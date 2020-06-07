# Background (REST)

In recent years, REST (REpresentational State Transfer) has emerged as the standard architectural design for web services and APIs. This project aims to create a RESTful web service using Python and the Flask microframework.

## What is REST?

The characteristics of a REST system are dfined by six design rules:

1. **Client-Server**: There should be a separation between the server that offers a service and the client that consumes it.
2. **Stateless**: Each request from a client must contain all the information required by the server to carry out the request.
3. **Cacheable**: The server must indicate to the client if requests can be cached or not.
4. **Layered System**: Communication between a client/server should be standardized in a way that allows intermediaries to respond to requests instead of the end server, without the client having to do anything different.
5. **Uniform Interface**: The method of communication between a client/server must be uniform.
6. **Code On Demand**: Servers can provide executable code or scripts for clients to execute in their context. This is optional.

## What is a RESTful web service?

The REST architecture was originally designed to fit the HTTP protocol that the world wide web uses.

Central to the concept of RESTful web services is the notion of resources. Resources are represented by URIs. The clients send requests to these URIs using the methods defined by the HTTP protocol, and possibly as a result of that the state of the affected resource changes.

The HTTP request methods are typically designed to affect a given resource in standard ways.

| HTTP Method | Action                              | Examples                                                                                   |
|-------------|-------------------------------------|--------------------------------------------------------------------------------------------|
| GET         | Obtain information about a resource | http://example.com/api/orders (retrieve order list)                                        |
| GET         | Obtain information about a resource | http://example.com/api/orders/123 (retrieve order #123)                                    |
| POST        | Create a new resource               | http://example.com/api/orders (create a new order, from data provided with the request)    |
| PUT         | Update a resource                   | http://example.com/api/orders/123 (update order #123, from data provided with the request) |
| DELETE      | Delete a resource                   | http://example.com/api/orders/123 (delete order #123)                                      |

The REST design does not require a specific format for the data provided with the requests. In general data is provided in the request body as a JSON blob, or sometimes as arguments in the query string portion of the URL.
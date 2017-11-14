# General Backend Questions

## REST API.

Taken from: https://stackoverflow.com/questions/671118/what-exactly-is-restful-programming

REST stands for Representational State Transfer.
It advocates web apps should use HTTP
- GET for look up/read
- PUT for mutation
- POST for creation
- DELETE for deletion

Eg: A get request should never be used to update information.
`http://myserver.com/addToCart?cart=314159&item=1729`

REST is the underlying architectural principle of web.
- web clients (browsers) can interact with servers without the client knowing anything about the server/resources it holds (provides interoperability).
- client and server must agree on the media used (HTML)
- an API that adheres to REST principles does not require client to know anything about the API structure.

REST follows a set of standards for web services, where nouns are used in the URL and verbs defined by HTTP methods.

Rest routes to ask:
Eg: GET request on http://www.monplan.com/courses (GOOD) should get all courses instead of routes such as http://www.monplan.com/getAllCourses (BAD)

The following are just resources that you can discuss.
### Web resources
Are documents or files identified by their URLs (older definition).
Any entity that can be identified, name, addressed or handled in anyway on the web (newer more abstract definition).

### REST and Web resources
In a RESTful web service, requests made to a resource's URI will result in a response (JSON, XML, HTML).
The response may confirm alteration been made to a stored resource, provide links to other related resources etc.

By using a stateless protocol, REST aims for feast performance, reliability and ability to scale.

### Why is REST stateless
Taken from: https://stackoverflow.com/questions/3105296/if-rest-applications-are-supposed-to-be-stateless-how-do-you-manage-sessions

If there is a session state on the server, it is not REST.

>[...] each request from client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client. [...]

So you would pass your client_id, item_id, operation etc in your request. It will be stored on the client side so the server doesn't need to keep this.

Being stateless it means that the server can service any client at any time. This makes it easier to scale horizontally as client's are not tied down to a particular server instance.

`ST` in `REST` stands for state transfer. It means you pass around state instead of storing it in the server. This is the only way to scale to millions of concurrent users.

HTTP is designed to work stateless. It leads to simpler implementation instead of a bunch of server side logic to maintain session states.

### How do you handle sessions being stateless?
(Disclaimer: This is what I think would happen.)
In an example scenario such as a shopping site and a cart I would assume something along the follow lines happens:

A client (a person on their web browser) logs in, they get a session key with some expiration time etc. The server will handle authentication.
This client can then browse items and add them into their cart/favourite them and so forth. At each operation the client will make a REST call to update a data storage layer for that client_id.
This means that if the client gets off the web browser and accesses the site via mobile or another browser etc they will still have those items in their cart as it is stored in a data storage layer and is not session state.


## Describe MVC.


MVC stands for Model-View-Controller. It was introduced to remove the cyclic dependency with the Model-View pattern in which the view could update the model and the model could update the view.
In MVC the view is the representation layer, the model has the business logic and the controller handles the user input. So when you type some text on the view, it goes to the controller which parsers it and determines what to do with it. It might update the model. Then the view will update as the model has changed.

At monPlan our front end is independent to our backend.

Our front end uses React, Redux and NodeJS. React is a presentation (view) layer framework and Redux manages the state for the React components.
Popular front end libraries such as jQuery (DOM manipulation) can be seen as DOM manipulation API and not an architecture (http://www.j2eebrain.com/java-J2ee-jquery-architecture.html).
React is the V in MVC and can be used with other Js libraries/frameworks in MVC.
When paired with Redux it similar to the Flux architecture used by Facebook when dealing with React promoting unidirectional data flow dependent on mutation (https://stackoverflow.com/questions/32461229/why-use-redux-over-facebook-flux).

Our backend uses Java Spring and components of Google App Engine including their data storage layer Google Datastore. It is a REST API which is a MVC-like structure.
The business logic is carried out here.
There is no view layer, `controller` classes at as controllers and business logic is carried out by `service` classes with implementations in `repository` classes.
The view can be seen as JSON response to the front end, when it gets queried.

## Dependency Injection.

- Dependency = an object that can be used.
- Injection = passing the dependency to the dependent object (client that uses it).

Dependency injection is when you inject your concrete class at run time. When coding you would accept a superclass of your object which whose concrete implementation will be specified at run time.
This is useful in factories and makes code more modular.

Note: Only expected to know this if you have done FIT3077.
It inverts the control of your class hierarchy. Rather than low level code calling high level modules, high level code and receive lower level code it calls down to. It inverts the typical control pattern in procedural programming.

If the candidate has not done FIT3077 an answer like the following after explaining what dependency injection is will suffice.
- makes unit testing easier, easier testable code means mode modular code which you can assert is correct.
- decoupling your system.
- code reuse.

Example of dependency injection:
- Making a system for clients, inject the client.
- http://www.javacreed.com/why-should-we-use-dependency-injection/

This uses `Abstract Factories` along with `Dependency Injection`

```Java
public class ApplicationClient {
    public ApplicationClient() {}

    public ConcreteWidget createWidget(AbstractWidgetFactory factory) {
        // Even though the window and scrollbar is either dark or light we don't care as we
        // treat it as it's base class (upper most class in the hierarchy).
        AbstractWindow w = factory.createWindow();
        AbstractScrollBar s = factory.createScrollBar();

        ConcreteWidget widget = new ConcreteWidget(s, w);
        System.out.println("Client created: " + widget.getDescription());
        return widget;
    }
}
```
The `ApplicationClient` takes an `AbstractWidgetFactory` which is a super class of other concrete `WidgetFactory` implementations.

The driver code can then specific what concrete `WidgetFactory` to use at run time.

```Java
public class Driver {
    public static void main(String[] args) {
        ApplicationClient app = new ApplicationClient();
        ArrayList<ConcreteWidget> myWidgets = new ArrayList<>();

        AbstractWidgetFactory currentFactory = new ConcreteDarkWidgetFactory();
        ConcreteWidget newWidget =  app.createWidget(currentFactory);
        myWidgets.add(newWidget);

        AbstractWidgetFactory anotherFactory = new ConcreteLightWidgetFactory();
        ConcreteWidget anotherWidget = app.createWidget(anotherFactory);
        myWidgets.add(anotherWidget);
    }
}
```
This has the following advantages:
- code reuse of `AbstractFactory`, following other OO principles the implementation classes will have the same interface as the abstract class.
- able to select concrete class at run time which is useful for when you don't know what concrete class you will need to use i.e. based on user input.

## What is the difference between query params and request body. When should I use query params and when should I use request body.

Note `GET` also has a limit length.
Large data typically goes to request body.
The query component is indicated by the `?` in the url. Query params (a.k.a string) is a query as part of the url.

Example:
- http://example.com/foo?bar
- http://example.com/foo/foo/foo?bar/bar/bar
- http://example.com/?bar
- http://example.com/?@bar._=???/1:

Query params are usually used for search terms i.e. http://example.com/item?itemId in `GET` requests.

Request body is used in `POST` and `PUT` requests to hold information in a JSON format.

Actions/instructions such as taking a screenshot that requires a `url`, `height` and `width`.
Setting the height and width can be considered an instruction for where to take the screenshot.
These should be put in request body.

# Cookies

**What is the difference between _cookies_, _localStoage_ and _sessionStorage_**

|  |`cookie`|`localStorage`|`sessionStorage`|
|--|--|--|--|
| Initiator | Client or server. Server can use `Set-Cookie` header | Client | Client |
| Expiry | Manually set | Forever | On tab close |
| Persistent across browser sessions | Depends on whether expiration is set | Yes | No |
| Have domain associated | Yes | No | No |
| Sent to server with every HTTP request| Cookies are automatically being sent via `Cookie` header | No | No |
| Capacity (per domain) | 4kb | 5MB | 5MB |
| Accessibility | Any window | Any window | Same tab |


Note: Material taken from monPlan summer 2017 coding interviews.
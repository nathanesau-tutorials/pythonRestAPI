# Design

The task of designing a web service or API that adheres to the REST guidelines then becomes an exercise in identifying the resources that will be exposed and how they will be affected by the different request methods.

Let's say we want to write a todo list application and we want to design a web service for it. The first thing to do is to decide what is the root URL to access this service. For example, we could expose this service as:

```
http://[hostname]/todo/api/v1.0/
```

Here I have decide to include the name of the application and the version of the API in the URL. Including the application name in the URL is useful to provide a namespace that separates this service from others than can be running on the same system. Including the versin in the URL can help with making updates in the future, since new and potentially incompatible functions can be added under a new version, without affecting applications that rely on the older functions.

The next step is to select the resources that will be exposed by this service. This is an extremely simple application, we only have tasks, so our only resource will be the tasks in our todo list.

Our tasks resource will use HTTP methods as follows:

| HTTP Method | URI                                             | Action                  |
|-------------|-------------------------------------------------|-------------------------|
| GET         | http://[hostname]/todo/api/v1.0/tasks           | Retrieve list of tasks  |
| GET         | http://[hostname]/todo/api/v1.0/tasks/[task_id] | Retrieve a task         |
| POST        | http://[hostname]/todo/api/v1.0/tasks           | Create a new task       |
| PUT         | http://[hostname]/todo/api/v1.0/tasks/[task_id] | Update an existing task |
| DELETE      | http://[hostname]/todo/api/v1.0/tasks/[task_id] | Delete a task           |

We can define a task as having the following fields:

* ``id``: unique identifier for tasks. Numeric type.
* ``title``: short task description. String type.
* ``description``: long task description. Text type.
* ``done``: task completion state. Boolean type.

And with this we are basically done with the design part of our web service. All that is left is to implement it!
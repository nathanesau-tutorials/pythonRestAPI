# Implementation

Building web services with Flask is surprisingly simple. Note: the author of the guide I am following for this project (Miguel Grinberg) wrote a very good Flask textbook and is just very knowledgeable about Python and Flask in general. Also, they are a good writer (their blog is easy to follow).

The clients of our web service will be asking the service to add, remove and modify tasks, so clearly we need to have a way to store tasks. The obvious way to do that is to build a small database, but because database are not the topic of this article we are going to take a much simpler approach.

In place of a database we will store our task list in a memory structure. This will only work when the web server that runs our application is a single process and single threaded. This is okay for Flask's own development web server. It is not okay to use this technique on a priduction web server. For that a proper database setup must be used.

# Improvements to Basic REST API

Return URI with each task instead of ID.

```python
from flask import url_for

def make_public_task(task);
    new_task = {}
    for field in task:
        if field == 'id': # replace 'id' with 'uri'
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})
```


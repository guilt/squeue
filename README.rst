******************************
squeue: A simple SQLite Queue
******************************

squeue is used to create simple queues that can be persisted, 
then retrieved for work. It's very easy to create a mini workflow
engine with this.

=============
Main Features
=============

* Very compact
* Few Dependencies

=====
Usage
=====

One can create a new queuable function (or unit of work) by using the
@queuefunc decorator.

.. code-block:: python

    @queue_function
    def hello(world):
        return "Hello, {}!".format(world)
    hello.delay("World")

It will get invoked when a worker process fetches a function
to execute. Do check the provided test.py with this distribution.

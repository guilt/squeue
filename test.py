#!/usr/bin/env python
"""
squeue: A simple SQLite Queue
"""
from six.moves.urllib.request import urlopen
from squeue import queue_function, dequeue_function

@queue_function
def count_words_at_url(url):
    """Just an example function that's called async."""
    return len(urlopen(url).read().split())

@queue_function
def add_three(a, b, c):
    """Just another example function that's called async."""
    return a + b + c

@queue_function
def hello(world):
    """Hello, You!"""
    return "Hello, {}!".format(world)

def dequeue_loop():
    """Dequeue jobs in Queue."""
    while True:
        result = dequeue_function()
        if not result:
            break
        print(result)

def main():
    """Main function."""
    for _ in range(5):
        hello.delay("World")
        add_three.delay(2, 3, 4)
        count_words_at_url.delay("http://karthikkumar.org")
    dequeue_loop()

if __name__ == "__main__":
    main()

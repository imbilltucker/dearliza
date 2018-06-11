# What this heck is this?

- A service that keeps track of how many requests per second it is receiving.
- A client that can throttle the number of requests per second it can send concurrently.

# What does it do?
    A Client gets created.
    It generates some requests against the server (asyncio Tasks)
    Tasks are put in an asyncio Queue, if it's below a limit
    If Task can't be put on Queue, it can error, or we can wait.


# How do I make it go?
    `python3 socket_server.py`
    `python3 socket_client.py`


# Background on asyncio

    Tools for end-user developers:
        - `async def` and `await`
        - event loop
    Tools for framework developer:
        - all the others

    Here's a basic structure for running an asyncio process:
        Event Loop
            `loop = asyncio.get_event_loop()`
        Watch for a cancel (e.g. control-c) or error condition.
        ```
            async def main():
                await asyncio.sleep(1.0)
                loop.stop()

            loop = asyncio.get_event_loop()
            loop.create_task(main())
            loop.run_in_executor(None, blocking)
            try:
                # do stuff
                loop.run_forever()
            except KeyboardInterrupt    # watch for cancel
                print("Ending processing")
            finally:  # Clean up and exit
                pending = asyncio.Task.all_tasks(loop=loop)
                group = asyncio.gather(*pending)
                loop.run_until_complete(group)
                loop.close()
        ```
# Resources for asyncio

    https://www.pythonsheets.com/notes/python-asyncio.html
    Using Asyncio in Python 3:  https://www.safaribooksonline.com/library/view/using-asyncio-in/9781491999691/

from flask import current_app
from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler
class StreamableChain:
    def stream(self, input):

        queue = Queue()
        handler = StreamingHandler(queue)

        def task(app_context):
            # Get access to current context
            app_context.push()
            self(input, callbacks=[handler])

        # Pass current app context to thread, as flask has limitation, 
        # that new threads cant access context
        Thread(target=task, args=[current_app.app_context()]).start()
        while True:
            token = queue.get() 
            if token is None:
                break
            yield token

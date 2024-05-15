from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from queue import Queue
from threading import Thread
load_dotenv()

queue = Queue()

class StreamingHandler(BaseCallbackHandler):
    def __init__(self, queue):
        self.queue = queue

    def on_llm_new_token(self, token, **kwargs):
        self.queue.put(token)

    def on_llm_end(self, response, **kwargs):
        self.queue.put(None)
        

    def on_llm_error(self, error, **kwargs):
        self.queue.put(None)

chat = ChatOpenAI(
        streaming=True
        )

prompt = ChatPromptTemplate.from_messages(
        [("human", "{content}")]
        )

class StreamableChain:
    def stream(self, input):

        queue = Queue()
        handler = StreamingHandler(queue)

        def task():
            self(input, callbacks=[handler])

        Thread(target=task).start()
        while True:
            token = queue.get() 
            if token is None:
                break
            yield token

# New class mixin of streaming class and llmchain. 
# Easy to extend and support conversationChain, by just 
# Creating a new class that extended StreamableChain and ConversationalRetrievalChain
class StreamingChain(StreamableChain, LLMChain):
    pass

chain = StreamingChain(llm=chat, prompt=prompt)
# chain = LLMChain(llm=chat, prompt=prompt)
for output in chain.stream(input={'content': 'Tell me a joke'}):
    print(output)

#for output in chain.stream(input={"content": "Tell me a joke"}):
#    print(output)
# messages = prompt.format_messages(content="tell me a joke")



# output = chat.stream(messages)
# print(output)
# for message in chat.stream(messages):
#     print(message)

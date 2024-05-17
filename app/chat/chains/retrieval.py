
from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain
from app.chat.chains.traceable import TraceableChain

# Custom class implementing stream and conversationalStream
class StreamingConversationalRetrievalChain(
    TraceableChain,
    StreamableChain,
    ConversationalRetrievalChain
):
    pass


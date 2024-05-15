
from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain

# Custom class implementing stream and conversationalStream
class StreamingConversationalRetrievalChain(
    StreamableChain,
    ConversationalRetrievalChain
):
    pass


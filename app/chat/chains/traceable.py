from langfuse.model import CreateTrace
from app.chat.tracing.langfuse import langfuse

class TraceableChain:
    # Function that gets executed always when chain runs.
    def __call__(self, *args, **kwargs):
        '''
        Intercept every call to chain and log it to trace tool
        '''
        # Callback handler
        trace = langfuse.trace(
            CreateTrace(
                # id will be the key so either new trace or append to trace 
                # with this key
                id=self.metadata["conversation_id"],
                metadata=self.metadata
                )
            )
    
        # Add to list of callbacks
        callbacks = kwargs.get("callbacks", [])
        callbacks.append(trace.getNewHandler())
        kwargs["callbacks"] = callbacks
        
        # Pass callbacks on to actual call of chain
        return super().__call__(*args, **kwargs)


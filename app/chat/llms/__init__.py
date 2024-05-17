from functools import partial
from .chatopenai import build_llm


# map and partial let us load function before hand, and can then call 
# map with keyword to get wanted model while reusing function
llm_map = {
        "gpt-4": partial(build_llm, model_name="gpt-4"),
        "gpt-3.5-turbo": partial(build_llm, model_name="gpt-3.5-turbo"),
        }


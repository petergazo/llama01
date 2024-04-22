# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="res/Meta-Llama-3-8B-Instruct.Q8_0.gguf")

# create a text prompt
prompt = "Q: Explain general teory of relativity on example of trains and flashlight. A:"

# set max_tokens to 0 to remove the response size limit
# output = LLM(prompt)
output = LLM(prompt, max_tokens=0) # not limit on number of tokens produced


# display the response
print(output["choices"][0]["text"])
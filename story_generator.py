#
import os
import openai
from api_key import KEY

key = KEY
# openai.api_key = os.getenv(key)
openai.api_key = key

prompt = "Write me a short story with an ending about a child lost in the woods but there is hope."

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
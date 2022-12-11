#
import os
import openai
from api_keys import OPEN_AI_API_KEY


# openai.api_key = os.getenv(key)
# openai.api_key = key

# prompt = "Write me a short story with an ending about a child lost in the woods but there is hope."


def get_story(prompt):
    openai.api_key = OPEN_AI_API_KEY
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response


def gradio_input_to_story(gradio_input):
    # prompt = ''
    formatted_prompt = "Write me a short story with an ending about " + gradio_input
    story = get_story(formatted_prompt)
    return story['choices'][0]['text']

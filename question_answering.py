import openai
from api_keys import OPEN_AI_API_KEY
from text_to_prompt import read_story


def get_answer(story, question):
    story = read_story("inputs/text/story.txt")

    question = 'Who was the old man?'

    prompt = f"""Answer the questions with a positive sentiment using provided text, and if the answer is not contained within the text below, say "No one knows" in a mysterious positive way.

    Context:
    {story}

    Q: {question}
    A: """
    openai.api_key = OPEN_AI_API_KEY
    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )["choices"][0]["text"].strip(" \n")
    
    print(response)

get_answer('','')
  
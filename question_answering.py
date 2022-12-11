import openai
from api_keys import OPEN_AI_API_KEY, ASSEMBLY_AI_API_KEY
from text_to_prompt import read_story
import requests
import time
import speech_utils

def get_answer(story, question):

    # question = 'Who was the old man?'

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
    return response

       
def get_question(audio_file_path="https://storage.googleapis.com/bucket/b2c31290d9d8.wav", upload=True):
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": audio_file_path
        }
    headers = {
        "Authorization": ASSEMBLY_AI_API_KEY,
        "Content-Type": "application/json"
        }
    
    if upload:
        upload_url = speech_utils.upload_file(audio_file_path, headers)
    else:
        upload_url = {'upload_url': audio_file_path}
    transcription = speech_utils.request_transcript(upload_url, headers)
    polling = speech_utils.make_polling_endpoint(transcription)
    speech_utils.wait_for_completion(polling, headers)
    text = speech_utils.get_paragraphs(polling, headers)
    # response = get_transcription_result(headers, json, endpoint)
    # response = requests.post(endpoint, json=json, headers=headers)
    print(text[0]['text'])
    return text[0]['text']

# get_answer('','')
def question_answering():
    story = read_story("inputs/text/story.txt")
    question = get_question('inputs/audio/question.mp3')
    answer = get_answer(story, question)
    print(answer)
    return answer

question_answering()
  
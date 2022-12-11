import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))
from math import ceil, floor
import random

def get_audio_length(audio_length):
    return audio_length

def chunk_into_n(lst, n):
  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )

def round_to_multiple(number, multiple):
    return multiple * ceil(number / multiple)

# Rounding 23 to a multiple of 5


# sent_tokenize is one of instances of
# PunktSentenceTokenizer from the nltk.tokenize.punkt module
 
def read_story(file_path):
    f = open(file_path, "r")
    return f.read()

def sentence_split(paragraph):
    return paragraph.split('.')

def tokenize_sentence(sentence):
    return sent_tokenize(sentence)

def get_tags_list():
    # return ['VBG', 'JJ','NNS', 'VBD', 'VBN', 'NN', 'VB']
    return ['VBG', 'VBD', 'NNS', 'VBN', 'NN', 'VB']


def filter_stop_words(tokens):
    wordsList = nltk.word_tokenize(tokens)
    wordsList = [w for w in wordsList if not w in stop_words]
    # tagged = nltk.pos_tag(wordsList)
    # wordsList = [w[0] for w in tagged if w[-1] in get_tags_list()]
    return wordsList

def get_prompt(story_path = "data/text/story.txt"):
    story = read_story(story_path)
    sentences = sentence_split(story)
    tokenized_sentences = map (lambda x: tokenize_sentence(x) ,sentences)
    prompts = []

    for sentence in tokenized_sentences:
        if sentence:
            filtered_tokens = filter_stop_words(sentence[0])
            # 
            prompts.append(' '.join(filtered_tokens))
            # print(filtered_tokens)
            # break
    return prompts

def chunking_recursive(no_of_images, prompt, counter):
    if no_of_images < 0.7 * len(prompt):
        return chunk_into_n(prompt, no_of_images)
    else:
        value = prompt[counter]
        prompt.insert(counter+1,value)
        chunking_recursive(no_of_images, counter+3)

def segment_prompts():
    prompt = get_prompt()
    audio_length = get_audio_length(5) # pass path of audio
    duration = 5 # number of seconds an image is shown
    no_of_images = round_to_multiple(audio_length, duration)
    chunk = chunking_recursive(no_of_images, prompt, 0)
    return chunk

def add_key_words():
    general = ['mdjrny-v4 style', 'animation', 'highly detailed', 'sharp focus', 'illustration', '8k', 'vivid colors', 'magical']
    light = ['bright', 'dark', 'humid', 'mist']
    art = ['artstation', 'concept art', 'smooth', 'high contrast', 'Matte painting', 'photorealistic', 'concept art', 'digital painting']
    return general+[ random.choice(light)] + [random.choice(art)]

def generate_prompts():
    prompts = segment_prompts()
    final_prompts = []
    for prompt in prompts:
        selection = add_key_words()
        prompt = prompt + selection
        # print(prompt)
        # print('-'*20)
        # print(selection)
        # value = ', '.join(prompt)
        final_prompts.append(prompt)
        # print(value)
        # break
    print(final_prompts)
    return final_prompts


generate_prompts()

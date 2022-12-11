import librosa
import os
import random
from math import ceil, floor
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))


def get_audio_length(audio_path):
    files = [filename for filename in os.listdir(
        audio_path) if filename.startswith("audio")]
    duration = 0
    # print(audio_path)
    # print(files)
    if files:
        for file in files:
            file_path = audio_path+'/'+file
            # print('File path: ', file_path)
            duration += librosa.get_duration(filename=file_path)
    # print('Duration of audio: ', duration)
    return duration


def chunk_into_n(lst, n):
    size = ceil(len(lst) / n)
    print(lst, n, len(lst))
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(n)))
    )


def round_to_multiple(number, multiple):
    return ceil(number / multiple)

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


def get_prompt(story_path="inputs/text/story.txt"):
    story = read_story(story_path)
    sentences = sentence_split(story)
    tokenized_sentences = map(lambda x: tokenize_sentence(x), sentences)
    prompts = []

    for sentence in tokenized_sentences:
        if sentence:
            filtered_tokens = filter_stop_words(sentence[0])
            #
            prompts.append(' '.join(filtered_tokens))
            # print(filtered_tokens)
            # break
    # print(prompts)
    return prompts


def chunking_recursive(no_of_images, prompt, counter):
    lenght_of_prompt = len(prompt)
    if counter >= lenght_of_prompt:
        counter = ceil(lenght_of_prompt/2)

    if no_of_images == lenght_of_prompt:
        # return chunk_into_n(prompt, no_of_images)
        # print('-'*300)
        # print(prompt, lenght_of_prompt)
        return prompt

    elif no_of_images < lenght_of_prompt:
        return chunk_into_n(prompt, no_of_images)

    else:
        value = prompt[counter]
        prompt.insert(counter+1, value)
        # print(no_of_images, lenght_of_prompt, counter, prompt)
        return chunking_recursive(no_of_images, prompt, counter+3)


def segment_prompts():
    prompt = get_prompt()
    audio_length = get_audio_length('outputs/audio')  # pass path of audio
    duration = 5  # number of seconds an image is shown
    no_of_images = round_to_multiple(audio_length, duration)
    chunk = chunking_recursive(no_of_images, prompt, 0)
    # chunk = chunking_recursive(5, prompt, 0)

    # print('-'*200)
    # print(chunk)
    return chunk


def add_key_words():
    general = ['mdjrny-v4 style', 'animation', 'highly detailed',
               'sharp focus', 'illustration', '8k', 'vivid colors', 'magical']
    light = ['bright', 'dark', 'humid', 'mist']
    art = ['artstation', 'concept art', 'smooth', 'high contrast',
           'Matte painting', 'photorealistic', 'concept art', 'digital painting']
    return general+[random.choice(light)] + [random.choice(art)]


def generate_prompts():
    prompts = segment_prompts()
    final_prompts = []
    # print('Prompts: ', prompts, type(prompts))
    for prompt in prompts:
        selection = add_key_words()
        # print(prompt, selection)

        prompt = [prompt] + selection
        # print(prompt)
        # print('-'*20)
        # print(selection)
        # value = ', '.join(prompt)
        final_prompts.append(prompt)
        # print(value)
        # break
    # print(final_prompts, len(final_prompts))
    return final_prompts

#
from story_generator import gradio_input_to_story
# from 
from text_to_prompt import get_audio_length

if __name__ == '__main__':
    # get gradio text
    gradio_input = ''
    story = gradio_input_to_story(gradio_input)
    audio_length = get_audio_length('outputs/audio') # pass path of audio

    story_voice = 
    story_to_uberduck_voice = ''
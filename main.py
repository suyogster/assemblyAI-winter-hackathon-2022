#
from story_generator import gradio_input_to_story
# from
from text_to_prompt import get_audio_length
from text_to_music import music_generator
from text_to_speech_converter import generate_speech
from text_to_image import generate_image
from text_to_prompt import generate_prompts
from image_to_video import generate_video

from utils import runcmd

if __name__ == '__main__':
    get gradio text
    gradio_input = 'Journey of a poor boy becoming rich after helping an unknown old man'

    story = gradio_input_to_story(gradio_input)
    f = open("./inputs/text/story.txt", "w")
    f.write(story)
    f.close()

    print('Generated Story')

    story_voice = generate_speech(story)
    print('Generated story_voice')

    audio_length = get_audio_length('./inputs/audio')  # pass path of audio
    print('Generated Audio Length')

    background_music = music_generator(duration=audio_length)
    runcmd('wget -O /inputs/audio/music.mp3 '+ background_music)

    print('Generated background_music')


    prompts = generate_prompts(audio_length)
    # print('Generated Prompts')

    story_images = generate_image(prompts)
    print('Generated Images')

    # prompts = [1,2,3,4]
    story_video = generate_video(len(prompts))

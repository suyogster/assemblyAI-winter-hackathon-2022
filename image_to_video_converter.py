from moviepy.editor import *
from pathlib import Path

img_clips = []
path_list = []
image_folder = "images"
audioclip = AudioFileClip("./audio/30-sec-audio.mp3")
# accessing path of each image
for image in os.listdir(image_folder):
    if image.endswith(".jpg"):
        path_list.append(os.path.join(image_folder, image))
# creating slide for each image
for img_path in path_list:
    slide = ImageClip(img_path, duration=2)
    img_clips.append(slide)
# concatenating slides
video_slides = concatenate_videoclips(
    img_clips, method='compose').set_audio(audioclip)
# exporting final video
video_slides.write_videofile("./videos/output_video.mp4", fps=24)

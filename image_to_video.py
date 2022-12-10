from moviepy.editor import *
from pathlib import Path

img_clips = []
path_list=[]
lock = 0
#accessing path of each image
img_path = '/home/spygaurad/Documents/images_delete/'
for image in os.listdir(img_path):
    if image.endswith(".jpg"):
        path_list.append(os.path.join(img_path, image))
#creating slide for each image
# print(path_list)
path_list.sort()
for img_path in path_list:
    slide = ImageClip(img_path,duration=5)
    img_clips.append(slide)

video = concatenate_videoclips(img_clips, method='compose')
video.write_videofile("output.mp4", fps=24)

clip1 = VideoFileClip("output.mp4")
subclips = []
no_of_clips = 7
x = 0
for i in range(no_of_clips):
    clip = clip1.subclip(x,x+5)
    clip = clip.crossfadeout(1.0)
    clip = clip.crossfadein(2.0)
    subclips.append(clip)
    x +=5
  
# showing final clip
final = concatenate_videoclips(subclips, method='compose')
final.write_videofile("Generated_story.mp4", fps=24)
os.remove("output.mp4")

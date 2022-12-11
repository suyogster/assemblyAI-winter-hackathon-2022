import replicate
from api_keys import REPLICATE_TOKEN

repl = replicate.Client(api_token=REPLICATE_TOKEN)
model = repl.models.get("stability-ai/stable-diffusion")
version = model.versions.get(
    "27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
print(version.predict(
    prompt="Once upon a time there were a group of kids who lived in a small village near the woods, hd, positive vibe, bright light, no faces, trending on ArtStation, subtle muted cinematic colors, made in Maya, Blender and Photoshop, octane render, excellent composition, cinematic atmosphere, dynamic dramatic cinematic lighting, aesthetic, very inspirational, arthouse"))

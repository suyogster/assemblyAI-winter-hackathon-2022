import replicate
from api_key import REPLICATE_TOKEN
import requests

repl = replicate.Client(api_token=REPLICATE_TOKEN)
model = repl.models.get("stability-ai/stable-diffusion")
version = model.versions.get(
    "27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")


def generate_image(prompts):
    url = version.predict(prompt=prompts)
    img_data = requests.get(url).content
    open(f'./inputs/images/{img_data.title}',
         'wb').write(img_data)

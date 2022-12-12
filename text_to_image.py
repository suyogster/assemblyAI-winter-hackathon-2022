import replicate
from api_keys import REPLICATE_TOKEN
import requests
import shutil
repl = replicate.Client(api_token=REPLICATE_TOKEN)
model = repl.models.get("stability-ai/stable-diffusion")
version = model.versions.get(
    "27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")


def generate_image(prompts):
    counter = 0
    for item in prompts:
        prompt = ', '.join(item)
        print('-'*300,prompt)

        url = version.predict(prompt=prompt)
        # url = 'https://replicate.delivery/pbxt/WVz8GeooKv1jE62fErO3bgoDsTtVipUezBO4BU1yU8YJixRgA/out-0.png'
        print(url)

        response = requests.get(url[0], stream=True)

        with open('./inputs/images/'+str(counter)+'.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        counter +=1
        # break
    return ''

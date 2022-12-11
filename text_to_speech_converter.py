import requests
from api_keys import UBER_DUCK_API_SECRET, UBER_DUCK_KEY

speeches = ['Once upon a time there was a young child who lived in a small village near the woods. The child was a curious one and loved to explore the woods, but one day the child lost their way. The sun was setting and the little one was scared and alone, not knowing what to do.The child stumbled through the trees, but it was getting dark and they could no longer see the way. Suddenly, through the fog, the child heard a faint sound of music. Following the sound, the child eventually stumbled upon a small clearing in the woods. There were two people playing music together, an old man with a guitar and a young woman with a fiddle.',
            'The old man noticed the child and smiled warmly. He said, “It looks like you’ve lost your way. Don’t worry, I will take you home.”The old man and the young woman walked the child back to their village. As they walked, the old man explained to the child that through life, there will always be moments of fear and uncertainty, but if we remain hopeful and have faith, then we will eventually find our way back home.']

url = "https://api.uberduck.ai/speak"

headers = {
    "accept": "application/json",
    "uberduck-id": "anonymous",
    "content-type": "application/json"
}

for i in range(len(speeches)):
    payload = {"speech": speeches[i], "voices": "zwf"}
    speak_response = requests.post(url, json=payload, headers=headers, auth=(
        UBER_DUCK_KEY, UBER_DUCK_API_SECRET))
    print(f'i: {i}', speak_response.json()["uuid"])

    headers1 = {"accept": "application/json"}
    received = False
    while received is False:
        print("Fetching data.....")
        status_response = requests.get(
            f'https://api.uberduck.ai/speak-status?uuid={speak_response.json()["uuid"]}', headers=headers1, auth=(
                UBER_DUCK_KEY, UBER_DUCK_API_SECRET))
        if status_response.json()["path"] is not None:
            received = True
            path = status_response.json()["path"]
            print(path)
            path_response = requests.get(path)
            open(f'./audio/audio{i}.mp3', 'wb').write(path_response.content)
            print(f'audio{i} downloaded')

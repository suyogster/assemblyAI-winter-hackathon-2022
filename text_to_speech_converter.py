import requests
from api_key import UBER_DUCK_API_SECRET, UBER_DUCK_KEY

url = "https://api.uberduck.ai/speak"

headers = {
    "accept": "application/json",
    "uberduck-id": "anonymous",
    "content-type": "application/json"
}


def generate_speech(speeches):
    # for i in range(len(speeches)):
    payload = {"speech": speeches, "voices": "zwf"}
    print(payload)
    speak_response = requests.post(url, json=payload, headers=headers, auth=(
        UBER_DUCK_KEY, UBER_DUCK_API_SECRET))
    print(speak_response.text)
    print(speak_response.json()["uuid"])

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
            open(f'./inputs/audio/audio.mp3',
                 'wb').write(path_response.content)
            print(f'audio downloaded')

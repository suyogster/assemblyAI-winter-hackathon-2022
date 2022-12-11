# AI TALEBOOK

Ai Talebook is an AI solution for providing a complete storytelling experience.

<!-- ![](https://github.com/suyogster/assemblyAI-winter-hackathon-2022/blob/master/inputs/ai_talebook.jpg) -->
<img src="https://github.com/suyogster/assemblyAI-winter-hackathon-2022/blob/master/inputs/ai_talebook.jpg" width="812" height="512">


## Components
Due to GPU and computation limitations we used following components:
- **A Story Generator** : Open AI API
- **Story Text To Voice Generator** : Uberduck API
- **Background Music Generator** : MuBert
- **Text to Prompt to Image Generator** : Replicate
- **Image, Music, Voice To Video Generator** : MoviePy
- **Question Answering the Story**: Assembly API, Open AI API

## More about AI Talebook
<img src="https://github.com/suyogster/assemblyAI-winter-hackathon-2022/blob/master/inputs/Talebook_diagram.png" width="1080" height="1920">

## Installation

Activate env and install requirements.

```python
pip install -r requirements.txt

```

## Run

```python
uvicorn main:app --reload
```

- You can use the API **generateVideo(character_name, plot)** to get the story and the generated video URL from the API.

## Demo
** Please check us out at <link src="https://huggingface.co/spaces/suyogster/assemblyAI-winter-hackathon-2022"/>**


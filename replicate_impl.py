import replicate
repl = replicate.Client(api_token="4d62d765b827468b0885f14240f59de8a8ab3b43")
model = repl.models.get("stability-ai/stable-diffusion")
version = model.versions.get(
    "27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
print(version.predict(prompt="a 19th century portrait of a wombat gentleman"))

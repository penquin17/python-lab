# https://huggingface.co/facebook/musicgen-small
from typing import Any

import ray
import scipy
from fastapi import FastAPI
from pydantic import BaseModel
from ray import serve
from transformers import pipeline

# ray.init()
# Start Ray Serve with a custom port
# serve.start(http_options={"host": "0.0.0.0", "port": 8080})
app = FastAPI()


class Input(BaseModel):
    text: str


@serve.deployment(
    # route_prefix="/",
    # num_replicas=1,
    # Resource allocation
    ray_actor_options={"num_cpus": 2, "num_gpus": 0},
    autoscaling_config={
        "min_replicas": 1,
        "max_replicas": 5,
        "target_num_ongoing_requests_per_replica": 10
    },
    name="music_generator"  # Name of the deployment
)
@serve.ingress(app)
class MusicGenerator:
    def __init__(self):
        # Load the model when deployment starts
        self.synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

    def gen_music(self, description: str):
        try:
            music = self.inference(description)
            self.write_audio(music)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    @app.post("/gen_music")
    def gen_music_route(self, input: Input):
        description = input.text
        success = self.gen_music(description)
        return {"success": success}

    def inference(self, description: str):
        music = self.synthesiser("lo-fi music with a soothing melody",
                                 forward_params={"do_sample": True})
        return music

    def write_audio(self, audio: Any, path: str = './temp/audio.wav'):
        scipy.io.wavfile.write(path, rate=audio["sampling_rate"],
                               data=audio["audio"])

serve.start(http_options={"host": "0.0.0.0", "port": 8000})
music_generator = MusicGenerator.bind()
serve.run(music_generator, route_prefix="/v1")


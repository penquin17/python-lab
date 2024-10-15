```bash
cd serve-ray-fastapi
docker pull continuumio/miniconda3
docker build -f dockerfile -t python-lab:serve-ray-fastapi .
docker run -it -v "./app":"/code" -v "./models":"/models" -p 8000:8000 python-lab:serve-ray-fastapi
```

```python
# quick test
import requests
url = "http://localhost:8000/v1/gen_music"
data = {"text": "Heal the world"}
response = requests.post(url, json=data)
```
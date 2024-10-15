# https://huggingface.co/docs/huggingface_hub/v0.25.2/package_reference/file_download
import huggingface_hub

model_name = "facebook/musicgen-small"
local_dir = huggingface_hub.snapshot_download(model_name, cache_dir='./models')
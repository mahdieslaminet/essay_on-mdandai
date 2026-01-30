import torch
from transformers import AutoProcessor, AutoModelForCausalLM

MODEL_NAME = "ZJU-AI4H/Hulu-Med-4B"

def load_model():
    processor = AutoProcessor.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
        torch_dtype=dtype
    ).to(device)

    model.eval()
    return processor, model

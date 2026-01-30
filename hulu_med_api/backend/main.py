from multiprocessing.connection import answer_challenge
from platform import processor

from fastapi import FastAPI, UploadFile, File, Form
from PIL import Image
import torch
import io

from model_loader import load_model

app = FastAPI(title= "Hulu-Med API")

processor, model = load_model()

@app.post("/infer")
async def infer(
        image: UploadFile = File(...),
        prompt: str = Form(...)
):
    # --- load image ---
    image_bytes = await image.read()
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    # --- prepare inputs ---
    inputs = processor(
        text=prompt,
        images=img,
        return_tensors="pt"
    )
    for k in inputs:
        inputs[k] = inputs[k].to(model.device)

    # --- inference ---
    with torch.interface_mode():
        output_ids = model.generate(
            **inputs,
            max_new_token=128,
            temperature=0.2,
            do_sample=False
        )

    answer = processor.batch_decode(
        output_ids,
        skip_special_tokens= True
    )[0]

    return {
        "answer": answer.strip()
    }

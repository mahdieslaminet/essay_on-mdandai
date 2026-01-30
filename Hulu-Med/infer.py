
import argparse
import torch
from transformers import AutoModelForCausalLM, AutoProcessor, BitsAndBytesConfig
from PIL import Image

def main(args):
    # Load processor
    processor = AutoProcessor.from_pretrained(
        "ZJU-AI4H/Hulu-Med-7B",
        trust_remote_code=True
    )

    # Quantization config
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        "ZJU-AI4H/Hulu-Med-7B",
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        quantization_config=quant_config,
        attn_implementation="flash_attention_2"
    )

    # Load image
    image = Image.open(args.image_path).convert("RGB")

    # Prepare inputs
    inputs = processor(
        images=image,
        text=args.prompt,
        return_tensors="pt"
    ).to(model.device)

    # Generate output
    output_ids = model.generate(
        **inputs,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature
    )

    output_text = processor.decode(output_ids[0], skip_special_tokens=True)
    print("\\n======================")
    print("OUTPUT:")
    print("======================\\n")
    print(output_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_path", type=str, required=True)
    parser.add_argument("--prompt", type=str, default="یک گزارش پزشکی کامل بنویس.")
    parser.add_argument("--max_new_tokens", type=int, default=512)
    parser.add_argument("--temperature", type=float, default=0.7)
    args = parser.parse_args()

    main(args)

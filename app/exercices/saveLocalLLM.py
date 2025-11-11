from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = "qwen/qwen3-4b-thinking-2507"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Test
input_text = "Bonjour, comment vas-tu ?"
inputs = tokenizer(input_text, return_tensors="pt", truncation=True)

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=50, do_sample=True, temperature=0.7)

print("Output : ", tokenizer.decode(outputs[0]))

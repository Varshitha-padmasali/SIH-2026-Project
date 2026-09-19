from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "ai4bharat/IndicBART"

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    do_lower_case=False,
    use_fast=False,
    keep_accents=True
)

print("Loading model...")

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

print("Model loaded!")

# Hindi educational sentence
text = "पौधों को बढ़ने के लिए पानी और सूर्य के प्रकाश की आवश्यकता होती है।"

print("\nInput:")
print(text)

# Tokenize
inputs = tokenizer(
    text,
    return_tensors="pt",
    padding=True
)

# Generate output
outputs = model.generate(
    **inputs,
    max_length=100,
    num_beams=4
)

# Convert model output back to text
result = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("\nModel output:")
print(result)
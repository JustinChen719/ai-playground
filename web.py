from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

app = FastAPI()

# Initialize
model_path = 'Helsinki-NLP/opus-mt-en-zh'
translate_tokenizer = AutoTokenizer.from_pretrained(model_path)
translate_model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# pipeline
translation_pipeline = pipeline("translation", model=translate_model, tokenizer=translate_tokenizer, device="cuda")

cache = {}

@app.get('/translate/{text}')
async def translate_text(text: str):
    if text in cache:
        return cache[text]
    translated_text = translation_pipeline(text)[0]['translation_text']
    cache[text] = translated_text
    print(f"{text} ---> {translated_text}")
    return {'translated_text': translated_text}




# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="ibm-granite/granite-3.3-2b-instruct")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)

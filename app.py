import gradio as gr
from transformers import pipeline

# Load pre-trained model and tokenizer
generator = pipeline('text-generation', model='gpt2')

def generate_text(prompt):
    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

interface = gr.Interface(fn=generate_text, inputs="text", outputs="text")
interface.launch()
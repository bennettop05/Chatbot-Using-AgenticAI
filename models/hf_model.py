from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

def load_hf_llm():
    generator = pipeline(
        "text-generation",
        model="mistralai/Mistral-7B-Instruct-v0.1",  
        max_new_tokens=200
    )
    return HuggingFacePipeline(pipeline=generator)

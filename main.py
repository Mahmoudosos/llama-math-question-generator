import os
from llama_cpp import Llama
from google.colab import drive
from IPython.display import Markdown, display
from generator_config import SYSTEM_PROMPT, CURRICULUM_LIST, QUESTIONS_TO_GENERATE

def load_llama_model(model_path: str) -> Llama:
    """
    Mounts Google Drive and loads the Llama model.

    Args:
        model_path: The full path to the GGUF model file on Google Drive.

    Returns:
        An instance of the Llama model, or None if loading fails.
    """
    try:
        drive.mount('/content/drive')
        llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_gpu_layers=-1,
            verbose=False
        )
        print("✅ Model loaded successfully.")
        return llm
    except Exception as e:
        print(f"❌ Error loading the model: {e}")
        return None

def generate_math_question(llm: Llama, base_question_data: dict) -> str:
    """
    Generates a new math question using the local LLM based on an example.

    Args:
        llm: An instance of the loaded Llama model.
        base_question_data: A dictionary containing all example question details.

    Returns:
        A string containing the generated question text, or an error message.
    """
    prompt = f"""
[INST]
{SYSTEM_PROMPT}
---
{CURRICULUM_LIST}
---
Example Question:
@title {base_question_data['title']}
@question {base_question_data['question_text']}
@instruction {base_question_data['instruction']}
@difficulty {base_question_data['difficulty']}
@Order {base_question_data['order']}
{base_question_data['options']}
---
Now, generate a new question similar to the example. {base_question_data['new_question_prompt']}
[/INST]
"""
    print(f"🔄 Generating new question based on: {base_question_data['title']}...")

    try:
        response = llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=512,
        )
        generated_text = response['choices'][0]['message']['content']
        cleaned_text = generated_text.replace("imes", "\\times").replace("\t", "").strip()
        return cleaned_text
    except Exception as e:
        print(f"❌ An error occurred during generation: {e}")
        return "Error generating question."

if __name__ == "__main__":
    MODEL_PATH = "/content/drive/MyDrive/Llama_CPP_Models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

    llm_instance = load_llama_model(MODEL_PATH)

    if llm_instance:
        for i, q_data in enumerate(QUESTIONS_TO_GENERATE, start=1):
            generated_question = generate_math_question(llm_instance, q_data)

            print(f"\nFinal Generated Question {i}:")
            print("--------------------------------------")
            display(Markdown(generated_question))
            print("--------------------------------------")

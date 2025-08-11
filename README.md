# llama-math-question-generator
# Llama Math Question Generator

This project uses a local LLM (Mistral 7B) running via `llama-cpp-python` to generate new multiple-choice math questions based on provided examples. The script is designed to run in a Google Colab environment, leveraging its free GPU resources for faster inference.

## Features

- **Dynamic Question Generation**: Creates new math problems by altering the context and numbers of a base question.
- **Structured Output**: Generates questions in a specific, tag-based format (`@title`, `@question`, etc.) for easy parsing.
- **Curriculum Alignment**: Ensures generated questions are categorized according to a predefined curriculum hierarchy.
- **LaTeX Support**: Preserves mathematical notation in LaTeX format.
- **Scalable Design**: Easily add new base questions to the `generator_config.py` file to expand the question bank.

## Prerequisites

- A Google Colab environment.
- A Google Drive account with a fine-tuned GGUF model (e.g., `mistral-7b-instruct-v0.2.Q4_K_M.gguf`) stored in a specific directory.

## Installation

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/your-username/llama-math-question-generator.git](https://github.com/your-username/llama-math-question-generator.git)
    cd llama-math-question-generator
    ```

2.  **Install Dependencies**:
    Open the `main.py` file in Google Colab. The notebook environment will handle the mounting of Google Drive. Install the required packages by running the following cell:
    ```python
    !pip install -r requirements.txt
    ```

## Usage

1.  **Place the Model**: Ensure your GGUF model file is located at the path specified in `main.py`: `/content/drive/MyDrive/Llama_CPP_Models/mistral-7b-instruct-v0.2.Q4_K_M.gguf`

2.  **Run the Script**:
    The script is designed to be run directly. Simply execute all cells in the Colab notebook. The output for each generated question will be displayed in Markdown format.

3.  **Customize Questions**:
    To generate new questions, modify the `QUESTIONS_TO_GENERATE` list in `generator_config.py`. Add a new dictionary for each desired question, following the existing format.

## Example Output

The script will generate output that looks like this:

# Executive Llama

![Python](https://img.shields.io/badge/Python-%2320232a.svg?style=for-the-badge&logo=python)
![Llama 2](https://img.shields.io/badge/Llama_2-%2320232a.svg?style=for-the-badge&logo=meta)

### Work in Progress!

## About

Executive Llama is a basic chatbot that is built upon Llama 2 utilizing Ollama

It can be interacted with via text or voice fully offline

## Installation

### Requirements

- Python 3.8+
- Llama 2:13B via [Ollama](https://ollama.ai/)
- [LangChain](https://pypi.org/project/langchain/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [PyTTSx3](https://pypi.org/project/pyttsx3/)
- [Vosk](https://pypi.org/project/vosk/)

### Setup

1. Clone the repository

```bash
git clone https://github.com/jordanjanakievski/executive_llama.git
```

2. Install the requirements

```bash
pip3 install -r requirements.txt
```

3. Be sure Ollama is running in the background

```bash
ollama run llama2:13b
```

4. Run the program

```bash
python3 main.py
```

## Commands

### Text

- `/help` - Displays the help message
- `/bye` - Exits the program

### Keywords

- `write` - Stores the output of the model in a text file
    - `email` - Stores the file in `docs/emails/`
    - `prepare` - Stores the file in `docs/prep/`
    - `research` - Stores the file in `docs/research/`

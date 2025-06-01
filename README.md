# Alita - Gemini CLI Assistant

## Overview

**Alita** is a lightweight, command-line AI assistant powered by Google's Gemini model.
It enables natural, contextual conversations directly from your terminal and maintains session memory for coherent dialogue.

---

## Features

* AI responses powered by Google Gemini API (`gemini-1.5-flash`)
* Session memory for contextual conversations
* Minimal dependencies and clean architecture
* Customizable system prompt
* CLI-based for maximum portability

---

## Installation Guide

### Clone the Repository

```bash
git clone https://github.com/Rnaveennithyakalyan/alita-cli-assistant.git
cd alita-cli-assistant
```

### Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

### Install Dependencies

```bash
pip install google-generativeai python-dotenv
```

### Configure API Key

Create a `.env` file in the project root directory and add your Gemini API key:

```
GEMINI_API_KEY=your-google-gemini-api-key
```

---

## Running Alita

```bash
python main.py
```

The assistant will start with:

```
Alita here (type 'exit' to quit)
you :
```

Type your messages to begin the conversation.

---

## Project Structure

```
alita-cli-assistant/
├── main.py              # Main interaction loop and logic
├── .env                 # Environment file with API key
└── utils/
    └── prompts.py       # Defines the system prompt for Gemini
```

---

## Prompt Customization

To change Alita’s tone or behavior, edit the `utils/prompts.py` file:

```python
INITIAL_PROMPT = "You are Alita, a helpful and friendly AI assistant."
```

---

## Future Enhancements

* Persistent memory across sessions using file or database storage
* Voice input and output integration (text-to-speech and speech-to-text)
* Support for personality profiles and conversation modes

---

## License

This project is licensed under the MIT License.

---

## Contact

GitHub: [https://github.com/Rnaveennithyakalyan](https://github.com/Rnaveennithyakalyan)
Email: [naveennithyakalyan@gmail.com](mailto:naveennithyakalyan@gmail.com)

---

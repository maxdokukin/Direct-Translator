
# Direct Translator

## Overview
**Direct Translator** is a Flask-based web application designed to take Russian text input and translate it into English through a word-by-word lookup. This approach ignores grammar and context entirely, resulting in humorous and often nonsensical translations — capturing the charm and awkwardness of literal translations made by language learners.

## Features
- Simple web interface with a text input box and "Translate" button.
- Word-by-word Russian to English translation using a dictionary.
- Randomized selection when multiple translations exist for a word.
- Basic CSS for layout and presentation.

## Technology Stack
- **Language:** Python
- **Framework:** Flask
- **Development Environment:** PyCharm
- **Other Tools:** Russian-English Dictionary Source (en.openrussian.org)

## How It Works
1. User inputs Russian text into a text box.
2. Application splits the text into individual words.
3. Each word is looked up in the Russian-English dictionary.
4. If multiple translations exist, one is selected at random.
5. The translated English text is displayed on the page.

## Example
### Input (Russian)
Привет, меня зовут Макс, и я учусь в университете Сан-Хосе.

### Output (English)
Hello, myself called Max, and I learn in university Dignity Cosay.

## Installation
1. Clone the repository (private repo link: [Direct Translator](https://github.com/maxdokukin/Direct-Translator))
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On Mac/Linux:
        ```bash
        source venv/bin/activate
        ```
4. Install dependencies:
    ```bash
    pip install Flask pandas
    ```
5. Run the Flask application:
    ```bash
    python app.py
    ```
6. Access the application at `http://localhost:5000`.

## Notes
- This project does not use machine learning or advanced NLP techniques — it relies entirely on simple dictionary lookups and random word selection.
- Intended for entertainment purposes and to demonstrate the quirks of literal translation.

## Author
Max Dokukin

from flask import Flask, render_template, request
import re
import random
import pandas as pd
app = Flask(__name__)

df = pd.read_csv("data/dictionary.csv")

# Mock translation function
import random
import re
import string

TRANSLITERATION_MAP = {
    # Lowercase
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',

    # Uppercase
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
    'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
    'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
}


def transliterate(word):
    """Fallback function to transliterate a word letter by letter."""
    return ''.join(TRANSLITERATION_MAP.get(char, char) for char in word)


def translate_text(input_text):
    # Merge all DataFrames
    print(f"Translating: {input_text}")
    output = []

    for word in input_text.split(" "):
        # Preserve punctuation and capitalization
        stripped_word = word.strip(string.punctuation)
        punctuation = word[len(stripped_word):] if stripped_word else word  # Preserve trailing punctuation

        # Check if the word exists in lowercase, capitalized, or as-is
        possible_forms = [
            stripped_word,
            stripped_word.lower(),
            stripped_word.capitalize()
        ]
        translation = df.loc[df['ru'].isin(possible_forms), 'en']

        print(f"Translating word: {word} (stripped: {stripped_word})")
        print(word, translation)

        if not translation.empty:
            # Convert translation series to a list
            translation_list = translation.tolist()
            print("translation_list", translation_list)

            # Randomly select a translation
            selected_translation = random.choice(translation_list)

            # Process for cases with multiple options (separated by ";" or ",")
            if ";" in selected_translation:
                selected_translation = selected_translation.split(";")[0].strip()
            if "," in selected_translation:
                selected_translation = selected_translation.split(",")[0].strip()

            # Remove anything in parentheses, if necessary
            result = re.sub(r"\s*\(.*?\)", "", selected_translation).strip()

            # Reapply original capitalization
            if stripped_word.istitle():  # Title case
                result = result.capitalize()
            elif stripped_word.isupper():  # Uppercase
                result = result.upper()

            # Add back the punctuation
            print(f"Selected translation: {result}")
            output.append(result + punctuation)
        else:
            # Handle case where no translation is found
            print(f"No translation found for: {word}")
            transliterated = transliterate(stripped_word)  # Fallback transliteration
            print(f"Transliterated: {transliterated}")

            # Reapply original capitalization
            if stripped_word.istitle():  # Title case
                transliterated = transliterated.capitalize()
            elif stripped_word.isupper():  # Uppercase
                transliterated = transliterated.upper()

            # Add back the punctuation
            output.append(transliterated + punctuation)

    return " ".join(output)


@app.route("/", methods=["GET", "POST"])
def home():
    translation = ""
    input_text = ""  # Initialize input_text to preserve its value

    if request.method == "POST":
        input_text = request.form["input_text"]  # Get input from the form
        translation = translate_text(input_text)  # Call translation function

    # Pass input_text and translation to the template
    return render_template("index.html", translation=translation, input_text=input_text)


if __name__ == "__main__":
    app.run(debug=True)

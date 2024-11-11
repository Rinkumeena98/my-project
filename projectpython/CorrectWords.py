import streamlit as st
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word:
                corrected_words.append(f'correcting "{word}" to "{corrected_word}"')
            else:
                corrected_words.append(word)

        return ' '.join(corrected_words)

    def run(self):
        st.title("Spell Checker App")
        st.write("Enter text to check for spelling errors. The corrected words will be shown.")

        text_input = st.text_area("Enter text to check", "")

        if st.button("Check Spelling"):
            if text_input:
                corrected_text = self.correct_text(text_input)
                st.subheader("Corrected Text:")
                st.write(corrected_text)
            else:
                st.warning("Please enter some text to check.")


if __name__ == "__main__":
    app = SpellCheckerApp()
    app.run()

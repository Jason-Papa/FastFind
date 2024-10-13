from googletrans import Translator

def translate_text(text, target_lang='en', source_lang=None):
    # Initialize the Translator object
    translator = Translator()
    
    try:
        # If source language is not provided, auto-detect the language
        if source_lang:
            translation = translator.translate(text, src=source_lang, dest=target_lang)
        else:
            # Auto-detect the source language
            print(f"Detected language: {translation.src if not source_lang else source_lang}")
            translation = translator.translate(text, dest=target_lang)
        
        # Print the detected language and translated text
        print(f"Translated text: {translation.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

from googletrans import Translator

translator = Translator()

def translate(text):
    return translator.translate(text, dest='pt', src='en').text
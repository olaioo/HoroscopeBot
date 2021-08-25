from googletrans import Translator

translator = Translator(service_urls=['translate.googleapis.com'])

def translate(text):
    return translator.translate(text, dest='pt', src='en').text
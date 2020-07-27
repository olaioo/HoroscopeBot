import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

TRANSLATOR_TOKEN = os.environ.get('WATSON_TRANSLATOR_TOKEN')
TRANSLATOR_URL = os.environ.get('WATSON_TRANSLATOR_URL')

authenticator = IAMAuthenticator(TRANSLATOR_TOKEN)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(TRANSLATOR_URL)

def translate(text):
    return language_translator.translate(text=text, model_id='pt-en').get_result()['translations'][0]['translation']

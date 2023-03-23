"""
Translates text from English -> French and French -> English
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2023-03-23',authenticator=authenticator)
language_translator.set_service_url(url)



def english_to_french(english_text):
    """
    Takes a string arugment and translate string from English To French
    """
    if english_text == '':
        return 'Input cannot be an empty string'
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    #print(json.dumps(french_text, indent=2))
    return french_text['translations'][0]['translation']



def french_to_english(french_text):
    """
    Takes a string argument and translate string from French to English
    """
    if french_text == '':
        return 'Input cannot be an empty string'
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    #print(json.dumps(english_text, indent=2))
    return english_text['translations'][0]['translation']

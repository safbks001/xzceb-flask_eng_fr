import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('zFQ6xmP8Nr-Fh5k7GPFEH77f4Ffi0sEi6lxejDR0rgzO')
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/3f980740-06bd-486d-9152-e9c60d67ec62')

def english_to_french(english_text):
    translation = lt.translate(text = english_text , model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation = lt.translate(text =  french_text , model_id = 'fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
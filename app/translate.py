import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if app.config['MS_TRANSLATOR_KEY'] is not None:
        return microsoft_translate(text, source_language, dest_language)
    else:
        return google_translate(text, source_language, dest_language)

def microsoft_translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
        not app.config['MS_TRANSLATOR_KEY']:
        app.logger.error('The Microsoft translation service is not configured.')
        return _('Error: the translation service is not configured.')
    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'westus',
    }
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com'
        '/translate?api-version=3.0&from={}&to={}'.format(
            source_language, dest_language), headers=auth, json=[{'Text': text}])
    if r.status_code != 200:
        app.logger.error('Error: the Microsoft translation service failed.')
        return _('Error: the translation service failed.')
    return r.json()[0]['translations'][0]['text']

def google_translate(text, source_language, dest_language):
    if 'GOOGLE_TRANSLATOR_KEY' not in app.config or \
        not app.config['GOOGLE_TRANSLATOR_KEY']:
        app.logger.error('The Google translation service is not configured.')
        return _('Error: the translation service is not configured.')
    r = requests.post(
        url='https://translation.googleapis.com/language/translate/v2',
        params={
            "target": dest_language,
            "source": source_language,
            "format": "text",
            "key": app.config['GOOGLE_TRANSLATOR_KEY'],
            "q": text
        }
    )
    if r.status_code != 200:
        app.logger.error('The Google translation service failed.')
        return _('Error: the translation service failed.')
    return r.json()['data']['translations'][0]['translatedText']
from googletrans import LANGUAGES
from google.cloud import translate_v2 as translate




def getLanguageList():
    languageCodes = dict(map(reversed, LANGUAGES.items()))
    return languageCodes

def translate_text(text, target):

    translate_client = translate.Client()

    

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    return result["translatedText"]

print(translate_text("hello", "fr"))

# print(list(getLanguageList().keys()))



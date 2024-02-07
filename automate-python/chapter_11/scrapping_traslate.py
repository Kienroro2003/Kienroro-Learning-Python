from googletrans import Translator


def translate_word(wordEnlish):
    translator = Translator()
    translation = translator.translate(wordEnlish, src='en', dest='vi')
    return translation.text




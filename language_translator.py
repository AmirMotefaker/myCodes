# Code by AmirMotefaker

# Language Translator Using Google API

# import googletrans
 
# print(googletrans.LANGUAGES)

# from googletrans import Translator

# translator = Translator()

# result = translator.translate('ich liebe dich')

# print(result.src)
# print(result.dest)
# print(result.origin)
# print(result.text)
# print(result.pronunciation)


# Specifying Source and Destination Languages

from googletrans import Translator

translator = Translator()
result = translator.translate('ich liebe dich', src='de', dest='fr')

print(result.src)
print(result.dest)
print(result.text)


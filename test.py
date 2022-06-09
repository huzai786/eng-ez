from packages.utils import get_definations, get_words
from packages.api_data import get_definations
import requests


# x, y, z = get_definations('antiquate')
# print(x, y, sep='\n\n')


res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/accession')
print(res.json())
print(type(res.json()))
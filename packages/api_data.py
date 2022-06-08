import requests
import pprint

def get_example(x):
    if x.get('example'):
        return True
    else:
        return False

def definations(word):
    res = requests.get(
        f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    link_url = res.json()[0].get('sourceUrls')
    meanings = res.json()[0].get('meanings')
    partOfSpeech = meanings[0].get('partOfSpeech')
    all_definations = []
    for i in meanings:
        single_def = i.get('definitions')
        for define in single_def:
            defination = {}
            if define.get('definition'):
                defination['Defination'] = define.get('definition')
            if define.get('antonyms'):
                defination['antonyms'] = define.get('antonyms')
            if define.get('synonyms'):
                defination['synonyms'] = define.get('synonyms')
            if define.get('example'):
                defination['Examples'] = define.get('example')
            all_definations.append(defination)
    if len(all_definations) > 4:
        sorted(all_definations, key=get_example)
    return all_definations, link_url


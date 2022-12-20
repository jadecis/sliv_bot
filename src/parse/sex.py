import pymorphy2
import emoji

def sex_fromgender(text):
    name=emoji.replace_emoji(text, "")
    name=name.strip()
    if len(name.split()) > 1:
        name= name.split()[0]
    morph = pymorphy2.MorphAnalyzer()
    result= morph.parse(name)[0]
    if result.tag.gender == 'masc':
        return 'm'
    elif result.tag.gender == 'femn':
        return 'w'
    elif result.tag.gender == None:
        return None
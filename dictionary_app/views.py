from django.shortcuts import render
from pydictionary import Dictionary

def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = Dictionary(search)
    
    try:
        meaning = dictionary.meanings()[0]
    except:
        context = {
            'error': 'Invalid input. please try again.'
        }
        return render(request, 'word.html', context=context)
        
    synonyms = dictionary.synonyms()
    antonyms = dictionary.antonyms()
    print(antonyms)
    context = {
        'meaning': meaning,
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    
    return render(request, 'word.html', context=context)
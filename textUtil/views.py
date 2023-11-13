#Created by xort


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def analyze(request):
    #get the text
    djText = request.GET.get('text', 'default')
    
    print(djText)
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    #remove punctuation
    
    punctuations = '''!"#$%&'()*+,- ./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    if(removepunc == "on"):
        for char in djText:
            if(char not in punctuations):
                analyzed += char
    else:
        return HttpResponse("errore")
    params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
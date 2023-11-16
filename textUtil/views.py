#Created by xort
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def analyze(request):
    # Get the text
    djText = request.GET.get('text', 'default')
    
    # Check box value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newLineRemover = request.GET.get('newLineRemover', 'off')
    extraSpaceRemover = request.GET.get('extraSpaceRemover', 'off')    
    
    punctuations = '''!"#$%&'()*+,- ./:;<=>?@[\]^_`{|}~'''
    if(removepunc == "on"):
        analyzed = ""
        for char in djText:
            if(char not in punctuations):
                analyzed += char
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djText:
            analyzed += char.upper()
        params = {'purpose' : 'Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newLineRemover == "on"):
        analyzed = ""
        for char in djText:
            if(char != "\n"):
                analyzed += char
        params = {'purpose' : 'New line removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(extraSpaceRemover == "on"):
        analyzed = ""
        for index, char in enumerate(djText):
            if(not(djText[index] == " " and djText[index + 1] == " ")):
                analyzed += char
        params = {'purpose' : 'Extra Space removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("errore")
    
    
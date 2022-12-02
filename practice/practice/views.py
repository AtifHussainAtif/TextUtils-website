from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')
    
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed = ''
         for char in djtext:
            if char not in punctuations:
                analyzed = analyzed +char

         params = {'purpose' : 'Remove Punctuation', 'analyzed_text' : analyzed}
         return render(request, 'analyze2.html', params)

         
    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose' : 'UPPERCASE', 'analyzed_text' : analyzed}
        djtext = analyzed

    if(charcount =='on'):
        analyzed = len(djtext)
        params = {'purpose' : 'Character Count', 'analyzed_text' : analyzed}
        djtext = analyzed

    if(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
               analyzed = analyzed + char
        params = {'purpose' : 'extra space remover', 'analyzed_text' : analyzed}
        djtext = analyzed

    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n"and char!="\r":
                analyzed = analyzed + char

        params = {'purpose' : 'New Line Remover', 'analyzed_text' : analyzed}
        djtext = analyzed
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze2.html', params)

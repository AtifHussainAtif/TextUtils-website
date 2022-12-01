from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')

def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))
    
def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover= request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    if removepunc == "on":
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed = ''
         for char in djtext:
            if char not in punctuations:
                analyzed = analyzed +char

         params = {'purpose' : 'Remove Punctuation', 'analyzed_text' : analyzed}
         return render(request, 'analyze2.html', params)

         
    elif(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose' : 'UPPERCASE', 'analyzed_text' : analyzed}
        return render(request, 'analyze2.html', params)

    elif(charcount =='on'):
        analyzed = len(djtext)
        
        

        params = {'purpose' : 'Character Count', 'analyzed_text' : analyzed}
        return render(request, 'analyze2.html', params)

    elif(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
               analyzed = analyzed + char

        params = {'purpose' : 'extra space remover', 'analyzed_text' : analyzed}
        return render(request, 'analyze2.html', params)

    elif(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose' : 'New Line Remover', 'analyzed_text' : analyzed}
        return render(request, 'analyze2.html', params)



    else:
        return HttpResponse("Error 404")

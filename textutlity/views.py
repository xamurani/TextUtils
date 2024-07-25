from django.http import HttpResponse
from django.shortcuts import render
import os


def index(request):
    return render(request, 'index.html')

# Analyze the text
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    analyzed = djtext

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        prev_char = None
        for char in djtext:
            if not (prev_char == " " and char == " "):
                analyzed += char
            prev_char = char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = len([ele for ele in djtext if ele.isalpha()])
        params = {'purpose': 'Character Counted', 'analyzed_text': analyzed}

    if (
            removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcount != "on"):
        return HttpResponse("please select any operation and try again")


    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

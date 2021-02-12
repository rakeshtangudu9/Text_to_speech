from django.shortcuts import render
import pyttsx3
# Create your views here.


def index(request):
    return render(request, 'index.html')


def result(request):
    text = request.POST.get('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

    return render(request, 'result.html')

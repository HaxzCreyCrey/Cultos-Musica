from django.shortcuts import render

def musicas(request):
    return render(request,'index.html')

from django.shortcuts import render

def pageHome(request):
    return render(request, 'pageHome.html')


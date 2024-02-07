from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def homePage(request):
     return render(request, 'base/requests.html')

def bookTractor(request):
     return render(request, 'base/book-tractor.html')
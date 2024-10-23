from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

# Uma view do Django eh um ooobjeto chamavel que recebe um http request e retorna um http response

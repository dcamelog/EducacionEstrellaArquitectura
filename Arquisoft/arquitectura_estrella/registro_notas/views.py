import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'interfaz_carga.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile=request.FiLES['myfile']
        fs = FileSystemStorage()
        filename= fs.save(myfile.name, myfile)
        uploades_file_url =fs.url(filename)
        return render(request, 'app/index.html', {
            'uploaded_file_url':uploaded_file_url
        })
    return render(request,'interfaz_carga.html')
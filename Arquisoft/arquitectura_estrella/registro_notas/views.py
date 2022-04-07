import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings



def index(request):
    return render(request, 'interfaz_carga.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs = FileSystemStorage()
        filename= fs.save(myfile.name, myfile)
        uploaded_file_url =fs.url(filename)
        return render(request, 'interfaz_carga.html', {
            'uploaded_file_url':uploaded_file_url
        })
        
    return render(request,'interfaz_carga.html')
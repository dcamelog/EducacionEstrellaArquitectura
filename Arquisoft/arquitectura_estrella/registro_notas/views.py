import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
    

def index(request):
    return render(request, 'interfaz_carga.html')


@login_required
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


def logout(request):
    django_logout(request)
    domain = 'dev-ot3xuai3.us.auth0.com'
    client_id = '9Oh3BSY7ro9hyyuD8FvKCSPnymUd91Hn'
    return_to = 'http://52.201.214.34:8000/registro_notas' 
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

def hand_crafted_redirect(request):
  response = HttpResponse(status=500)
  response['Location'] = '/redirect/fail/'
  return response

def redirect(request):
    return redirect('/redirect/fail/')

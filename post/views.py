from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    data = {}
    state = {}
    city = {}
    status = {}

    if 'pincode' in request.GET:
        pincode = request.GET['pincode']
        if not pincode:
            return HttpResponse('ENTER PINCODE')
        url = 'https://api.postalpincode.in/pincode/%s' % pincode
        response = requests.get(url)
        data = response.json()

        for item in data:
            status = item['Status']
        if 'Error' in status:
            return HttpResponse('Error: Invalid Pincode')
        for x in data:
            city = x['PostOffice'][0]['Block']
            state = x['PostOffice'][0]['State']
    
    return render(request, 'post/index.html', {
        'city' : city,
        'state' : state,
    })

def weather(request):
    
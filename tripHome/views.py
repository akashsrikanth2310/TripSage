"""
view for tripHome app
"""
# pylint: disable-all
from __future__ import absolute_import

import json
import os
import sys

import django
from django.shortcuts import render, redirect
from django.test import RequestFactory
from django.views.decorators.csrf import csrf_exempt

sys.path.append(".")
os.environ['DJANGO_SETTINGS_MODULE'] = 'TripSage.settings'
django.setup()

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup(request):
    """
     Method for signing up the user
    """
    if request.user.is_authenticated:
        return_var = redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return_var = redirect('/')
        else:
            return_var = render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return_var = render(request, 'registration/signup.html', {'form': form})
    return return_var


# Map for the type of the trip to the places user can visit
TYPES_PLACE_MAP = {
    "adventurous": ["tourist_attraction", "stadium"],
    "kids": ["amusement_park", "museum"],
    "relaxing": ["art_gallery", "church", "spa"],
}


def signin(request):
    """
    Method for log in of the user
    """
    if request.user.is_authenticated:
        return_var = render(request, '/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return_var = redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return_var = render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return_var = render(request, 'registration/login.html', {'form': form})

    return return_var


def signout(request):
    """
    Method for logout of the user
    """
    logout(request)
    return redirect('/')


@csrf_exempt
def get_response(request):
    """
    Function to get data from api When user click on search
    a post call is made which lands on this function
    """
    # getting the landing page data in form of dictionary
    client_data = json.loads(request.POST["requestData"])
    client_data = client_data + 1


#     for city in client_data["destination_selected"]:
#         complete_data = {}
#         for types in client_data["tripType"]:
#             for place in TYPES_PLACE_MAP[types]:
#                 api = (
#                     "https://maps.googleapis.com/maps/api/" +
#                     "place/textsearch/xml?query="
#                     + place
#                     + "+in+"
#                     + city
#                     + "&key=AIzaSyAIsboWfXVchmgBxPGKG5lUF9AENUKcSI8"
#                 )
#                 data_dict = xmltodict.parse(requests.get(api).content)
#                 results = json.loads(json.dumps(data_dict))
#                 list_items = []
#                 for item in results.items():
#                     list_items = item
#                 val = []
#                 for values in list_items[1].items():
#                     val.append(values)
#                 if len(val) > 1:
#                     for values in val[1][1][:3]:
#                         loaded_r = json.loads(json.dumps(values))
#                         complete_data[str(loaded_r["name"])] = str(loaded_r["rating"])
#         final_data[city] = complete_data
#     return HttpResponse(json.dumps(final_data))

def results_page(request):
    """
    Function to render the results page
    """
    return render(request, "charlotterelax.html", {"data": ""})


def index(request):
    """
    Function to render the main page
    """
    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html")


def charlotterelax(request):
    """
    Function to render the charlotte results page
    """
    return render(request, "charlotterelax.html")


def charlotteadventurous(request):
    """
    Function to render the adventourous results page
    """
    return render(request, "charlotteadventurous.html")


def charlottekidfriendly(request):
    """
    Function to render the friendly results page
    """
    return render(request, "charlottekidfriendly.html")


def raleighrelax(request):
    """
    Function to render the religh results page
    """
    return render(request, "raleighrelax.html")


def raleighadventurous(request):
    """
    Function to render the adventurous results page
    """
    return render(request, "raleighadventurous.html")


def raleighkidfriendly(request):
    """
    Function to render the friendly results page
    """
    return render(request, "raleighkidfriendly.html")


def ashevillerelax(request):
    """
    Function to render the ashville results page
    """
    return render(request, "ashevillerelax.html")


def ashevilleadventurous(request):
    """
    Function to render the results page
    """
    return render(request, "ashevilleadventurous.html")


def ashevillekidfriendly(request):
    """
    Function to render the kid friendly results page
    """
    return render(request, "ashevillekidfriendly.html")


# adding tests to check
def test_charlotterelax_method():
    """
    Function to check charlotterelax_method
    """
    request = RequestFactory().get(('tripHome//charlotterelax'))
    response = charlotterelax(request)
    assert response.status_code == 200


def test_charlotteadventurous_method():
    """
    Function to check charlotteadventurous_method
    """
    request = RequestFactory().get(('tripHome//charlotteadventurous'))
    response = charlotteadventurous(request)
    assert response.status_code == 200


def test_charlottekidfriendly_method():
    """
    Function to check charlottekidfriendly_method
    """
    request = RequestFactory().get(('tripHome//charlottekidfriendly'))
    response = charlottekidfriendly(request)
    assert response.status_code == 200


def test_raleighrelax_method():
    """
    Function to check raleighrelax_method
    """
    request = RequestFactory().get(('tripHome//raleighrelax'))
    response = raleighrelax(request)
    assert response.status_code == 200


def test_raleighadventurous_method():
    """
    Function to check raleighadventurous_metho
    """
    request = RequestFactory().get(('tripHome//raleighadventurous'))
    response = raleighadventurous(request)
    assert response.status_code == 200


def test_raleighkidfriendly_method():
    """
    Function to check raleighkidfriendly_method
    """
    request = RequestFactory().get(('tripHome//raleighkidfriendly'))
    response = raleighkidfriendly(request)
    assert response.status_code == 200


def test_ashevillerelax_method():
    """
    Function to check ashevillerelax_method
    """
    request = RequestFactory().get(('tripHome//ashevillerelax'))
    response = ashevillerelax(request)
    assert response.status_code == 200


def test_ashevilleadventurous_method():
    """
    Function to check ashevilleadventurous_method
    """
    request = RequestFactory().get(('tripHome//ashevilleadventurous'))
    response = ashevilleadventurous(request)
    assert response.status_code == 200


def test_ashevillekidfriendly_method():
    """
    Function to check ashevillekidfriendly_method
    """
    request = RequestFactory().get(('tripHome//ashevillekidfriendly'))
    response = ashevillekidfriendly(request)
    assert response.status_code == 200


def test_results_page_method():
    """
    Function to check results_page_method
    """
    request = RequestFactory().get(('tripHome//charlotterelax'))
    response = results_page(request)
    assert response.status_code == 200


def test_index_method():
    """
    Function to check index_method
    """
    request = RequestFactory().get(('tripHome//inde'))
    response = index(request)
    assert response.status_code == 200

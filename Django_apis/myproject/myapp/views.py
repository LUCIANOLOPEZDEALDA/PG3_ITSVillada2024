# myapp/views.py

import requests
from django.shortcuts import render

def brewery_list(request):
    # Obtener parámetros de búsqueda
    search_query = request.GET.get('search', '')
    quantity = request.GET.get('quantity', '')

    # Preparar parámetros para la API
    params = {}
    if search_query:
        params['by_name'] = search_query
    if quantity:
        params['per_page'] = quantity

    # Realizar la solicitud a la API con los parámetros de búsqueda
    response = requests.get('https://api.openbrewerydb.org/breweries', params=params)
    breweries = response.json()

    # Obtener parámetros de selección de columnas
    show_city = 'city' in request.GET
    show_type = 'type' in request.GET
    show_state = 'state' in request.GET

    return render(request, 'myapp/brewery_list.html', {'breweries': breweries, 'search_query': search_query,
                                                        'quantity': quantity, 'show_city': show_city,
                                                        'show_type': show_type, 'show_state': show_state})

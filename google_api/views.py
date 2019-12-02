from django.shortcuts import render
from django.http import JsonResponse
import requests, json


# Create your views here.

def search(request, keyword):
        link = "https://www.googleapis.com/books/v1/volumes?q=" + keyword
        data = requests.get(link).json()
        totalItems = data['totalItems']

        for item in data['items']:
            if 'imageLinks' not in item['volumeInfo']:
                item['volumeInfo']['imageLinks'] = {}
                item['volumeInfo']['imageLinks']['smallThumbnail'] = "https://www.iconspng.com/images/icon-book/icon-book.jpg"
                item['volumeInfo']['imageLinks']['thumbnail'] = "https://www.iconspng.com/images/icon-book/icon-book.jpg"

        return JsonResponse({'data':data})
    
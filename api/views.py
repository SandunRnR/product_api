from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list',
        'Detail view': '/product-detail/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-detail/<int:id>',
    }

    return Response(api_urls)
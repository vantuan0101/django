from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get (seft , request , *args , **kwargs):
        data = {
            'username' : 'admin',
            'year_active' : 2019,
        }
        return Response(data)
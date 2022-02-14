from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, LogSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from time import time
from .models import Logs
import datetime
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

class AllUserView(APIView):
    def get(self, request):
        try: 
            user_obj = User.objects.all()
            print(user_obj, '*******************')
            user_serializer = UserSerializer(user_obj, many=True)
            return JsonResponse(user_serializer.data, safe=False)
        except User.DoesNotExist: 
            return JsonResponse({'message': 'The user data does not exist'}, safe=False) 

class UserView(APIView):

    def get(self, request, id):
        try:
            start_time = datetime.datetime.now()
            print(start_time)
            user_obj = User.objects.get(id=id)
            user_serializer = UserSerializer(user_obj)
            end_time = datetime.datetime.now()
            print(end_time)
            log = Logs(request_type='Get', request_body=id, request_time=str(start_time),response=user_serializer.data, response_time=str(end_time))
            log.save()
            return JsonResponse(user_serializer.data, safe=False)
        except User.DoesNotExist: 
            return JsonResponse({'message': 'The user data does not exist'}, safe=False) 

    def post(self, request, *args, **kwargs):
        start_time = datetime.datetime.now()
        user_serializer = UserSerializer(data=request.data)
        json_data = json.dumps(request.data) 
        if user_serializer.is_valid():
            user_serializer.save()
            end_time = datetime.datetime.now()
            log = Logs(request_type='Post', request_body=json_data, request_time=str(start_time),response=user_serializer.data, response_time=str(end_time))
            log.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            end_time = datetime.datetime.now()
            log = Logs(request_type='Post', request_body=json_data, request_time=str(start_time),response={'message': 'The user does not exist'}, response_time=str(end_time))
            log.save()
            return JsonResponse(user_serializer.errors, safe=False) 

    def put(self, request, id):
        start_time = datetime.datetime.now()
        user = User.objects.get(id=id) 
        user_serializer = UserSerializer(user, data=request.data) 
        json_data = json.dumps(request.data)
        if user_serializer.is_valid(): 
            user_serializer.save() 
            end_time = datetime.datetime.now()
            log = Logs(request_type='Put', request_body=json_data, request_time=str(start_time),response=user_serializer.data, response_time=str(end_time))
            log.save()
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, safe=False) 

    def delete(self, request, id):
        try:
            start_time = datetime.datetime.now()
            json_data = json.dumps(id)
            user = User.objects.get(id=id)
            user.delete() 
            # return JsonResponse({'message': 'User deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            end_time = datetime.datetime.now()
            log = Logs(request_type='Delete', request_body=json_data, request_time=str(start_time),response={'message': 'User deleted successfully!'}, response_time=str(end_time))
            log.save()
            return JsonResponse({'message': 'User deleted successfully!'}, safe=False)
        except User.DoesNotExist: 
            end_time = datetime.datetime.now()
            log = Logs(request_type='Delete', request_body=json_data, request_time=str(start_time),response={'message': 'The user does not exist'}, response_time=str(end_time))
            log.save()
            return JsonResponse({'message': 'The user does not exist'}, safe=False) 


class logView(APIView):
    def get(self, request):
        try: 
            log_obj = Logs.objects.all()
            print(reversed(log_obj))
            # print(user_obj, '*******************')
            log_serializer = LogSerializer(log_obj, many=True)
            return JsonResponse(log_serializer.data, safe=False)
        except Logs.DoesNotExist: 
            return JsonResponse({'message': 'The log data does not exist'}, safe=False) 
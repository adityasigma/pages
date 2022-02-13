from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'index.html')

class AllUserView(APIView):
    def get(self, request):
        try: 
            user_obj = User.objects.all()
            user_serializer = UserSerializer(user_obj, many=True)
            return JsonResponse(user_serializer.data, safe=False)
        except User.DoesNotExist: 
            return JsonResponse({'message': 'The user data does not exist'}, safe=False) 

class UserView(APIView):

    def get(self, request, id):
        try: 
            user_obj = User.objects.get(id=id)
            user_serializer = UserSerializer(user_obj)
            return JsonResponse(user_serializer.data, safe=False)
        except User.DoesNotExist: 
            return JsonResponse({'message': 'The user data does not exist'}, safe=False) 

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(user_serializer.errors, safe=False) 

    def put(self, request, id):
        user = User.objects.get(id=id) 
        user_serializer = UserSerializer(user, data=request.data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, safe=False) 

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete() 
            # return JsonResponse({'message': 'User deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse({'message': 'User deleted successfully!'}, safe=False)
        except User.DoesNotExist: 
            return JsonResponse({'message': 'The user does not exist'}, safe=False) 
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from . import models
from rest_framework.views import APIView
from django.forms.models import model_to_dict
# Create your views here.
 

class BookList(APIView):
	def get(self, request):
		author = request.GET.get('author')
		if (author):
			return Response({'message':"this book was writen by the author : "+author},status=status.HTTP_200_OK)
		return Response({"message":"List of books"},status=status.HTTP_200_OK)
	def post(self, request):
		return Response({'message':'Creating a book'},status=status.HTTP_201_CREATED)

class Book(APIView):
	def get(self, request, pk):
		if (models.Book.objects.filter(pk=pk).exists()):
			book = models.Book.objects.get(pk=pk)
			return Response({
				'id':pk,
				'title':book.title,
				'author':book.author,
				'price':book.price
			},status=status.HTTP_200_OK)
		return Response({'message':"This book does not exist "},status=status.HTTP_200_OK)

class Books(viewsets.ViewSet):
	def create(self, request):
		return Response({"message":"Creating a book"},status.HTTP_201_CREATED)
	def update(self, request, pk=None):
		return Response({"message":"Updating a book"},status.HTTP_200_OK)
	def destroy(self, request, pk=None):
		return Response({"message":'Removing a book'},status.HTTP_200_OK)
	def partial_update(self, request, pk =None):
		return Response({'message':'Partially updating a book'},status.HTTP_200_OK)
	def retreive(self,request, pk =None):
		return Response({'message':'Displaying a book'},status.HTTP_200_OK)

class ReadBooks(viewsets.ReadOnlyModelViewSet):
	def list(self, request):
		books = models.Book.objects.all()
		author = request.GET.get('author')
		if author:
			return Response({'message':'Books of the author : '+author},status.HTTP_200_OK)
		return Response({"message":"All books"},status.HTTP_200_OK)


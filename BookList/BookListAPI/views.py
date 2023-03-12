from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets

# Create your views here.
class Book(viewsets.ViewSet):
	def books(self, request):
		return Response({"message":"All books"},status.HTTP_200_OK)
	def create(self, request):
		return Response({"message":"Creating a book"},status.HTTP_201_CREATED)
	def update(self, request):
		return Response({"message":"Updating a book"},status.HTTP_200_OK)
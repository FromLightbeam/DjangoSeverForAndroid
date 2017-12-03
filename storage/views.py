from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers

from storage.models import Product, Category


class CategoryView(View):
    def get(self, request):
        categoriesJSON = serializers.serialize("json", Category.objects.all())
        responce = HttpResponse(categoriesJSON, content_type="application/json")
        return responce


class ProductsView(View):
    def get(self, request):
        productsJSON = serializers.serialize("json", Product.objects.filter(category=request.GET['pk']))
        responce = HttpResponse(productsJSON, content_type="application/json")
        return responce


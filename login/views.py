from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class IndexClass(View):
	def get(self, *args, **kwargs):
		return HttpResponse("<h1>XinChao</h1>")
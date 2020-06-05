from django.shortcuts import render
from django.http import HttpResponse
from .form import PostForm, SendEmail

from django.views import View
# Create your views here.

class IndexClass(View):
	def get(self, request):
		return HttpResponse("Hello")

def index(request, *argc, **argv):
	return HttpResponse("Hello world!")
# class PostClass(View):
# 	def get(self, request, *argc, **argv):
# 		a= PostForm()
# 		return render(request, 'news/add_new.html',{'f':a})
class SaveClass(View):
	def post(self, request, *argc, **argv):
		g = PostForm(request.POST)
		if g.is_valid():
			g.save()
			return HttpResponse("save success")
		else:
			return HttpResponse("not valid")
	def get(self, request, *argc, **argv):
		a= PostForm()
		return render(request, 'news/add_new.html',{'f':a})
def email_view(request, *argc, **argv):
	b = SendEmail()
	return render(request, 'news/email.html',{'f':b})

def email_process(request, *argc, **argv):
	if request.method =="POST":
		m= SendEmail(request.POST)
		if m.is_valid():
			title = m.cleaned_data['title']
			cc=m.cleaned_data['cc']
			content=m.cleaned_data['content']
			email=m.cleaned_data['email']
			context = {'title': title, 'cc':cc, 'content':content, 'email':email}
			return render(request, 'news/print_email.html',context)
		return HttpResponse("not valid")
	else:
		return HttpResponse("not post request")
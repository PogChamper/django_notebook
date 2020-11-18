from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Message 
from .forms import MessageForm	
import datetime
# Create your views here.

def index(request):
	mess = Message.objects.order_by('-id')
	return render(request, 'chat/index.html', {'title': 'Записная книжка', 'mess': mess})


def create(request):
	error = ''
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'AAAAAAAAAAA'
	form = MessageForm()
	context = {'form': form, 'error': error}

	return render(request, 'chat/create.html', context)
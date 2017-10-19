# -*- coding: utf-8 -*-
from django.shortcuts import render
from board.models import Post
from django.core.paginator import Paginator

def home(request):

	post_list = Post.objects.all()

	paginator = Paginator(post_list, 1)

	return render(request, 'pages/home.html', {'posts' : post})

def single(request, single):
	single = Post.objects.get(id=single)
	context = {
		'post' : single, 
	}
	return render(request, 'pages/single.html', context)

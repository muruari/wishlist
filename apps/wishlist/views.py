from __future__ import unicode_literals
import bcrypt, time
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from datetime import datetime

def registration(request):
	return render(request, 'wishlist/registration.html')


def register(request):
    check = User.objects.validate(request.POST)
    if request.method != 'POST':
		return redirect('/')
    if len(check) > 0:
        for error in check:
            messages.add_message(request, messages.INFO, error, extra_tags="register")
            return redirect('/')

    passwd = request.POST['password']
    if len(check) == 0:
		hashed_pw = bcrypt.hashpw(str(passwd).encode(), bcrypt.gensalt())

    #Creates a new user in the database:
		user = User.objects.create(
			name = request.POST['name'],
			username = request.POST['username'],
			password = hashed_pw,
            date_hired =  request.POST['date_hired']
		)


    username = request.POST['username']
    user = User.objects.get(username = username) # THIS LINE results in JSON serializable error because I was capturing the ENTIRE user object into session.
    request.session['user_id'] = user.id
    request.session['username'] = username

    return redirect('/dashboard')


def login(request):
    if request.method != 'POST':
        return redirect('/')
    user = User.objects.filter(username = request.POST.get('username')).first()
    if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        return redirect('/dashboard')
    else: 
        messages.add_message(request, messages.INFO, 'Your credentials are invalid! Please try again.', extra_tags="login")
        return redirect('/')
    return redirect('/dashboard')

	

def logout(request):
		request.session.clear()
		return redirect('/')


def dashboard(request):
    user = User.objects.get(id = request.session["user_id"])
    my_wishlists = Wishlist.objects.exclude(wished_by = user)
    context = {
        "user" : user,
        "wishlist" : Wishlist.objects.filter(wished_by = user),
        "all_wishlists" : Wishlist.objects.exclude(wished_by = user)
    }
    return render(request, 'wishlist/dashboard.html', context)


def create_wish_page(request):

    return render(request, 'wishlist/add_wish.html')


def wish_page(request, id):
    user = User.objects.get(id = request.session["user_id"])
    wish = Wishlist.objects.get(id = id)
    context = {
        "user" : user,
        "users" : User.objects.filter(my_wishlists = wish),
        "wish" : wish
    }
    return render(request, "wishlist/wishes.html", context)


def create_wish(request):
    user = User.objects.get(id = request.session["user_id"])
    
    #Creates new wishlist and adds to the database
    Wishlist.objects.create(
        item_name = request.POST['item_name'],
        added_by = user
    )
    return redirect('/dashboard')


def add_wish(request, id):
    user = User.objects.get(id = request.session["user_id"])
    wishlist = Wishlist.objects.get(id = id) 
    user.my_wishlists.add(wishlist)
    user.save()
    return redirect('/dashboard')


def remove_wish(request, id):
    user = User.objects.get(id = request.session["user_id"])    
    wishlist = Wishlist.objects.get(id = id) 
    user.my_wishlists.remove(wishlist)
    return redirect('/dashboard')
    
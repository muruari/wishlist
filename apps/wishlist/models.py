from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re

class UserManager(models.Manager):
    def validate(self, postData):
        errors = []

        if len(postData.get('name')) and len(postData.get('username')) < 3:
            is_valid = False
            errors.append('Name and username must have at least 3 characters each. Please try again.')

        if len(User.objects.filter(username = postData.get("username"))) > 0:
            is_valid = False
            errors.append('That username is already taken. Please try again.')

        if not re.search(r'^[a-z" "A-Z]+$', postData.get('name')):
            is_valid = False
            errors.append('Name must be alphabetical characters only. Please try again.')

        if len(postData.get('password')) < 4:
            is_valid = False
            errors.append('Passwords must have at least 5 characters. Please try again.')

        if postData.get('password_confirmation') != postData.get('password'):
            is_valid = False
            errors.append('Passwords do not match. Please try again.')
        return errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    date_hired = models.DateField(default = '2018-04-13')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
    def __str__(self):
        return "name:{}, username:{}, password:{}, date_hired, created_at:{}, updated_at:{}".format(self.name, self.username, self.password, self.date_hired, self.created_at, self.updated_at)



class WishlistManager(models.Manager):
    def validate_wish(self, postData):
        errors = []

        if len(postData.get('item_name')) < 3:
            is_valid = False
            errors.append('Wish name must have at least 3 characters. Please try again.')

        if len(Wishlist.objects.filter(item_name = postData.get("item_name"))) > 0:
            is_valid = False
            errors.append('That wish has already been made. Please try again.')

        if not re.search(r'^[a-z" "A-Z]+$', postData.get('item_name')):
            is_valid = False
            errors.append('Name must be alphabetical characters only. Please try again.')

        return errors


class Wishlist(models.Model):
    item_name = models.CharField(max_length = 255)
    date_added = models.DateField(auto_now_add = True)
    added_by = models.ForeignKey(User, related_name="added_by_user")
    wished_by = models.ManyToManyField(User, related_name="my_wishlists")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = WishlistManager()

""" The file containing all the views for the landing page """

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    """ The index function returns the landing page's home.html """
    # Render takes the arguments: request (just passing it through), 
    # and the path in the local "templates" dir for the html file to load
    # Can also pass a dictionary through a third argument.
    return render(request, "landing/home.html")

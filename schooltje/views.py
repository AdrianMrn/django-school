# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render, redirect
from django.http import Http404 #future: 404 this for all urls that don't exist? https://docs.djangoproject.com/en/1.11/intro/tutorial03/#raising-a-404-error

#can be removed once all functions use return render/redirect instead of HttpResponse & loader
from django.http import HttpResponse

from .models import Richting, Leraar, Klas, Contact

import datetime
def index(request):
    lastPageVisited = setLastPage('schooltje:index', request)

    #time of day greet
    currentTime = datetime.datetime.now().hour
    greeting = ""
    if currentTime < 12 :
        greeting = "Goedemorgen"
    elif currentTime > 12 :
        greeting = "Goedemiddag"
    elif currentTime > 18 :
        greeting = "Goedenavond"

    #check for returning user
    if 'returning' in request.COOKIES:
        greeting += ", welkom terug!"

    context = {'greeting': greeting, 'lastPageVisited':lastPageVisited}

    response = render(request, 'schooltje/index.html', context)

    #all visited pages in session
    if 'uniq_sesh_id' in request.COOKIES:
        sessionkey = request.COOKIES['uniq_sesh_id']
    else:
        sessionkey = request.session.session_key #taking session key once at the start of session and using this as a static, unique session id
        response.set_cookie('uniq_sesh_id', sessionkey) #set a session time to 30 minutes, because set_expiry doesn't work with cookies

    pagesInSession(request, sessionkey, 'index')

    #if cookies get blocked or cause an error (eg too large), return response without setting cookies
    try:
        #first time user set returning cookie
        if not 'returning' in request.COOKIES:
            response.set_cookie('returning', 'true', max_age=10 * 365 * 24 * 60 * 60)
        #saving visited pages in cookie
        if 'pages_visited' in request.COOKIES:
            cookie_pagesVisited = request.COOKIES['pages_visited']
            cookie_pagesVisited += " index"
            response.set_cookie('pages_visited', cookie_pagesVisited)
        else:
            response.set_cookie('pages_visited', 'index')
    except:
        return response
    
    return response

def richtingen(request):
    lastPageVisited = setLastPage('schooltje:richtingen', request)

    richtingen_list = Richting.objects.all()
    context = {'richtingen_list': richtingen_list, 'lastPageVisited':lastPageVisited}

    response = render(request, 'schooltje/richtingen.html', context)

    #all visited pages in session
    if 'uniq_sesh_id' in request.COOKIES:
        sessionkey = request.COOKIES['uniq_sesh_id']
    else:
        sessionkey = request.session.session_key #taking session key once at the start of session and using this as a static, unique session id
        response.set_cookie('uniq_sesh_id', sessionkey) #set a session time to 30 minutes, because set_expiry doesn't work with cookies

    pagesInSession(request, sessionkey, 'richtingen')

    #saving visited pages in cookie
    if 'pages_visited' in request.COOKIES:
        cookie_pagesVisited = request.COOKIES['pages_visited']
        cookie_pagesVisited += " richtingen"
        response.set_cookie('pages_visited', cookie_pagesVisited)
    else:
        response.set_cookie('pages_visited', 'richtingen')

    return response

def wieiswie(request):
    lastPageVisited = setLastPage('schooltje:wieiswie', request)

    leraren_list = Leraar.objects.all()
    for leraar in leraren_list:
        klassen_list = Klas.objects.filter(leraar_id=leraar.id)
        leraar.klassen = list(klassen_list)

    context = {'leraren_list': leraren_list, 'lastPageVisited':lastPageVisited,}

    response = render(request, 'schooltje/wieiswie.html', context)

    #all visited pages in session
    if 'uniq_sesh_id' in request.COOKIES:
        sessionkey = request.COOKIES['uniq_sesh_id']
    else:
        sessionkey = request.session.session_key #taking session key once at the start of session and using this as a static, unique session id
        response.set_cookie('uniq_sesh_id', sessionkey) #set a session time to 30 minutes, because set_expiry doesn't work with cookies

    pagesInSession(request, sessionkey, 'wieiswie')

    #saving visited pages in cookie
    if 'pages_visited' in request.COOKIES:
        cookie_pagesVisited = request.COOKIES['pages_visited']
        cookie_pagesVisited += " wieiswie"
        response.set_cookie('pages_visited', cookie_pagesVisited)
    else:
        response.set_cookie('pages_visited', 'wieiswie')

    return response

def contact(request):
    lastPageVisited = setLastPage('schooltje:contact', request)

    context = {'lastPageVisited':lastPageVisited,}
    response = render(request, 'schooltje/contact.html', context)

    #all visited pages in session
    if 'uniq_sesh_id' in request.COOKIES:
        sessionkey = request.COOKIES['uniq_sesh_id']
    else:
        sessionkey = request.session.session_key #taking session key once at the start of session and using this as a static, unique session id
        response.set_cookie('uniq_sesh_id', sessionkey) #set a session time to 30 minutes, because set_expiry doesn't work with cookies

    pagesInSession(request, sessionkey, 'contact')

    #saving visited pages in cookie
    if 'pages_visited' in request.COOKIES:
        cookie_pagesVisited = request.COOKIES['pages_visited']
        cookie_pagesVisited += " contact"
        response.set_cookie('pages_visited', cookie_pagesVisited)
    else:
        response.set_cookie('pages_visited', 'contact')

    return response

    #future: accept url parameter for error message ("bericht verstuurd")? https://stackoverflow.com/questions/17202861/django-no-reverse-match-with-arguments

def contactpost(request):
    new_entry = Contact(email=request.POST['email'], nummer=request.POST['nummer'], content=request.POST['content'])
    new_entry.save()

    return redirect('schooltje:contact')

def setLastPage(page, request):
    #getting last visited page and then setting it to current page (session)
    lastPageVisited = request.session.get('lastPageVisited',page)
    request.session['lastPageVisited'] = page

    return lastPageVisited

#all visited pages in session
def pagesInSession(request, sessionkey, page):
    with open('sessions.json', 'r') as f:
        data = json.load(f)

    with open('sessions.json', 'w') as f:
        if sessionkey in data:
            data[sessionkey] += " " + page 
            json.dump(data, f)
        else:
            data[sessionkey] = page
            json.dump(data, f)
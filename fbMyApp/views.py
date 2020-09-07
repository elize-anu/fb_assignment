# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import json
import facebook
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def fetch_posts_from_page (request):
    token = ["EAAFMtgP4iwoBAEuEkGK4sPFRc8Po5uCpdxdk4mKVGGvWkpkOUzkUrcEmsIia0J7alwTgI34CiNqh3Ku233Pm3EmzAkeLhpbVcuNo9KtzsAHbAL8PJsckZBy3pgrt7bot8ZALbVtWZBwrQLeWwPV8ZAWd2OVbBPNlF2fSzCKQdqbwtqVGG9Gw"]
    if request.method == 'POST':
        # try :
        #     result = {}
            graph = facebook.GraphAPI(token)
            # fields = ["full_picture", "message","picture", "permalink_url", "id"]
            # profile = graph.get_object("elizeanu", fields=fields)
            data = [ "posts"]
            profile = graph.get_object("elizeanu",fields=data)
            # profile = graph.get_object("me",fields=data)
            
            # print("-->", profile)
            
        # except Exception as e:
        #     result["success"] = False
        #     return HttpResponse(result,content_type='application/json')


            return HttpResponse(json.dumps(profile),content_type='application/json')


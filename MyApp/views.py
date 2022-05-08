from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.
@api_view(["POST"])
def test(string_to_cut):
    try:
        height=json.loads(string_to_cut.body)
        print(height)
        newString= height['string_to_cut']
        result_string = cut_string(newString)
        return_json = {
        "return_string": result_string,
        }
        print(return_json)
        return JsonResponse(return_json,safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def cut_string(string):
    i = 0
    cut_list = []
    for char in string:
        i += 1
        if i == 3:
            cut_list.append(char)
            i = 0
    return "".join(cut_list)

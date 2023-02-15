from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def profile(req):
    temp = """
    <a href='{}'> product profile</a>|
    <a href='{}'>product login</a>|
    <a href='{}'>product logout</a>
    """.format(reverse("product:profile"), reverse("product:login"), reverse("product:logout"))
    return HttpResponse(temp)


def login(req):
    temp = """
        <a href='{}'> product profile</a>|
        <a href='{}'>product login</a>|
        <a href='{}'>product logout</a>
        """.format(reverse("product:profile"), reverse("product:login"), reverse("product:logout"))
    return HttpResponse(temp)


def logout(req):
    temp = """
        <a href='{}'> product profile</a>|
        <a href='{}'>product login</a>|
        <a href='{}'>product logout</a>
        """.format(reverse("product:profile"), reverse("product:login"), reverse("product:logout"))
    return HttpResponse(temp)

from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.urls import reverse


def profile(req):
    # temp = """
    # <a href='{}'>profile</a>|
    # <a href='{}'>login</a>|
    # <a href='{}'>logout</a>
    # """.format(reverse("account:profile"), reverse("account:login"), reverse("account:logout"))
    # return HttpResponse(temp)
    # print(type(reverse("account:login")))
    # return render(req, "account/profile.html", {"saeed": "hassani"})
    # return HttpResponse("{'joon':'baba'}", status=200, content_type="application/json")
    # return Http404

    return JsonResponse({"jafar": True}, safe=True)
    # return "asd"


def login(req):
    # temp = """
    # <a href='{}'>profile</a>|
    # <a href='{}'>login</a>|
    # <a href='{}'>logout</a>
    # """.format(reverse("account:profile"), reverse("account:login"), reverse("account:logout"))
    # return HttpResponse(temp)
    return render(req, "account/login.html", {})


def logout(req):
    # temp = """
    # <a href='{}'>profile</a>|
    # <a href='{}'>login</a>|
    # <a href='{}'>logout</a>
    # """.format(reverse("account:profile"), reverse("account:login"), reverse("account:logout"))
    # return HttpResponse(temp)
    return render(req, "account/logout.html", {})

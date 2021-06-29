from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict

from django.urls.base import reverse
challenges = OrderedDict()
challenges = {
    "january": "Eat healthy food for the entire month",
    "february":  "Walk for 20 mins at least per day",
    "march":"Learn django for at least 30 mins every day",
    "april":"Solve at least one problem daily",
    "may":"Give 30 mins to ur personal development daily",
    "june":"Read books for at least 30 mins every day",
    "july":"Read books for at least 30 mins every day",
    "august":"Complete courses this month",
    "september":"Give 30 mins to ur personal development daily",
    "october":"Solve at least one problem daily",
    "november":"Give 30 mins to ur personal development daily",
    "december":"Complete courses this month"
}

# Create your views here
def monthly_challenges_by_number(requests,month):
    months = list(challenges.keys())
    if month >len(months):
        return HttpResponseNotFound("This month is not supported")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) #/challenges
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request,month):
    try:
        challenge_next = challenges[month.lower()]
        response_text = f"<h1>{challenge_next}<h1>"
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound("This month is not supported")


def index(request):
    list_items = ""
    months = list(challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

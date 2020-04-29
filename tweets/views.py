from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

def home_view(request, *args, **kwargs):
      print(args, kwargs)
      # return HttpResponse("<h1>Hey World</h1>")
      return render(request, "pages/home.html", context = {})

def tweet_detail_view(request, tweet_id, *args, **kwargs):
      print(args, kwargs)
      context = {
            "success" : True,
            "message" : "Tweets Found",
      }
      status = 200
      data = {}

      try :
            tweet = Tweet.objects.get(id=tweet_id)
            
            data["id"] = tweet.id
            data["content"] = tweet.content

            context["data"] = data

      except:
            context["message"] = "Twwet Not Found"
            status = 404

      return JsonResponse(context, status = status)
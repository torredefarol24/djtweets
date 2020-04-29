from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

def home_view(request, *args, **kwargs):
      print(args, kwargs)
      return HttpResponse("<h1>Hey World</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
      print(args, kwargs)
      try :
            tweet = Tweet.objects.get(id=tweet_id)
      except:
            raise Http404

      context = {
            "success" : True,
            "message" : "Tweets Found",
            "data" : {
                  "id" : tweet.id,
                  "content" : tweet.content
            }
      }

      # return HttpResponse(f"<h1>Tweet Detail View TweetID:{tweet_id} Content:{tweet.content}</h1>")
      return JsonResponse(context)
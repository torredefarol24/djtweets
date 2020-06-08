import random 
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm


def home_view(request, *args, **kwargs):
      print(args, kwargs)
      # return HttpResponse("<h1>Hey World</h1>")
      return render(request, "pages/home.html", context = {})

def tweet_create_view(request, *args, **kwargs):
      form = TweetForm(request.POST or None)
      if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form = TweetForm()
      context = {
            "form" : form
      }
      return render(request, 'components/form.html', context = context)

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
            context["message"] = "Tweet Not Found"
            status = 404

      return JsonResponse(context, status = status)


def tweet_list_view(request, *args, **kwargs):
      qs = Tweet.objects.all()
      tweets = [ {"id" : x.id, "content" : x.content, "likes" : random.randint(0, 600) } for x in qs]
      data = {
            "isUser" : False,
            "success" : True,
            "message" : "Tweets Found",
            "data" : tweets
      }

      return JsonResponse(data)
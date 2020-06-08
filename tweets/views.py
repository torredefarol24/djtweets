import random 
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request, *args, **kwargs):
      print(args, kwargs)
      return render(request, "pages/home.html", context = {})

def tweet_create_view(request, *args, **kwargs):
      form = TweetForm(request.POST or None)
      next_url = request.POST.get("next") or None

      if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            if request.is_ajax():
                  return JsonResponse({}, status=201)

            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                  return redirect(next_url)
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
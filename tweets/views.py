import random 
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url
from .serializers import TweetSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request, *args, **kwargs):
      print(args, kwargs)
      return render(request, "pages/home.html", context = {})

def tweet_create_view(request, *args, **kwargs):
      data = request.POST or None
      serializer = TweetSerializer(data = data)
      if serializer.is_valid():
            obj = serializer.save(user = request.user)
            return JsonResponse( serializer.data , status = 201)

      return JsonResponse({}, status = 400)


def tweet_create_view_pure_django(request, *args, **kwargs):
      user = request.user
      if not request.user.is_authenticated:
            user = None
            if request.is_ajax():
                  return JsonResponse({}, status = 401)
            return redirect(settings.LOGIN_URL)


      form = TweetForm(request.POST or None)
      next_url = request.POST.get("next") or None

      if form.is_valid():

            obj = form.save(commit=False)
            obj.user = user
            obj.save()

            if request.is_ajax():
                  return JsonResponse(obj.serialize(), status=201)

            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                  return redirect(next_url)

            form = TweetForm()

      if form.errors:
            if request.is_ajax():
                  return JsonResponse(form.errors, status = 400)

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
      tweets = [ x.serialize() for x in qs]
      data = {
            "isUser" : False,
            "success" : True,
            "message" : "Tweets Found",
            "data" : tweets
      }

      return JsonResponse(data)
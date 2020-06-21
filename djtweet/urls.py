from django.contrib import admin
from django.urls import path
from tweets.views import home_view, tweet_detail_view, tweet_list_view, tweet_create_view, tweet_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view),
    path("api/create-tweet", tweet_create_view),
    path("api/tweets", tweet_list_view),
    path("api/tweets/<int:tweet_id>", tweet_detail_view),
    path("api/tweets/<int:tweet_id>/delete", tweet_delete_view)

]

from django.conf.urls import url, include
from bookmark.views import BookmarkDV, BookmarkLV

app_name = 'bookmark'

urlpatterns = [
    # class-based views for bookmark app
    url('r^$', BookmarkLV.as_view(), name='index'),
    url('r^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail')
]
from django.contrib import admin
from django.conf.urls import include, url

from books.views import list_books
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', list_books, name='books'),
]
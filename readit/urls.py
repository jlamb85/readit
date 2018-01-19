from django.contrib import admin
from django.conf.urls import include, url

from books.views import (AuthorDetail, AuthorList, BookDetail,
                         list_books, review_book, ReviewList, CreateAuthor)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', list_books, name='books'),
    url(r'^authors/$', AuthorList.as_view(), name='authors'),
    url(r'^books/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name='book-detail'),
    url(r'^authors/add/$', CreateAuthor.as_view(), name='add-author'),
    url(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^review/$', ReviewList.as_view(), name='review-books'),
    url(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),
]
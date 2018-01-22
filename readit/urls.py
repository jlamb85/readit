from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from books.views import (AuthorDetail, AuthorList, BookDetail,
                         list_books, review_book, ReviewList, CreateAuthor)

urlpatterns = [
    # Auth
    url(r'^logout/$', auth_views.logout, {'next_page': 'books' }, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html' }, name='login'),
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Custom
    url(r'^$', list_books, name='books'),
    url(r'^authors/$', AuthorList.as_view(), name='authors'),
    url(r'^books/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name='book-detail'),
    url(r'^authors/add/$', login_required(CreateAuthor.as_view()), name='add-author'),
    url(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^review/$', login_required(ReviewList.as_view()), name='review-books'),
    url(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),
]
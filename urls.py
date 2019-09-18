from django.conf.urls import url
from BRMapp import views
from django.urls import path

urlpatterns=[
 url('view-book',views.viewbook),
  url('edit-book',views.editBook),
   url('edit',views.edit),
    url('delete-book',views.deleteBook),
     url('search-book',views.searchBook),
      url('search',views.search),
       url('new-book',views.newbook),
        url(r'^add',views.add),
        url('login',views.userLogin),
        url('logout',views.userLogout),
]

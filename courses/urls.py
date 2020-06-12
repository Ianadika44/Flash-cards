from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    url('^today/$', views.courses_today, name='notesToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^notes/(\d+)',views.notes,name ='notes'),
    url(r'^new/notes$', views.new_notes, name='new-notes')
   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

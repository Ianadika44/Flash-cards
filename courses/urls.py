from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit/profile/$',views.profile_edit,name = 'edit_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^card/',views.card,name ='card'),
    url(r'^new/card$', views.new_card, name='new-card'),
    #url('^today/$',views.notes_of_day,name='notesToday'),
    #url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews') 
]
if settings.DEBUG:
    
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
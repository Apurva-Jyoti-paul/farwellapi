from . import views
from django.urls import path

urlpatterns=[

path('home/',views.home,name='home'),
#apis
path('apireqseniorall/',views.see_seniors,name="see"),
path('apireqseniori/<key>',views.indv_senior,name="seeindv"),
path('apireqseniorawrd/<key>',views.awrds_senior,name="seeawrds"),
path('apireqseniorgall/<key>',views.gallery_senior,name="seegallery"),
#path('apicomplete/<key>',views.complete,name="completeinfo"),
path('apireqseniorrat/<key>',views.rating_senior,name="seerating"),
]
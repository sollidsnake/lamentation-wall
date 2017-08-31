from django.conf.urls import url

from index_board import views

urlpatterns  = ['',
                url(r'crytogether', views.cry_together),
                url(r'', views.index),
]

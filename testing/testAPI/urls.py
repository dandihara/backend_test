from django.urls import path
from . import views
urlpatterns = [
    path('',views.CounterView.as_view(),name = 'person_statics'),
    path('entrance',views.EntranceView.as_view(),name='entrance_statics'),
    path('concept/<str:name>',views.SearchView.as_view(),name = 'use_concepts'),
    path('table/<str:name>',views.GetTableValuesView.as_view(),name='table_values')
]
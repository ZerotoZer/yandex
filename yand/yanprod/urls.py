from django.urls import path
from . import views

urlpatterns = [
    path('imports/', views.import_cp),
    path('nodes/<str:node_id>', views.node_tree),
    path('delete/<str:node_id>', views.delete),
]
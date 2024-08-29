from django.urls import path
from . import views

urlpatterns = [
    path("notes/",views.NoteListCreate.as_view(),name = "note-list"),
    path("notes/delete/<int:pk>/",views.NoteDelete.as_view(),name = "delete-one"),
     path('user/family-details/', views.FamilyDetailsListCreateView.as_view(), name='family-details-list-create'),
    path('user/family-details/<int:pk>/', views.FamilyDetailsUpdateDeleteView.as_view(), name='family-details-update-delete'),
]



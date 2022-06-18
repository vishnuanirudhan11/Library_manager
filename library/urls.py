from django.urls import path
from .import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('details/<slug:ct_slug>/<slug:bk_slug>/',views.details,name='details'),
    path('categories/<slug:ct_slug>/',views.details,name='categ'),
    path('cat_edit/<int:pk>/',views.Edit.as_view(),name='cat_edit'),
    path('cat_delete/<int:cat_id>/', views.cat_delete, name='cat_delete'),
    path('bk_delete/<int:bk_id>/', views.bk_delete, name='bk_delete'),
    path('bk_edit/<int:pk>/',views.Bkedit.as_view(),name='bk_edit'),
    path('add_cat/',views.add_cat,name='add_cat'),
    path('add_book/',views.add_book,name='add_book'),
    path('adminpanel/',views.adminpanel,name='adminpanel'),
    path('search/',views.search,name='search')
]

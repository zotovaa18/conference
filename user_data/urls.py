from django.urls import path
from .views import *

urlpatterns = [
    path('', BasePage, name='base'),
    path("section-number/", SectionNumberList.as_view(), name='section_number'),
    path("section-number/<int:pk>/", SectionNumberDetails.as_view(), name="section_number_detail"),
    path("scientific-director/", ScientificDirectorList.as_view(), name='scientific_director'),
    path("scientific-director/<int:pk>/", ScientificDirectorDetails.as_view(), name="scientific_director_detail"),
    path("author/", AuthorList.as_view(), name='author'),
    path("author/<int:pk>/", AuthorDetails.as_view(), name="author_detail"),
    path("thesis/", ThesisList.as_view(), name='thesis'),
    path("thesis/<int:pk>/", ThesisDetails.as_view(), name="thesis_detail"),
]
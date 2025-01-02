from django.urls import path

from .views import PizzaListCreateView, PizzaRetrieveUpdateDestroyView

urlpatterns = [
    path('', PizzaListCreateView.as_view(), name='get/post pizza'),
    path('/<int:pk>', PizzaRetrieveUpdateDestroyView.as_view(), name='retrieve/update/delete pizza'),
]

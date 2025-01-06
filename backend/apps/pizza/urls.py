from django.urls import path

from .views import PizzaListCreateView, PizzaRetrieveUpdateDestroyView

urlpatterns = [
    path('', PizzaListCreateView.as_view(), name='pizza_get_post'),
    path('/<int:pk>', PizzaRetrieveUpdateDestroyView.as_view(), name='pizza_retrieve_update_delete '),
]

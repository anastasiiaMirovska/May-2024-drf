from django.urls import path

from apps.pizza_shop.views import PizzaShopAddPizzaView, PizzaShopListCreateView

urlpatterns = [
    path('', PizzaShopListCreateView.as_view(), name='pizza-shop-list-create'),
    path('/<int:pk>/pizzas', PizzaShopAddPizzaView.as_view(), name='pizza-shop-create-pizza'),

]

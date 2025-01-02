from django.db.models import Q, Min, Max, Count
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request

from apps.pizza.filter import filter_pizza
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer

class PizzaListCreateView(ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()

    def get_queryset(self):
        return filter_pizza(self.request.query_params)

class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']

# class PizzaListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = PizzaModel.objects.all()
#     serializer_class = PizzaSerializer
#
#     def get_queryset(self):
#         return filter_pizza(self.request.query_params)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class PizzaRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = PizzaModel.objects.all()
#     serializer_class = PizzaSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

# Create your views here.
# class PizzaListCreateView(APIView):
#
#     def get(self, request: Request, **kwargs):
#         # pizzas = pizzas.filter(Q(size__lt=20) | Q(name='Margarita')).exclude(price__lt=300).order_by('size', '-price').reverse()
#         # pizzas = PizzaModel.objects.all()[2:5]# Тут це просто query в базу даних, а якщо ми пропишемо [2:5:2], то зробиться вже запит в базу даних
#         # pizzas = PizzaModel.objects.all().values("id", "name", "price") # Зменшуємо навантаження на базу даних, але тоді треба зробити серіалайзер під цей набір значень
#         # pizzas = PizzaModel.objects.aggregate(Min('size'), Max('price'))
#         # annotate = PizzaModel.objects.values('name').annotate(count=Count('name'))
#         # print(annotate)
#         # qs = PizzaModel.objects.all()
#         qs = filter_pizza(request.query_params)
#         serializer = PizzaSerializer(qs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = PizzaSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class PizzaRetrieveUpdateDestroyView(APIView):
#     def get(self,*args,**kwargs):
#         pk = kwargs.get('pk')
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = PizzaSerializer(pizza)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self,*args,**kwargs):
#         pk = kwargs.get('pk')
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response({'details': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         data = self.request.data
#         serializer = PizzaSerializer(instance=pizza, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self,*args,**kwargs):
#         pk = kwargs.get('pk')
#         try:
#             pizza = PizzaModel.objects.get(pk=pk).delete()
#         except PizzaModel.DoesNotExist:
#             return Response({'details': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         return Response({'details': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)


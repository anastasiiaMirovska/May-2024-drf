
from drf_yasg.utils import swagger_auto_schema

from django.utils.decorators import method_decorator

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaPhotoSerializer, PizzaResponseSerializer, PizzaSerializer


@method_decorator(name='post', decorator=swagger_auto_schema(security=[], operation_description='hahahaah'))
@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[],
        operation_description='hahahaah',
        responses={200: PizzaResponseSerializer()},
        operation_summary='get all pizzas'
    )
)

class PizzaListCreateView(ListCreateAPIView):
    """
    get:
    List all Pizza
    """
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects
    filterset_class = PizzaFilter
    permission_classes = (AllowAny,)
    @swagger_auto_schema(
        security=[],
        operation_description='hahahaah',
        responses={200: PizzaResponseSerializer()},
        operation_summary='get all pizzas'
    )
    def post(self, request, *args, **kwargs): # Якщо у нас є той метод, то ми просто навішуємо зверху сам swagger_auto_schema
        pass


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']


class PizzaAddPhotoView(UpdateAPIView):
    serializer_class = PizzaPhotoSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['put']
    permission_classes = (AllowAny,)

    def perform_update(self, serializer):
        pizza = self.get_object()
        pizza.photo.delete()
        super().perform_update(serializer)



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict

from users.models import UserModel


class UserListCreateView(APIView):
    def get(self):
        users = UserModel.objects.all()
        response = [model_to_dict(user) for user in users]
        return Response(response, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        user = UserModel(name=data['name'], age=data['age'], status=data['status'], weight=data['weight'])
        user.save()
        response = model_to_dict(user)
        return Response(response, status=status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response(f'User with id {pk} does not exist', status=status.HTTP_404_NOT_FOUND)
        return Response(model_to_dict(user), status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response(f'User with id {pk} does not exist', status=status.HTTP_404_NOT_FOUND)
        data = self.request.data
        for k, v in data.items():
            setattr(user, k, v)
        user.save()
        return Response(model_to_dict(user), status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            user = UserModel.objects.get(pk=pk).delete()
        except UserModel.DoesNotExist:
            return Response(f'User with id {pk} does not exist', status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)



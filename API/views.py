from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsersSerializer
from Authentication.models import CustomUser


@api_view(['GET'])
def getUsers(request):
    users = CustomUser.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    user = CustomUser.objects.get(email=pk)
    serializer = UsersSerializer(user, many=False)
    return Response(serializer.data)

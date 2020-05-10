from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserProfileSerializer, UserSerializer
from .permissions import IsAdminOrOwnerOrReadOnly


# Create your views here.
class UserList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({"success": "User '{}' created successfully".format(user.username)})


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [IsAdminOrOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def put(self, request, pk):
        saved_profile = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data
        serializer = self.serializer_class(instance=saved_profile, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            user_profile_saved = serializer.save()
            return Response({"success": "Profile '{}' updated successfully".format(user_profile_saved.username)})

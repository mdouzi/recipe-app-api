from rest_framework import generics
from rest_framework import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)
    


# Create your views here.


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serialzer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERED_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthencated]
    
    
    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
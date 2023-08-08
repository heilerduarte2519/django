from ejercicioeeg.models import Ejercicioeeg,Paciente
from ejercicioeeg.serializers import EjercicioeegSerializer,PacienteSerializer
from ejercicioeeg.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from ejercicioeeg.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from django_filters import rest_framework as filters

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'ejercicioeeg': reverse('ejercicioeeg-list', request=request, format=format),
        'paciente': reverse('paciente-list', request=request, format=format)

    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class EjercicioeegList(generics.ListAPIView):
    serializer_class = EjercicioeegSerializer
    name='ejercicioeeg-list'
    def get_queryset(self):
        queryset = Ejercicioeeg.objects.all()
        fechaint = self.request.query_params.get('fechaint')
        if fechaint is not None:
            queryset = queryset.filter(purchaser__fechaint=fechaint)
        return queryset
    #filter_backends = (filters.DjangoFilterBackend,)
    #filterset_class = EjercicioeegFilter


class EjercicioeegViewSet(viewsets.ModelViewSet):
    queryset = Ejercicioeeg.objects.all()
    serializer_class = EjercicioeegSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    #filterset_class = EjercicioeegFilter
    

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        ejercicioeeg = self.get_object()
        return Response(ejercicioeeg.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
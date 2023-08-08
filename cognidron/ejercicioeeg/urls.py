from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ejercicioeeg import views
from ejercicioeeg.views import EjercicioeegViewSet, UserViewSet, api_root,PacienteViewSet
from rest_framework import renderers

paciente_list = PacienteViewSet.as_view({
    'get': 'list',
})
paciente_detail = PacienteViewSet.as_view({
    'get': 'retrieve',
})

ejercicioeeg_list = EjercicioeegViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
ejercicioeeg_detail = EjercicioeegViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
ejercicioeeg_highlight = EjercicioeegViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('ejercicioeeg/', ejercicioeeg_list, name='ejercicioeeg-list'),
    path('ejercicioeeg/<int:pk>/', ejercicioeeg_detail, name='ejercicioeeg-detail'),
    path('ejercicioeeg/<int:pk>/highlight/', ejercicioeeg_highlight, name='ejercicioeeg-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('paciente/', paciente_list, name='paciente-list'),
    path('paciente/<int:pk>/', paciente_detail, name='paciente-detail'),

])

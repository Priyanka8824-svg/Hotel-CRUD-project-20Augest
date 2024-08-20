from django.urls import path
from .views import *

urlpatterns = [
    path('hv/', homeview),
    path('ov/', addview),
    path('sv/', showview),
    path("uv/<int:pk>/", updateview),
    path('dv/<int:x>/', deleteview)
]
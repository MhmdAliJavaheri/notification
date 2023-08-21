from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='home'),
    path('user/<int:user_id>/send_notification/', send_notification)
]

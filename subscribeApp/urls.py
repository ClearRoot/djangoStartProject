from django.urls import path

from subscribeApp.views import SubscriptionView

app_name = 'subscribeApp'

urlpatterns = [
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe'),
]

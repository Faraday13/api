from django.urls import path

from .views import GetItemAPIView, BuyItemAPIView

urlpatterns = [
    path('item/<int:id>/', GetItemAPIView.as_view()),
    path('buy/<int:id>/', BuyItemAPIView.as_view())
]
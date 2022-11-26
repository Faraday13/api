from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

import stripe

from .models import Item
from .serializers import ItemSerializer
from django.conf import settings


class GetItemAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name='index.html'

    def get(self, request, id):
        item = Item.objects.filter(id=id).first()
        
        return Response({
            'stripe_pk': settings.STRIPE_API_PUBLIC_KEY,
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            })


class BuyItemAPIView(APIView):

    def get(self, request, id):
        stripe.api_key = settings.STRIPE_API_PRIVATE_KEY
        item = Item.objects.filter(id=id).first()
        session = stripe.checkout.Session.create(
            line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                'name': item.name,
                },
                'unit_amount': int(item.price),
            },
            'quantity': 1,
            }],
            mode='payment',
            success_url=f'http://localhost:8000/item/{item.id}',
            cancel_url=f'http://localhost:8000/item/{item.id}',
        )

        return Response(session)

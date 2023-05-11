from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PaymentSerializer
from .models import Payment

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    path = {
        "get-all": "/all-payments",
    }
    return Response(path)

@api_view(['GET'])
def getAllPayments(request):

    payments = Payment.objects.all()
    serialized_payments = PaymentSerializer(payments, many=True)
    return Response(serialized_payments.data)

@api_view(['POST'])
def submitPayment(request):
    print("This is the data")
    print(request.data)

    data = {}
    payment = PaymentSerializer(data = request.data)

    if payment.is_valid():
        payment.save()
        data['status'] = True
    else:
        data['status'] = False

    return Response(data)

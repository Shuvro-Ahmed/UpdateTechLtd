from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sales
from .serializers import SalesSerializer

@api_view(['POST'])
def create_sale(request):
    serializer = SalesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_sales(request):
    sales = Sales.objects.all()
    serializer = SalesSerializer(sales, many=True)
    return Response(serializer.data)

# Add more API views as per your requirements
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def generate_pdf_report(request):
    sales = Sales.objects.all()

    # Generate the PDF report using the sales data
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sales_report.pdf"'

    p = canvas.Canvas(response)
    # Add your code to generate the PDF report here

    p.showPage()
    p.save()

    return response

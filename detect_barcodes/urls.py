from django.urls import path
from .views import generate_pdf

from . import views

urlpatterns = [
    path('', views.detect_barcode, name='detect_barcode'),
   # path('', views.detect_barcode, name='detect_barcodes'),
    path('camera_feed', views.camera_feed, name='camera_feed'),
    path('detect_barcodes/', views.detect_barcode, name='detect_barcodes-detect_barcodes'),
    path('get_customer_details/', views.get_customer_details, name='get_customer_details'),
    path('detect_inverter/', views.detect_inverter, name='detect_barcodes-detect_inverter'),
    path('get_inverter_details/', views.get_inverter_details, name='get_inverter_details'),
   # path('create-pdf', views.pdf_barcode_create, name='create-pdf'),
    path('generate-pdf/', views.generate_pdf, name='generate-pdf')
]

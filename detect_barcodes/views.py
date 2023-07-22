
import os
import time
from datetime import datetime
import cv2
import numpy as np
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from PIL import Image
from pyzbar.pyzbar import decode

from customer.models import Customer
import json
from django.http import HttpResponse, JsonResponse

from dashboard.models import staff_Notification
from .models import BarcodeImage, InverterImage
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
#from utils.camera_streaming_widget import CameraStreamingWidget
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
import base64
import cv2
import numpy as np
import pytz
from pyzbar import pyzbar
from .models import BarcodeImage
from .models import Customer
from django.contrib.auth.models import User  # Import the User model


import base64
import cv2
import numpy as np
from django.http import JsonResponse
from pyzbar import pyzbar
from django.utils import timezone
import pytz

import base64
import cv2
import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from pyzbar import pyzbar

from django.shortcuts import render
from django.http import JsonResponse
from .models import BarcodeImage
from django.utils import timezone
import base64
import cv2
import numpy as np
from pyzbar import pyzbar

from django.shortcuts import render
from django.http import JsonResponse
import cv2
from pyzbar import pyzbar
import base64



@login_required(login_url='user-login')

# Camera feed
def camera_feed(request):
    stream = CameraStreamingWidget()
    frames = stream.get_frames()

    # if ajax request is sent
    if request.is_ajax():
        print('Ajax request received')
        time_stamp = str(datetime.now().strftime("%d-%m-%y"))
        image = os.path.join(os.getcwd(), "media",
                             "images", f"img_{time_stamp}.png")
        if os.path.exists(image):
            # open image if exists
            im = Image.open(image)
            # decode barcode
            if decode(im):
                for barcode in decode(im):
                    barcode_data = (barcode.data).decode('utf-8')
                    file_saved_at = time.ctime(os.path.getmtime(image))
                    # return decoded barcode as json response
                    return JsonResponse(data={'barcode_data': barcode_data, 'file_saved_at': file_saved_at})
            else:
                return JsonResponse(data={'barcode_data': None})
        else:
            return JsonResponse(data={'barcode_data': None})
    # else stream the frames from camera feed
    else:
        return StreamingHttpResponse(frames, content_type='multipart/x-mixed-replace; boundary=frame')


# def detect(request):
#     stream = CameraStreamingWidget()
#     success, frame = stream.camera.read()
#     if success:
#         status = True
#     else:
#         status = False
#     return render(request, 'detect_barcodes/detect.html', context={'cam_status': status})


# def detect(request):
#     camera_value = os.environ.get('CAMERA')
#     if camera_value is not None:
#         camera = int(camera_value)
#     else:
#         camera = 0  # Assign a default camera value, such as 0 or another appropriate value
#
#     stream = CameraStreamingWidget(camera)
#     success, frame = stream.camera.read()
#     if success:
#         status = True
#     else:
#         status = False
#     return render(request, 'detect_barcodes/detect.html', context={'cam_status': status})


@login_required(login_url='user-login')
class CameraStreamingWidget:
    def __init__(self, camera):
        self.camera = cv2.VideoCapture(camera)

@login_required(login_url='user-login')
def detect(request):
    camera_value = os.environ.get('CAMERA')
    if camera_value is not None:
        try:
            camera = int(camera_value)
        except ValueError:
            # Handle the case when the camera value is not a valid integer
            # Assign a default camera value or take appropriate action
            camera = 0
    else:
        camera = 0  # Assign a default camera value, such as 0 or another appropriate value

    stream = CameraStreamingWidget(camera)
    success, frame = stream.camera.read()
    if success:
        status = True
    else:
        status = False
    return render(request, 'detect_barcodes/detect.html', context={'cam_status': status})


# def detect_barcode(request):
#     if request.method == 'POST':
#         image = request.FILES['image']
#         image_data = image.read()
#         image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#         nparr = np.frombuffer(image_data, np.uint8)
#         img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#
#         barcodes = pyzbar.decode(img)
#         if barcodes:
#             barcode_data = barcodes[0].data.decode('utf-8')
#             # Process the barcode data as needed
#             # Save the image or perform any other operations
#
#             response = {
#                 'barcode_data': barcode_data,
#                 'file_saved_at': '2023-06-06 10:30:00'  # Replace with the actual timestamp of the saved image
#             }
#         else:
#             response = {
#                 'barcode_data': None,
#                 'file_saved_at': None
#             }
#
#         return JsonResponse(response)
#
#     return render(request, 'detect_barcodes/detect_barcodes.html')

# def detect_barcode(request):
#     if request.method == 'POST':
#         response = []
#         images = request.FILES.getlist('image')  # Retrieve multiple uploaded images
#
#         for image in images:
#             image_data = image.read()
#             image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#             nparr = np.frombuffer(image_data, np.uint8)
#             img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#
#             barcodes = pyzbar.decode(img)
#             if barcodes:
#                 barcode_data = barcodes[0].data.decode('utf-8')
#                 # Process the barcode data as needed
#                 # Save the image or perform any other operations
#
#                 response.append({
#                     'barcode_data': barcode_data,
#                     'file_saved_at': '2023-06-06 10:30:00'  # Replace with the actual timestamp of the saved image
#                 })
#             else:
#                 response.append({
#                     'barcode_data': None,
#                     'file_saved_at': None
#                 })
#
#         return JsonResponse(response, safe=False)
#
#     return render(request, 'detect_barcodes/detect_barcodes.html')



# def detect_barcode(request):
#     if request.method == 'POST':
#         images = request.FILES.getlist('image')  # Get list of uploaded images
#
#         detected_barcodes = []
#
#         for image in images:
#             image_data = image.read()
#             image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#             nparr = np.frombuffer(image_data, np.uint8)
#             img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#
#             barcodes = pyzbar.decode(img)
#             if barcodes:
#                 barcode_data = barcodes[0].data.decode('utf-8')
#                 # Process the barcode data as needed
#                 # Save the image or perform any other operations
#
#                 detected_barcodes.append({
#                     'barcode_data': barcode_data,
#                     'file_saved_at': '2023-06-06 10:30:00'  # Replace with the actual timestamp of the saved image
#                 })
#             else:
#                 detected_barcodes.append({
#                     'barcode_data': None,
#                     'file_saved_at': None
#                 })
#
#         return JsonResponse(detected_barcodes, safe=False)
#
#     return render(request, 'detect_barcodes/detect_barcodes.html')






# def detect_barcode(request):
#     if request.method == 'POST':
#         images = request.FILES.getlist('image')  # Get list of uploaded images
#
#         detected_barcodes = []
#
#         for image in images:
#             image_data = image.read()
#             image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#             nparr = np.frombuffer(image_data, np.uint8)
#             img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#
#             barcodes = pyzbar.decode(img)
#             if barcodes:
#                 barcode_data = barcodes[0].data.decode('utf-8')
#                 # Process the barcode data as needed
#                 # Save the image or perform any other operations
#
#                 tz = pytz.timezone('Asia/Kolkata')  # Set the timezone to IST (Indian Standard Time)
#                 file_saved_at = timezone.now().astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')
#
#                 detected_barcodes.append({
#                     'barcode_data': barcode_data,
#                     'file_saved_at': file_saved_at
#                 })
#             else:
#                 detected_barcodes.append({
#                     'barcode_data': None,
#                     'file_saved_at': None
#                 })
#
#         return JsonResponse(detected_barcodes, safe=False)
#
#     return render(request, 'detect_barcodes/detect_barcodes.html')

# def detect_barcode(request):
#     if request.method == 'POST':
#         images = request.FILES.getlist('image')  # Get list of uploaded images
#
#         detected_barcodes = []
#
#         for image in images:
#             image_data = image.read()
#             image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#             nparr = np.frombuffer(image_data, np.uint8)
#             img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#
#             barcodes = pyzbar.decode(img)
#             if barcodes:
#                 barcode_data = barcodes[0].data.decode('utf-8')
#
#                 tz = pytz.timezone('Asia/Kolkata')  # Set the timezone to IST (Indian Standard Time)
#                 file_saved_at = timezone.now().astimezone(tz)
#
#                 barcode_image = BarcodeImage.objects.create(
#                     barcode_data=barcode_data,
#                     file_saved_at=file_saved_at,
#                     image=image
#                 )
#
#                 detected_barcodes.append({
#                     'barcode_data': barcode_data,
#                     'file_saved_at': file_saved_at.strftime('%Y-%m-%d %H:%M:%S'),
#                     'image_url': barcode_image.image.url
#                 })
#             else:
#                 detected_barcodes.append({
#                     'barcode_data': None,
#                     'file_saved_at': None,
#                     'image_url': None
#                 })
#
#         return JsonResponse(detected_barcodes, safe=False)
#
#     return render(request, 'detect_barcodes/detect_barcodes.html')






# import base64
# import cv2
# import numpy as np
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.utils import timezone
# import pytz
# from pyzbar import pyzbar
# from .models import BarcodeImage
#
# def detect_barcode(request):
#     if request.method == 'POST':
#         images = request.FILES.getlist('image')  # Get list of uploaded images
#
#         detected_barcodes = []
#
#         for image in images:
#             image_data = image.read()
#             image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#             nparr = np.frombuffer(image_data, np.uint8)
#             img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#
#             barcodes = pyzbar.decode(img)
#             if barcodes:
#                 for barcode in barcodes:
#                     barcode_data = barcode.data.decode('utf-8')
#                     barcode_type = barcode.type
#
#                     existing_barcode = BarcodeImage.objects.filter(barcode_data=barcode_data).first()
#
#                     if existing_barcode:
#                         detected_barcodes.append({
#                             'barcode_data': barcode_data,
#                             'barcode_type': barcode_type,
#                             'message': 'Barcode data already exists in the database.',
#                         })
#                     else:
#                         tz = pytz.timezone('Asia/Kolkata')  # Set the timezone to IST (Indian Standard Time)
#                         file_saved_at = timezone.now().astimezone(tz)
#
#                         barcode_image = BarcodeImage.objects.create(
#                             barcode_data=barcode_data,
#                             barcode_type=barcode_type,
#                             file_saved_at=file_saved_at,
#                             image=image
#                         )
#
#                         detected_barcodes.append({
#                             'barcode_data': barcode_data,
#                             'barcode_type': barcode_type,
#                             'file_saved_at': file_saved_at.strftime('%Y-%m-%d %H:%M:%S'),
#                             'image_url': barcode_image.image.url,
#                             'message': 'Barcode data saved successfully.',
#                         })
#             else:
#                 detected_barcodes.append({
#                     'barcode_data': None,
#                     'barcode_type': None,
#                     'message': 'No barcode detected in the image.',
#                 })
#
#         return JsonResponse(detected_barcodes, safe=False)
#
#     return render(request, 'detect_barcodes/detect_barcodes.html')



# def detect_barcode(request):
#
#     if request.method == 'POST':
#         images = request.FILES.getlist('image')  # Get list of uploaded images
#
#         detected_barcodes = []
#
#         for image in images:
#             company = request.POST.get('solarPlateCompany')  # Get the value of the company field
#             wattage = request.POST.get('wattage')  # Get the value of the wattage field
#             new_customer_id = request.POST.get('new_customer_id')
#             #assign_to_user = User.objects.get(id=new_customer)
#             company_name = request.POST.get('phone')
#             print(new_customer_id)
#             image_data = image.read()
#             image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#             nparr = np.frombuffer(image_data, np.uint8)
#             img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#
#             barcodes = pyzbar.decode(img)
#             if barcodes:
#                 for barcode in barcodes:
#                     barcode_data = barcode.data.decode('utf-8')
#                     barcode_type = barcode.type
#
#                     existing_barcode = BarcodeImage.objects.filter(barcode_data=barcode_data).first()
#
#                     if existing_barcode:
#                         detected_barcodes.append({
#                             'barcode_data': barcode_data,
#                             'barcode_type': barcode_type,
#                             'message': 'Barcode data already exists in the database.',
#                         })
#                     else:
#                         tz = pytz.timezone('Asia/Kolkata')  # Set the timezone to IST (Indian Standard Time)
#                         file_saved_at = timezone.now().astimezone(tz)
#
#                         barcode_image = BarcodeImage.objects.create(
#                             barcode_data=barcode_data,
#                             barcode_type=barcode_type,
#                             company=company,  # Save the company value
#                             wattage=wattage,  # Save the wattage value
#                             file_saved_at=file_saved_at,
#                             image=image,
#                             AssignTo=new_customer_id,
#                             #AssignTo=assign_to_user,
#                             AssignBy=request.user.id,
#                             company_name=company_name,
#
#                         )
#
#                         detected_barcodes.append({
#                             'barcode_data': barcode_data,
#                             'barcode_type': barcode_type,
#                             'file_saved_at': file_saved_at.strftime('%Y-%m-%d %H:%M:%S'),
#                             'image_url': barcode_image.image.url,
#                             'message': 'Barcode data saved successfully.',
#                         })
#             else:
#                 detected_barcodes.append({
#                     'barcode_data': None,
#                     'barcode_type': None,
#                     'message': 'No barcode detected in the image.',
#                 })
#
#         return JsonResponse(detected_barcodes, safe=False)
#
#     # return render(request, 'detect_barcodes/detect_barcodes.html')
#
#     companies = Customer.objects.all()
#     return render(request, 'detect_barcodes/detect_barcodes.html', {'companies': companies})

@login_required(login_url='user-login')
def detect_barcode(request):
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    if request.method == 'POST':
        images = request.FILES.getlist('image')  # Get list of uploaded images
        detected_barcodes = []
        product_name = None

        # Determine the product_name based on the template being used
        if request.path == '/detect_barcodes/detect_barcodes/':
            product_name = 'SolarPanel'
        elif request.path == '/detect_barcodes/detect_inverter/':
            product_name = 'Inverter'

        for image in images:
            company = request.POST.get('solarPlateCompany')  # Get the value of the company field
            wattage = request.POST.get('wattage')  # Get the value of the wattage field
            new_customer_id = request.POST.get('new_customer_id')
            company_name = request.POST.get('comp_name')  # Get the value of the dynamically changing textbox

            image_data = image.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')

            nparr = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            barcodes = pyzbar.decode(img)
            if barcodes:
                for barcode in barcodes:
                    barcode_data = barcode.data.decode('utf-8')
                    barcode_type = barcode.type

                    existing_barcode = BarcodeImage.objects.filter(barcode_data=barcode_data).first()

                    if existing_barcode:
                        detected_barcodes.append({
                            'barcode_data': barcode_data,
                            'barcode_type': barcode_type,
                            'message': 'Barcode data already exists in the database.',
                        })
                    else:
                        tz = pytz.timezone('Asia/Kolkata')  # Set the timezone to IST (Indian Standard Time)
                        file_saved_at = timezone.now().astimezone(tz)

                        if new_customer_id.isdigit():
                            assign_to_user = User.objects.get(id=new_customer_id)
                        else:
                            assign_to_user = None

                        barcode_image = BarcodeImage.objects.create(
                            barcode_data=barcode_data,
                            barcode_type=barcode_type,
                            company=company_name,  # Save the company value
                            wattage=wattage,  # Save the wattage value
                            file_saved_at=file_saved_at,
                            image=image,
                            AssignTo=assign_to_user,
                            AssignBy=request.user.id,
                            company_name=company,  # Save the value of the dynamically changing textbox
                            product_name=product_name,  # Set the product_name
                        )

                        detected_barcodes.append({
                            'barcode_data': barcode_data,
                            'barcode_type': barcode_type,
                            'file_saved_at': file_saved_at.strftime('%Y-%m-%d %H:%M:%S'),
                            'image_url': barcode_image.image.url,
                            'message': 'Barcode data saved successfully.',
                        })
            else:
                detected_barcodes.append({
                    'barcode_data': None,
                    'barcode_type': None,
                    'message': 'No barcode detected in the image.',
                })

        return JsonResponse(detected_barcodes, safe=False)

    companies = Customer.objects.all()
    return render(request, 'detect_barcodes/detect_barcodes.html', {'companies': companies,'count1':count1,'notification1':notification1})


@login_required(login_url='user-login')
def detect_inverter(request):
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    if request.method == 'POST':
        images = request.FILES.getlist('image')  # Get list of uploaded images
        detected_barcodes = []
        product_name = None

        # Determine the product_name based on the template being used
        if request.path == '/detect_barcodes/detect_barcodes/':
            product_name = 'SolarPanel'
        elif request.path == '/detect_barcodes/detect_inverter/':
            product_name = 'Inverter'

        for image in images:
            company = request.POST.get('solarPlateCompany')  # Get the value of the company field
            wattage = request.POST.get('wattage')  # Get the value of the wattage field
            new_customer_id = request.POST.get('new_customer_id')
            company_name = request.POST.get('comp_name')  # Get the value of the dynamically changing textbox

            image_data = image.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')

            nparr = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            barcodes = pyzbar.decode(img)
            if barcodes:
                for barcode in barcodes:
                    barcode_data = barcode.data.decode('utf-8')
                    barcode_type = barcode.type

                    existing_barcode = BarcodeImage.objects.filter(barcode_data=barcode_data).first()

                    if existing_barcode:
                        detected_barcodes.append({
                            'barcode_data': barcode_data,
                            'barcode_type': barcode_type,
                            'message': 'Barcode data already exists in the database.',
                        })
                    else:
                        tz = pytz.timezone('Asia/Kolkata')  # Set the timezone to IST (Indian Standard Time)
                        file_saved_at = timezone.now().astimezone(tz)

                        if new_customer_id.isdigit():
                            assign_to_user = User.objects.get(id=new_customer_id)
                        else:
                            assign_to_user = None

                        barcode_image = BarcodeImage.objects.create(
                            barcode_data=barcode_data,
                            barcode_type=barcode_type,
                            company=company_name,  # Save the company value
                            wattage=wattage,  # Save the wattage value
                            file_saved_at=file_saved_at,
                            image=image,
                            AssignTo=assign_to_user,
                            AssignBy=request.user.id,
                            company_name=company,  # Save the value of the dynamically changing textbox
                            product_name=product_name  # Set the product_name
                        )

                        detected_barcodes.append({
                            'barcode_data': barcode_data,
                            'barcode_type': barcode_type,
                            'file_saved_at': file_saved_at.strftime('%Y-%m-%d %H:%M:%S'),
                            'image_url': barcode_image.image.url,
                            'message': 'Barcode data saved successfully.',
                        })
            else:
                detected_barcodes.append({
                    'barcode_data': None,
                    'barcode_type': None,
                    'message': 'No barcode detected in the image.',
                })

        return JsonResponse(detected_barcodes, safe=False)

    companies = Customer.objects.all()
    return render(request, 'detect_barcodes/detect_inverter.html', {'companies': companies,'count1':count1,'notification1':notification1})


# def detect_barcode(request):
#     if request.method == 'POST':
#         images = request.FILES.getlist('image')  # Get list of uploaded images
#         detected_barcodes = []
#
#         for image in images:
#             company = request.POST.get('solarPlateCompany')  # Get the value of the company field
#             wattage = request.POST.get('wattage')  # Get the value of the wattage field
#             new_customer_id = request.POST.get('new_customer_id')
#             company_name = request.POST.get('comp_name')  # Get the value of the dynamically changing textbox
#             #print(company_name)
#             image_data = image.read()
#             image_base64 = base64.b64encode(image_data).decode('utf-8')
#
#             nparr = np.frombuffer(image_data, np.uint8)
#             img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#
#             barcodes = pyzbar.decode(img)
#             if barcodes:
#                 for barcode in barcodes:
#                     barcode_data = barcode.data.decode('utf-8')
#                     barcode_type = barcode.type
#
#                     existing_barcode = BarcodeImage.objects.filter(barcode_data=barcode_data).first()
#
#                     if existing_barcode:
#                         detected_barcodes.append({
#                             'barcode_data': barcode_data,
#                             'barcode_type': barcode_type,
#                             'message': 'Barcode data already exists in the database.',
#                         })
#                     else:
#                         tz = pytz.timezone('Asia/Kolkata')  # Set the timezone to IST (Indian Standard Time)
#                         file_saved_at = timezone.now().astimezone(tz)
#
#                         if new_customer_id.isdigit():
#                             #assign_to_user = int(new_customer_id)
#                             assign_to_user = User.objects.get(id=new_customer_id)
#                         else:
#                             assign_to_user = None
#
#                         barcode_image = BarcodeImage.objects.create(
#                             barcode_data=barcode_data,
#                             barcode_type=barcode_type,
#                             company=company_name,  # Save the company value
#                             wattage=wattage,  # Save the wattage value
#                             file_saved_at=file_saved_at,
#                             image=image,
#                             AssignTo=assign_to_user,
#                             AssignBy=request.user.id,
#                             company_name=company,  # Save the value of the dynamically changing textbox
#                             product_name='SolarPanel'
#                         )
#
#                         detected_barcodes.append({
#                             'barcode_data': barcode_data,
#                             'barcode_type': barcode_type,
#                             'file_saved_at': file_saved_at.strftime('%Y-%m-%d %H:%M:%S'),
#                             'image_url': barcode_image.image.url,
#                             'message': 'Barcode data saved successfully.',
#                         })
#             else:
#                 detected_barcodes.append({
#                     'barcode_data': None,
#                     'barcode_type': None,
#                     'message': 'No barcode detected in the image.',
#                 })
#
#         return JsonResponse(detected_barcodes, safe=False)
#
#     companies = Customer.objects.all()
#     return render(request, 'detect_barcodes/detect_barcodes.html', {'companies': companies})
#


@login_required(login_url='user-login')
def get_customer_details(request):

    if request.method == 'GET':
        comp_name = request.GET.get('comp_name')
        if comp_name:
            customer = Customer.objects.filter(Comp_name=comp_name).first()
            if customer:
                data = {
                    'Comp_name': customer.Comp_name,
                    'phone': customer.phone,
                    'Address': customer.Address,
                    'City': customer.City,
                    'Plant_Capacity': customer.Plant_Capacity,
                    'new_customer_id': customer.new_customer_id,  # Add the new field here
                    # Add other fields here
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps({}), content_type='application/json')


@login_required(login_url='user-login')
def get_inverter_details(request):
    if request.method == 'GET':
        comp_name = request.GET.get('comp_name')
        if comp_name:
            customer = Customer.objects.filter(Comp_name=comp_name).first()
            if customer:
                data = {
                    'Comp_name': customer.Comp_name,
                    'phone': customer.phone,
                    'Address': customer.Address,
                    'City': customer.City,
                    'Plant_Capacity': customer.Plant_Capacity,
                    'new_customer_id': customer.new_customer_id,  # Add the new field here
                    # Add other fields here
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps({}), content_type='application/json')



# def pdf_barcode_create(request):
#
#         images = request.FILES.getlist('image')  # Get list of uploaded images
#         detected_barcodes = []
#
#         for image in images:
#             # Image processing code here
#
#             # Barcode detection and handling code here
#
#             template_path = 'detect_barcodes/barcodepdf.html'
#             context = {'detected_barcodes': detected_barcodes}
#             response = HttpResponse(content_type='application/pdf')
#             response['Content-Disposition'] = 'filename="report.pdf"'
#             template = get_template(template_path)
#             html = template.render(context)
#
#             pisa_status = pisa.CreatePDF(html, dest=response)
#             if pisa_status.err:
#                 return HttpResponse('We had some errors <pre>' + html + '</pre>')
#
#         return response  # Move the return statement outside the loop



# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
# from reportlab.pdfgen import canvas


from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa


from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io


def generate_pdf(request):
    # Retrieve the data from the previous HTML template
    detected_barcodes = request.session.get('detected_barcodes', [])
    duplicate_barcodes_count = request.session.get('duplicate_barcodes_count', 0)

    # Generate the PDF page using the data
    template = get_template('detect_barcodes/pdf_template.html')
    context = {
        'detected_barcodes': detected_barcodes,
        'duplicate_barcodes_count': duplicate_barcodes_count,
    }
    rendered_template = template.render(context)

    # Create a BytesIO stream to receive the PDF output
    result = BytesIO()

    # Create the PDF document
    pdf = pisa.CreatePDF(BytesIO(rendered_template.encode('UTF-8')), dest=result)

    if not pdf.err:
        # Set the response headers for the PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="barcode_results.pdf"'

        # Get the PDF content from the BytesIO stream
        pdf_data = result.getvalue()
        result.close()

        # Write the PDF content to the response
        response.write(pdf_data)

        return response
    else:
        return HttpResponse("Error generating PDF", status=500)

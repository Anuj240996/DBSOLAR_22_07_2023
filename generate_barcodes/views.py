# # import barcode
# # import qrcode
# # from barcode.writer import ImageWriter
# # from django.http import HttpResponse
# # from django.shortcuts import render
# # from django.utils.encoding import smart_str
# #
# # #
# # # def generate_file(barcode_file):
# # #     # output = HttpResponse(content_type="image/jpeg")
# # #     output = HttpResponse(content_type="application/force-download")
# # #     barcode_file.save(output, "JPEG")
# # #     output['Content-Disposition'] = 'attachment; filename=%s' % smart_str('barcode.jpg')
# # #     output['X-Sendfile'] = smart_str('barcode.jpg')
# # #     return output
# # #
# # #
# # # # Create your views here.
# # # def generate(request):
# # #     context = {
# # #         'barcode_types': [b for b in barcode.PROVIDED_BARCODES if str(b).startswith('code')] + ['qrcode']
# # #     }
# # #
# # #     if request.method == 'POST':
# # #         b_type = request.POST['typeOfBarcode']
# # #         b_data = request.POST['barcodeData']
# # #
# # #         if b_type == 'qrcode':
# # #             qr = qrcode.QRCode(
# # #                 version=1,
# # #                 error_correction=qrcode.constants.ERROR_CORRECT_L,
# # #                 box_size=10,
# # #                 border=1,
# # #             )
# # #             qr.add_data(b_data)
# # #             qr.make(fit=True)
# # #             qr_file = qr.make_image(fill_color="black", back_color="white") # render qr image
# # #             return generate_file(qr_file) # generate the file
# # #
# # #         else:
# # #             bar = barcode.get_barcode(name=b_type, code=b_data, writer=ImageWriter())
# # #             barcode_file = bar.render() # creates a PIL class image object
# # #             return generate_file(barcode_file) # generate the file
# # #     else:
# # #         return render(request, 'generate_barcodes/generate.html', context=context)
# # # #
# # # # import cv2
# # # # from django.shortcuts import render
# # # # from django.db.models import F
# # # # from detect_barcodes.models import BarcodeImage
# # # #
# # # #
# # # # def barcode_generator(request):
# # # #     # Retrieve barcode data from the database
# # # #     barcode_data = BarcodeImage.objects.all().values('data', 'type')
# # # #
# # # #     barcodes = []
# # # #     for data in barcode_data:
# # # #         barcode = {
# # # #             'data': data['data'],
# # # #             'type': data['type'],
# # # #             'image': generate_barcode_image(data['data'], data['type'])
# # # #         }
# # # #         barcodes.append(barcode)
# # # #
# # # #     return render(request, 'barcode_generator.html', {'barcodes': barcodes})
# # # #
# # # #
# # # # def generate_barcode_image(data, barcode_type):
# # # #     # Generate barcode using OpenCV
# # # #     barcode = cv2.QRCodeDetector().generate(data)
# # # #
# # # #     # Convert barcode image to base64
# # # #     _, barcode_image = cv2.imencode('.png', barcode[1])
# # # #     barcode_image_base64 = barcode_image.tobytes()
# # # #
# # # #     return barcode_image_base64
# #
# #
# # import barcode
# # import qrcode
# # from barcode.writer import ImageWriter
# # from django.http import HttpResponse
# # from django.shortcuts import render
# # from django.utils.encoding import smart_str
# #
# # import barcode
# # import qrcode
# # from barcode.writer import ImageWriter
# # from django.http import HttpResponse
# # from django.shortcuts import render
# # from django.utils.encoding import smart_str
# #
# # def generate_file(barcode_file):
# #     output = HttpResponse(content_type="application/force-download")
# #     barcode_file.save(output, "JPEG")
# #     output['Content-Disposition'] = 'attachment; filename=%s' % smart_str('barcode.jpg')
# #     output['X-Sendfile'] = smart_str('barcode.jpg')
# #     return output
# #
# # def generate(request):
# #     context = {
# #         'barcode_types': [b for b in barcode.PROVIDED_BARCODES if str(b).startswith('code')] + ['qrcode']
# #     }
# #
# #     if request.method == 'POST':
# #         b_type = request.POST['typeOfBarcode']
# #         b_data = request.POST['barcodeData']
# #
# #         if b_type == 'qrcode':
# #             qr = qrcode.QRCode(
# #                 version=1,
# #                 error_correction=qrcode.constants.ERROR_CORRECT_L,
# #                 box_size=10,
# #                 border=1,
# #             )
# #             qr.add_data(b_data)
# #             qr.make(fit=True)
# #             qr_file = qr.make_image(fill_color="black", back_color="white")
# #             # Save the barcode data and type in the database
# #             save_barcode_data(b_data, b_type)
# #             return generate_file(qr_file)
# #         else:
# #             bar = barcode.get_barcode(name=b_type, code=b_data, writer=ImageWriter())
# #             barcode_file = bar.render()
# #             # Save the barcode data and type in the database
# #             save_barcode_data(b_data, b_type)
# #             return generate_file(barcode_file)
# #     else:
# #         # Retrieve barcode data from the database
# #         barcode_data = retrieve_barcode_data()
# #         barcodes = []
# #         for data in barcode_data:
# #             barcode_image = generate_barcode_image(data['data'], data['type'])
# #             barcode = {
# #                 'data': data['data'],
# #                 'type': data['type'],
# #                 'image': barcode_image
# #             }
# #             barcodes.append(barcode)
# #         return render(request, 'generate_barcodes/generate.html', {'barcodes': barcodes})
# #
# # def save_barcode_data(data, barcode_type):
# #     # Perform database operations to save the barcode data and type
# #     # This depends on your Django model and database configuration
# #     # Implement the logic to save the data in your barcodeimage table
# #     pass
# #
# # def retrieve_barcode_data():
# #     # Perform database operations to retrieve the barcode data and type
# #     # This depends on your Django model and database configuration
# #     # Implement the logic to retrieve the data from your barcodeimage table
# #     pass
# #
# # def generate_barcode_image(data, barcode_type):
# #     # Generate barcode using OpenCV or any other library of your choice
# #     # Return the path or URL of the generated barcode image
# #     # This depends on how you want to generate and store the barcode images
# #     pass
#
#
# from django.shortcuts import render
# from django.utils.encoding import smart_str
# from detect_barcodes.models import BarcodeImage
# import qrcode
# from barcode.writer import ImageWriter
# from django.http import HttpResponse
#
#
# import qrcode
# from barcode.writer import ImageWriter
# from io import BytesIO
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.utils.encoding import smart_str
#
# import qrcode
# from barcode import get_barcode
# from barcode.writer import ImageWriter
# from io import BytesIO
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.utils.encoding import smart_str
#
#
#
# def generate_file(barcode_file):
#     output = HttpResponse(content_type="image/jpeg")
#     barcode_file.save(output, "JPEG")
#     output['Content-Disposition'] = 'attachment; filename=%s' % smart_str('barcode.jpg')
#     output['X-Sendfile'] = smart_str('barcode.jpg')
#     return output
# #
# # def generate(request):
# #     companies = BarcodeImage.objects.values_list('company', flat=True).distinct()
# #
# #     if request.method == 'POST':
# #         selected_company = request.POST.get('company')
# #         barcode_images = BarcodeImage.objects.filter(company=selected_company)
# #         barcodes = []
# #
# #         for barcode_image in barcode_images:
# #             b_data = barcode_image.barcode_data
# #             b_type = barcode_image.barcode_type
# #
# #             if b_type == 'qrcode':
# #                 qr = qrcode.QRCode(
# #                     version=1,
# #                     error_correction=qrcode.constants.ERROR_CORRECT_L,
# #                     box_size=10,
# #                     border=1,
# #                 )
# #                 qr.add_data(b_data)
# #                 qr.make(fit=True)
# #                 qr_file = qr.make_image(fill_color="black", back_color="white")
# #                 barcode_image.image.save('barcode.jpg', qr_file)
# #                 barcode_image.save()
# #             else:
# #                 # Handle other barcode types
# #                 pass
# #
# #             barcodes.append(barcode_image)
# #
# #     else:
# #         selected_company = None
# #         barcodes = []
# #
# #     context = {
# #         'companies': companies,
# #         'selected_company': selected_company,
# #         'barcodes': barcodes
# #     }
# #
# #
# #     return render(request, 'generate_barcodes/generate.html', context=context)
#
#
# # ...
#
# def generate(request):
#     companies = BarcodeImage.objects.values_list('company', flat=True).distinct()
#
#     if request.method == 'POST':
#         selected_company = request.POST.get('company')
#         barcode_images = BarcodeImage.objects.filter(company=selected_company)
#         barcodes = []
#
#         for barcode_image in barcode_images:
#             if barcode_image.barcode_type == 'qrcode':
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=1,
#                 )
#                 qr.add_data(barcode_image.barcode_data)
#                 qr.make(fit=True)
#                 qr_image = qr.make_image(fill_color="black", back_color="white")
#                 buffer = BytesIO()
#                 qr_image.save(buffer, format='JPEG')
#                 barcode_data = buffer.getvalue()
#
#             else:
#                 barcode = get_barcode(
#                     barcode_image.barcode_type,
#                     barcode_image.barcode_data,
#                     writer=ImageWriter()
#                 )
#                 barcode_image = barcode.render()
#                 buffer = BytesIO()
#                 barcode_image.save(buffer, format='JPEG')
#                 barcode_data = buffer.getvalue()
#
#             barcodes.append(barcode_data)
#
#     else:
#         selected_company = None
#         barcodes = []
#
#     context = {
#         'companies': companies,
#         'selected_company': selected_company,
#         'barcodes': barcodes
#     }
#
#     return render(request, 'generate_barcodes/generate.html', context=context)

from io import BytesIO
import barcode
import qrcode
from barcode.writer import ImageWriter
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.views import static

from dashboard.models import staff_Notification
from detect_barcodes.models import BarcodeImage
from django.template.defaultfilters import safe

import re
import barcode
import qrcode
from barcode.writer import ImageWriter
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from detect_barcodes.models import BarcodeImage



#
#
# def generate_file(barcode_file):
#     output = HttpResponse(content_type="image/jpeg")
#     barcode_file.seek(0)  # Reset the file pointer
#     output.write(barcode_file.read())  # Read the file-like object and write its contents to the HttpResponse
#     output['Content-Disposition'] = 'attachment; filename=%s' % smart_str('barcode.jpg')
#     return output

# # to create barcode properly
# def generate(request):
#     companies = BarcodeImage.objects.order_by().values_list('company', flat=True).distinct()
#     selected_company = request.POST.get('company')
#
#     if selected_company:
#         barcode_images = BarcodeImage.objects.filter(company=selected_company)
#         barcodes = []
#
#         for barcode_image in barcode_images:
#             b_type = barcode_image.barcode_type
#             b_data = barcode_image.barcode_data
#
#             if b_type == 'qrcode':
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=1,
#                 )
#                 qr.add_data(b_data)
#                 qr.make(fit=True)
#                 qr_file = qr.make_image(fill_color="black", back_color="white")  # Render QR code image
#
#                 with BytesIO() as qr_bytes:
#                     qr_file.save(qr_bytes, format='JPEG')  # Save the QR code image to a BytesIO object
#                     qr_bytes.seek(0)  # Reset the file pointer
#                     barcode_image.image.save('barcode.jpg', qr_bytes, save=True)  # Save the image to the model
#
#             else:
#                 bar = barcode.get_barcode(name=b_type, code=b_data, writer=ImageWriter())
#                 barcode_file = bar.render()  # Create a PIL class image object
#
#                 with BytesIO() as barcode_bytes:
#                     barcode_file.save(barcode_bytes, format='JPEG')  # Save the barcode image to a BytesIO object
#                     barcode_bytes.seek(0)  # Reset the file pointer
#                     barcode_image.image.save('barcode.jpg', barcode_bytes, save=True)  # Save the image to the model
#
#             barcode_image.save()  # Save the updated model instance
#
#             # Add barcode data, barcode type, and barcode image URL to the list
#             barcodes.append((barcode_image.barcode_data, barcode_image.barcode_type, barcode_image.image.url))
#
#         return render(request, 'generate_barcodes/generate.html', {
#             'companies': companies,
#             'selected_company': selected_company,
#             'barcode_images': barcode_images,
#             'barcodes': barcodes
#         })
#
#     return render(request, 'generate_barcodes/generate.html', {
#             'companies': companies,
#             'selected_company': selected_company
#     })


# def sanitize_code39_data(data):
#     # Regular expression pattern to remove unsupported characters
#     pattern = r'[^A-Z0-9-.$/+% ]'
#     sanitized_data = re.sub(pattern, '', data)
#     return sanitized_data

from barcode import Code39
from barcode.writer import ImageWriter
from io import BytesIO
from io import BytesIO
import barcode
import qrcode
from barcode.writer import ImageWriter
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from detect_barcodes.models import BarcodeImage

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
import qrcode

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
import qrcode

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
import qrcode

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
import qrcode
import os
from django.conf import settings

import os
import itertools
from django.shortcuts import render
from detect_barcodes.models import BarcodeImage
import qrcode
#import barcodefrom inventoryproject import settings
from barcode.writer import ImageWriter
from io import BytesIO
import os
from django.core.files.base import ContentFile

@login_required(login_url='user-login')
def generate_file(barcode_file):
    output = HttpResponse(content_type="image/jpeg")
    barcode_file.seek(0)  # Reset the file pointer
    output.write(barcode_file.read())  # Read the file-like object and write its contents to the HttpResponse
    output['Content-Disposition'] = 'attachment; filename=%s' % smart_str('barcode.jpg')
    return output


...
#
# def generate(request):
#     companies = BarcodeImage.objects.order_by().values_list('company', flat=True).distinct()
#     selected_company = request.POST.get('company')
#
#     if selected_company:
#         barcode_images = BarcodeImage.objects.filter(company=selected_company)
#         barcodes = []
#
#         # Count the occurrences of each barcode type
#         barcode_type_counts = {}
#
#         for barcode_image in barcode_images:
#             b_type = barcode_image.barcode_type
#             b_data = barcode_image.barcode_data
#
#             if not barcode_image.barcode_path:  # Check if barcode_path is null
#                 if b_type not in barcode_type_counts:
#                     barcode_type_counts[b_type] = 1
#                 else:
#                     barcode_type_counts[b_type] += 1
#
#                 if b_type == 'qrcode':
#                     qr = qrcode.QRCode(
#                         version=1,
#                         error_correction=qrcode.constants.ERROR_CORRECT_L,
#                         box_size=10,
#                         border=1,
#                     )
#                     qr.add_data(b_data)
#                     qr.make(fit=True)
#                     qr_file = qr.make_image(fill_color="black", back_color="white")  # Render QR code image
#
#                     with BytesIO() as qr_bytes:
#                         qr_file.save(qr_bytes, format='JPEG')  # Save the QR code image to a BytesIO object
#                         qr_bytes.seek(0)  # Reset the file pointer
#
#                         # Generate the image name with the barcode type and sequential number
#                         image_filename = f"{b_type}_{barcode_type_counts[b_type]}.jpg"
#
#                         barcode_image.image.save(image_filename, qr_bytes, save=True)  # Save the image to the model
#
#                 else:
#                     bar = barcode.get_barcode(name=b_type, code=b_data, writer=ImageWriter())
#                     barcode_file = bar.render()  # Create a PIL class image object
#
#                     with BytesIO() as barcode_bytes:
#                         barcode_file.save(barcode_bytes, format='JPEG')  # Save the barcode image to a BytesIO object
#                         barcode_bytes.seek(0)  # Reset the file pointer
#
#                         # Generate the image name with the barcode type and sequential number
#                         image_filename = f"{b_type}_{barcode_type_counts[b_type]}.jpg"
#
#                         barcode_image.image.save(image_filename, barcode_bytes, save=True)  # Save the image to the model
#
#                 # Generate and save the barcode image path
#                 relative_image_path = os.path.join('static/barcode_images', image_filename)
#                 barcode_image.barcode_path = relative_image_path
#                 barcode_image.save()
#
#             # Add barcode data, barcode type, and barcode image URL to the list
#             barcodes.append((barcode_image.barcode_data, barcode_image.barcode_type, barcode_image.image.url))
#
#         return render(request, 'generate_barcodes/generate.html', {
#             'companies': companies,
#             'selected_company': selected_company,
#             'barcode_images': barcode_images,
#             'barcodes': barcodes
#         })
#
#     else:
#         return render(request, 'generate_barcodes/generate.html', {
#             'companies': companies,
#             'selected_company': None
#         })


import os
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

import os
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

import os
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

import os
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

import os
from django.core.files import File


from django.core.files.base import ContentFile

from django.core.files.base import ContentFile
import os
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

# def generate(request):
#     companies = BarcodeImage.objects.order_by().values_list('company', flat=True).distinct()
#     selected_company = request.POST.get('company')
#
#     if selected_company:
#         barcode_images = BarcodeImage.objects.filter(company=selected_company)
#         barcodes = []
#
#         # Count the occurrences of each barcode type
#         barcode_type_counts = {}
#
#         for barcode_image in barcode_images:
#             b_type = barcode_image.barcode_type
#             b_data = barcode_image.barcode_data
#
#             if not barcode_image.barcode_path:  # Check if barcode_path is null
#                 if b_type not in barcode_type_counts:
#                     barcode_type_counts[b_type] = 1
#                 else:
#                     barcode_type_counts[b_type] += 1
#
#                 if b_type == 'qrcode':
#                     qr = qrcode.QRCode(
#                         version=1,
#                         error_correction=qrcode.constants.ERROR_CORRECT_L,
#                         box_size=10,
#                         border=1,
#                     )
#                     qr.add_data(b_data)
#                     qr.make(fit=True)
#                     qr_file = qr.make_image(fill_color="black", back_color="white")  # Render QR code image
#
#                     with BytesIO() as qr_bytes:
#                         qr_file.save(qr_bytes, format='JPEG')  # Save the QR code image to a BytesIO object
#                         qr_bytes.seek(0)  # Reset the file pointer
#
#                         # Generate the image name with the barcode type and sequential number
#                         image_filename = f"{b_type}_{barcode_type_counts[b_type]}.jpg"
#
#                         barcode_image.barcode_path.save(image_filename, qr_bytes, save=True)  # Save the image to the model
#
#                 else:
#                     bar = barcode.get_barcode(name=b_type, code=b_data, writer=ImageWriter())
#                     barcode_file = bar.render()  # Create a PIL class image object
#
#                     with BytesIO() as barcode_bytes:
#                         barcode_file.save(barcode_bytes, format='JPEG')  # Save the barcode image to a BytesIO object
#                         barcode_bytes.seek(0)  # Reset the file pointer
#
#                         # Generate the image name with the barcode type and sequential number
#                         image_filename = f"{b_type}_{barcode_type_counts[b_type]}.jpg"
#
#                         barcode_image.barcode_path.save(image_filename, barcode_bytes, save=True)  # Save the image to the model
#
#                 # Generate and save the barcode image path
#                 relative_image_path = os.path.join('static/barcode_images', image_filename)
#                 barcode_image.barcode_path = relative_image_path
#                 barcode_image.save()
#
#             # Add barcode data, barcode type, and barcode image URL to the list
#             barcodes.append((barcode_image.barcode_data, barcode_image.barcode_type, barcode_image.image.url, barcode_image.barcode_path.url))
#
#         return render(request, 'generate_barcodes/generate.html', {
#             'companies': companies,
#             'selected_company': selected_company,
#             'barcode_images': barcode_images,
#             'barcodes': barcodes
#         })
#
#     else:
#         return render(request, 'generate_barcodes/generate.html', {
#             'companies': companies,
#             'selected_company': None
#         })


import os
from io import BytesIO
import qrcode
import barcode
from barcode.writer import ImageWriter
from django.shortcuts import render
#from .models import BarcodeImage

@login_required(login_url='user-login')
def generate(request):
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    companies = BarcodeImage.objects.order_by().values_list('company', flat=True).distinct()
    selected_company = request.POST.get('company')

    if selected_company:
        barcode_images = BarcodeImage.objects.filter(company=selected_company)
        barcodes = []

        # Count the occurrences of each barcode type
        barcode_type_counts = {}

        for barcode_image in barcode_images:
            b_type = barcode_image.barcode_type
            b_data = barcode_image.barcode_data

            if not barcode_image.barcode_path:  # Check if barcode_path is null
                if b_type not in barcode_type_counts:
                    barcode_type_counts[b_type] = 1
                else:
                    barcode_type_counts[b_type] += 1

                # Generate the image name with the barcode type and sequential number
                image_filename = f"{b_type}_{barcode_type_counts[b_type]}.png"
                existing_images = BarcodeImage.objects.filter(barcode_type=b_type, barcode_path__contains=image_filename)

                # Check if a file with the same name already exists
                while existing_images.exists():
                    barcode_type_counts[b_type] += 1
                    image_filename = f"{b_type}_{barcode_type_counts[b_type]}.png"
                    existing_images = BarcodeImage.objects.filter(barcode_type=b_type, barcode_path__contains=image_filename)

                if b_type == 'qrcode':
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=1,
                    )
                    qr.add_data(b_data)
                    qr.make(fit=True)
                    qr_file = qr.make_image(fill_color="black", back_color="white")  # Render QR code image

                    with BytesIO() as qr_bytes:
                        qr_file.save(qr_bytes, format='PNG')  # Save the QR code image to a BytesIO object
                        qr_bytes.seek(0)  # Reset the file pointer

                        barcode_image.barcode_path.save(image_filename, qr_bytes, save=True)  # Save the image to the model

                else:
                    bar = barcode.get_barcode(name=b_type, code=b_data, writer=ImageWriter())
                    barcode_file = bar.render()  # Create a PIL class image object

                    with BytesIO() as barcode_bytes:
                        barcode_file.save(barcode_bytes, format='PNG')  # Save the barcode image to a BytesIO object
                        barcode_bytes.seek(0)  # Reset the file pointer

                        barcode_image.barcode_path.save(image_filename, barcode_bytes, save=True)  # Save the image to the model

                # Generate and save the barcode image path
                relative_image_path = os.path.join('static/barcode_images', image_filename)
                barcode_image.barcode_path = relative_image_path
                barcode_image.save()

            # Add barcode data, barcode type, and barcode image URL to the list
            barcodes.append((barcode_image.barcode_data, barcode_image.barcode_type, barcode_image.image.url, barcode_image.barcode_path.url))

        return render(request, 'generate_barcodes/generate.html', {
            'companies': companies,
            'selected_company': selected_company,
            'barcode_images': barcode_images,
            'barcodes': barcodes,
            'count1':count1,
            'notification1':notification1,
        })

    else:
        return render(request, 'generate_barcodes/generate.html', {
            'companies': companies,
            'count1': count1,
            'notification1': notification1,
            'selected_company': None
        })

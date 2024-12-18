from django.shortcuts import get_object_or_404
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password,check_password


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import carSerializer
from rest_framework import status 


from .models import usersData,loginHistory,carsList,Bookings


@csrf_exempt
def registerData(request):
   if request.method == "POST":
      try:
         data=json.load(request)
         useData=data.get('data',{})

         name=useData['name']
         phone=useData['phone']
         email=useData['email']
         city=useData['city']
         userId=useData['userId']
         password=useData['password']

         passKey=make_password(password=password)

         data=usersData.objects.create(name=name,phone=phone,email=email,city=city,userId=userId,password=passKey)
         data.save()
         print('success')
         return HttpResponse(useData)


      except Exception as err:
         print(str(err))
         return HttpResponse('Error',err)
        
   
@csrf_exempt
def loginData(request):
   try:
      if request.method == "POST":
         data=json.load(request)
         useData=data.get('data',{})

         user=useData['userId']
         password=useData['password']

   
         data=usersData.objects.get(userId=user)
         passKey=data.password
         is_valid=check_password(password,passKey)

         if(is_valid):
             login=loginHistory.objects.create(userId=user,password=password,validate=True)
             login.save()
             
             user_data = {
            "name": data.name,
            "phone": data.phone,
            "email": data.email,
            "city": data.city,
            "userId": data.userId,
            "status":'Login Successfully...'
        }

             return JsonResponse(user_data)

         else:
            login=loginHistory.objects.create(userId=user,password=password,validate=False)
            login.save()
            print('login fail')
            return HttpResponse('Login Failed...')

   except Exception as err:
      print(str(err))
      return HttpResponse('Unknown User...')
        
class UploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = carSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('Data inserted Successfully...')
            return Response({"message": "Car details inserted successfully..."}, status=status.HTTP_201_CREATED)
        
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




def carList(request):
    try:
        queryset = carsList.objects.all()
        data = [
            {
                "id": item.carId,
                "name": item.ownerName,
                "phone": item.ownerPhone,
                "address": item.ownerAddress,
                "carModel":item.carModel,
                "carRent":item.carRent,
                "image": request.build_absolute_uri(item.carImage.url) if item.carImage and hasattr(item.carImage, 'url') else None,            }
            for item in queryset
        ]
        return JsonResponse(data, safe=False)

    except Exception as err:
        print(str(err))
        return HttpResponse(err)

@csrf_exempt
def bookings(request):
   if request.method=="POST":
      data=json.load(request)
      bookingData=data.get('data',{})

      userId = get_object_or_404(usersData, pk=bookingData["userId"])
      carId = get_object_or_404(carsList, pk=bookingData["carId"])

      booking = Bookings.objects.create(
                userId=userId,
                name=bookingData['name'],
                phone=bookingData['phone'],
                pickup=bookingData['pickup'],
                pickupDate=bookingData['pickup_date'],
                drop=bookingData['drop'],
                dropDate=bookingData['drop_date'],
                car=carId
            )
      booking.save()
      print('success')
      return HttpResponse("Your Car Booked Successfully...")
   return HttpResponse("Your Car Booking Failed...")

@csrf_exempt
def update(request):
   if request.method=="POST":
      data=json.load(request)
      updateData=data.get('data',{})

      passKey=make_password(password=updateData['password'])

      data=usersData.objects.get(userId=updateData['userId'])
      data.name=updateData['name']
      data.phone=updateData['phone']
      data.email=updateData['email']
      data.city=updateData['city']
      data.password=passKey

      data.save()      
      return HttpResponse("Your Data Updated Successfully...")
   return HttpResponse('Your Data Update Failed...')


@csrf_exempt
def history(request):

   try:
      if request.method=="POST":
         data=json.load(request)
         user=data.get('data',{})

         bookings = Bookings.objects.filter(userId__userId=user)  # Filter by userId ForeignKey

               # Serialize the booking data into a list
         history = []
         for booking in bookings:
            car_image_full_url = (
               request.build_absolute_uri(booking.car.carImage.url)
               if booking.car.carImage else None
            )
            history.append({
                     'name': booking.name,
                     'pickup': booking.pickup,
                     'pickupDate': booking.pickupDate,
                     'drop': booking.drop,
                     'dropDate': booking.dropDate,
                     'carModel': booking.car.carModel,  # Access car details from carsList
                     'carRent': booking.car.carRent,
                     'carImage': car_image_full_url,  # Full URL for car image
                     'bookingDate': booking.bookingDate,
                  })

         return JsonResponse({'history': history}, safe=False)
   except Exception as err:    
      return HttpResponse(f'Failed: {err}')
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import CarSerializer


# In-memory data structure
CARS = []
CAR_ID = 1


class CarListCreateAPIView(views.APIView):
    def get(self, request):
        return Response(CARS, status=status.HTTP_200_OK)


    def post(self, request):
        global CAR_ID
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            car_data = serializer.data
            car_data['id'] = CAR_ID
            CARS.append(car_data)
            CAR_ID += 1
            return Response(car_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetailAPIView(views.APIView):
    def get(self, request, id):
        car = next((car for car in CARS if car['id'] == id), None)
        if car:
            return Response(car, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    def put(self, request, id):
        car = next((car for car in CARS if car['id'] == id), None)
        if car:
            serializer = CarSerializer(data=request.data)
            if serializer.is_valid():
                car.update(serializer.data)
                return Response(car, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    def delete(self, request, id):
            global CARS
            CARS = [car for car in CARS if car['id'] != id]
            return Response(status=status.HTTP_204_NO_CONTENT)
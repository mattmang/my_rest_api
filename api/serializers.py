from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField(max_length=100)   # e.g. Z4
    brand = serializers.CharField(max_length=100)   # e.g. BMW
    registration_date = serializers.DateField()     # YYYY-MM-DD
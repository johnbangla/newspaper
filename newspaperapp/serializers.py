from rest_framework import serializers
from .models import English,Bangla,Video








        
class EnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = '__all__'

        
class BanglaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bangla
        fields = '__all__'
        
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'        
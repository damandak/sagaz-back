from rest_framework import routers,serializers,viewsets
from rest_framework.serializers import SerializerMethodField
from .models import Lake,LakeMeasurement
import math

class LakeSerializer(serializers.ModelSerializer):
    sagaz_id = serializers.CharField(max_length=100, required=True)
    image = serializers.SerializerMethodField()
    class Meta:
        model = Lake
        fields = ('id', 'image', 'name','sagaz_id','country','region','lat','lon','altitude','area','volume', 'description', 'station_status', 'current_alert_status', 'updated_at', 'last_data_date')

    def create(self, validated_data):
        old_lake = Lake.objects.filter(sagaz_id=validated_data['sagaz_id']).first()
        if old_lake is not None:
            if 'area' in validated_data:
                old_lake.area = validated_data['area']
            if 'volume' in validated_data:
                old_lake.volume = validated_data['volume']
            if 'station_status' in validated_data:
                old_lake.station_status = validated_data['station_status']
            old_lake.save()
            return old_lake
        return Lake.objects.create(**validated_data)

    def get_image(self, lake):
        request = self.context.get('request')
        if request is None:
            return "https://www.sagaz.org/media/" + lake.image.url if lake.image else ""
        image = lake.image.url if lake.image else ""
        return request.build_absolute_uri(image)

class LakeMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LakeMeasurement
        fields = ('lake', 'date', 'water_level', 'water_temperature', 'atmospheric_pressure', 'atmospheric_temperature', 'precipitation', 'alert_status')

    def create(self, validated_data):
        old_lake_m = LakeMeasurement.objects.filter(lake=validated_data['lake'], date=validated_data['date']).first()
        if old_lake_m is None:
            return LakeMeasurement.objects.create(**validated_data)
        else:
            if 'water_level' in validated_data:
                if not math.isnan(validated_data['water_level']):
                    old_lake_m.water_level = validated_data['water_level']
                else:
                    old_lake_m.water_level = None
            else:
                old_lake_m.water_level = None
            if 'water_temperature' in validated_data:
                if not math.isnan(validated_data['water_temperature']):
                    old_lake_m.water_temperature = validated_data['water_temperature']
                else:
                    old_lake_m.water_temperature = None
            else:
                old_lake_m.water_temperature = None
            if 'atmospheric_pressure' in validated_data:
                if not math.isnan(validated_data['atmospheric_pressure']):
                    old_lake_m.atmospheric_pressure = validated_data['atmospheric_pressure']
                else:
                    old_lake_m.atmospheric_pressure = None
            else:
                old_lake_m.atmospheric_pressure = None
            if 'atmospheric_temperature' in validated_data:
                if not math.isnan(validated_data['atmospheric_temperature']):
                    old_lake_m.atmospheric_temperature = validated_data['atmospheric_temperature']
                else:
                    old_lake_m.atmospheric_temperature = None
            else:
                old_lake_m.atmospheric_temperature = None
            if 'precipitation' in validated_data:
                if not math.isnan(validated_data['precipitation']):
                    old_lake_m.precipitation = validated_data['precipitation']
                else:
                    old_lake_m.precipitation = None
            else:
                old_lake_m.precipitation = None
            if 'alert_status' in validated_data:
                old_lake_m.alert_status = validated_data['alert_status']
            else:
                old_lake_m.alert_status = None
            old_lake_m.save()
            return old_lake_m

    def update(self, instance, validated_data):
        old_lake_m = LakeMeasurement.objects.filter(lake=validated_data['lake'], date=validated_data['date']).first()
        if old_lake_m is None:
            return LakeMeasurement.objects.create(**validated_data)
        else:
            if 'water_level' in validated_data:
                if not math.isnan(validated_data['water_level']):
                    old_lake_m.water_level = validated_data['water_level']
            if 'water_temperature' in validated_data:
                if not math.isnan(validated_data['water_temperature']):
                    old_lake_m.water_temperature = validated_data['water_temperature']
            if 'atmospheric_pressure' in validated_data:
                if not math.isnan(validated_data['atmospheric_pressure']):
                    old_lake_m.atmospheric_pressure = validated_data['atmospheric_pressure']
            if 'atmospheric_temperature' in validated_data:
                if not math.isnan(validated_data['atmospheric_temperature']):
                    old_lake_m.atmospheric_temperature = validated_data['atmospheric_temperature']
            if 'precipitation' in validated_data:
                if not math.isnan(validated_data['precipitation']):
                    old_lake_m.precipitation = validated_data['precipitation']
            if 'alert_status' in validated_data:
                old_lake_m.alert_status = validated_data['alert_status']
            old_lake_m.save()
            return old_lake_m

from rest_framework import serializers
from .models import *
from .serializers import *
from .models import (
    InwardtestQCinfo,
    InwardtestDimensional,
    Inwardtestvisulainspection,
    InwardtestreworkQty,
    InwardtestrejectQty
)

class InwardtestDimensionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardtestDimensional
        fields = '__all__'
        extra_kwargs = {
            'qc': {'required': False}
        }


class InwardtestVisualInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inwardtestvisulainspection
        fields = '__all__'
        extra_kwargs = {
            'qc': {'required': False}
        }

class InwardtestReworkQtySerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardtestreworkQty
        fields = '__all__'
        extra_kwargs = {
            'qc': {'required': False}
        }

class InwardtestRejectQtySerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardtestrejectQty
        fields = '__all__'
        extra_kwargs = {
            'qc': {'required': False}
        }


class InwardtestQCinfoSerializer(serializers.ModelSerializer):
    dimension_tests = InwardtestDimensionalSerializer(many=True, required=False)
    visual_tests = InwardtestVisualInspectionSerializer(many=True, required=False)
    rework_qty = InwardtestReworkQtySerializer(many=True, required=False)
    reject_qty = InwardtestRejectQtySerializer(many=True, required=False)

    class Meta:
        model = InwardtestQCinfo
        fields = '__all__'

    def create(self, validated_data):
        dimension_data = validated_data.pop('dimension_tests', [])
        visual_data = validated_data.pop('visual_tests', [])
        rework_data = validated_data.pop('rework_qty', [])
        reject_data = validated_data.pop('reject_qty', [])

        # Create Main QC
        qc = InwardtestQCinfo.objects.create(**validated_data)

        # Create Dimension Tests
        for dim in dimension_data:
            InwardtestDimensional.objects.create(qc=qc, **dim)

        # Create Visual Tests
        for vis in visual_data:
            Inwardtestvisulainspection.objects.create(qc=qc, **vis)

        # Create Rework Qty
        for rw in rework_data:
            InwardtestreworkQty.objects.create(qc=qc, **rw)

        # Create Reject Qty
        for rj in reject_data:
            InwardtestrejectQty.objects.create(qc=qc, **rj)

        return qc





# from rest_framework import serializers
# from .models import (
#     SubconJobworkQCInfo,
#     SubconJobworkDimensional,
#     SubconJobworkVisualInspection,
#     SubconJobworkReworkQty,
#     SubconJobworkRejectQty
# )


class SubconJobworkDimensionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubconJobworkDimensional
        fields = '__all__'
        read_only_fields = ['qc']


class SubconJobworkVisualInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubconJobworkvisulainspection
        fields = '__all__'
        read_only_fields = ['qc']


class SubconJobworkReworkQtySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubconJobworkreworkQty
        fields = '__all__'
        read_only_fields = ['qc']


class SubconJobworkRejectQtySerializer(serializers.ModelSerializer):
    class Meta:
        model =SubconJobworkrejectQty
        fields = '__all__'
        read_only_fields = ['qc']


class SubconJobworkQCInfoSerializer(serializers.ModelSerializer):
    dimension_tests = SubconJobworkDimensionalSerializer(many=True, required=False)
    visual_tests = SubconJobworkVisualInspectionSerializer(many=True, required=False)
    rework_items = SubconJobworkReworkQtySerializer(many=True, required=False)
    reject_items = SubconJobworkRejectQtySerializer(many=True, required=False)

    class Meta:
        model = SubconJobworkQCInfo
        fields = '__all__'


    def create(self, validated_data):

        dimension_data = validated_data.pop('dimension_tests', [])
        visual_data = validated_data.pop('visual_tests', [])
        rework_data = validated_data.pop('rework_items', [])
        reject_data = validated_data.pop('reject_items', [])

        qc = SubconJobworkQCInfo.objects.create(**validated_data)

        
        for item in dimension_data:
            SubconJobworkDimensional.objects.create(qc=qc, **item)

        for item in visual_data:
            SubconJobworkvisulainspection.objects.create(qc=qc, **item)

        for item in rework_data:
            SubconJobworkreworkQty.objects.create(qc=qc, **item)

        for item in reject_data:
            SubconJobworkrejectQty.objects.create(qc=qc, **item)

        return qc


    def update(self, instance, validated_data):

        dimension_data = validated_data.pop('dimension_tests', [])
        visual_data = validated_data.pop('visual_tests', [])
        rework_data = validated_data.pop('rework_items', [])
        reject_data = validated_data.pop('reject_items', [])

        # Update main fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        instance.dimension_tests.all().delete()
        instance.visual_tests.all().delete()
        instance.rework_items.all().delete()
        instance.reject_items.all().delete()

        for item in dimension_data:
            SubconJobworkDimensional.objects.create(qc=instance, **item)

        for item in visual_data:
            SubconJobworkvisulainspection.objects.create(qc=instance, **item)

        for item in rework_data:
            SubconJobworkreworkQty.objects.create(qc=instance, **item)

        for item in reject_data:
            SubconJobworkrejectQty.objects.create(qc=instance, **item)

        return instance
    



from rest_framework import serializers


class SalesReturnDimensionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesReturnDimensional
        fields = '__all__'
        read_only_fields = ("id", "qc")


class SalesReturnVisualInspectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesReturnvisulainspection
        fields = '__all__'
        read_only_fields = ("id", "qc")


class SalesReturnQcInfoSerializer(serializers.ModelSerializer):

    dimension_tests = SalesReturnDimensionalSerializer(many=True)
    visual_tests = SalesReturnVisualInspectionSerializer(many=True)

    class Meta:
        model = SalesReturnQcInfo
        fields = '__all__'


    def create(self, validated_data):

        dimension_data = validated_data.pop('dimension_tests')
        visual_data = validated_data.pop('visual_tests')

        qc = SalesReturnQcInfo.objects.create(**validated_data)

        for dim in dimension_data:
            SalesReturnDimensional.objects.create(qc=qc, **dim)

        for vis in visual_data:
            SalesReturnvisulainspection.objects.create(qc=qc, **vis)

        return qc
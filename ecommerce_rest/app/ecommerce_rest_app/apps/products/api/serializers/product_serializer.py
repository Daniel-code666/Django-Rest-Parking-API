from apps.products.models import *
from rest_framework import serializers
from apps.products.api.serializers.general_serializers import *

class ProductSerializer(serializers.ModelSerializer):
    #category_product = CategoryProductSerializer()

    class Meta:
        model = Product
        exclude = ('state',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['measure_unit'] = MeasureUnitSerializer(instance.measure_unit).data
        ret['category_product'] = CategoryProductSerializer(instance.category_product).data
        return ret 
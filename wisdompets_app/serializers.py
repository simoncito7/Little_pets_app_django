from rest_framework import serializers

from wisdompets_app.models import Pet

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'submitter')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['is_on_sale'] = instance.is_on_sale()
        # data['current_price'] = instance.current_price()
        return data
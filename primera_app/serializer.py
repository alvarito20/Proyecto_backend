from rest_framework import serializers
from .models import Modelo_1
class Modelo_1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo_1
# fields = ('fullname','languaje','is_active’) acápodemos traer cualquier atributo o campo del modelo.
fields = '__all__'
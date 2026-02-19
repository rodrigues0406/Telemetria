from rest_framework import serializers
from models import (
    Marca,
    Modelo,
    UnidadeMedida,
    Veiculo,
    Medicao,
    MedicaoVeiculo
)

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

        

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'

        

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeMedida
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    marca_nome = serializers.ReadOnlyField(source='marca.nome')
    modelo_nome = serializers.ReadOnlyField(source='modelo.nome')

class Meta:
        model = Veiculo
        fields = [
            'id',
            'descricao',
            'marca',
            'marca_nome',
            'modelo',
            'modelo_nome',
            'ano',
            'horimetro'
        ]

        
class MedicaoSerializer(serializers.ModelSerializer):
    unidade_nome = serializers.ReadOnlyField(source='unidade_medida.nome')
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = Medicao
        fields = [
            'id',
            'tipo',
            'tipo_display',
            'unidade_medida',
            'unidade_nome'
        ]

        
class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    veiculo_descricao = serializers.ReadOnlyField(source='veiculo.descricao')
    medicao_tipo = serializers.ReadOnlyField(source='medicao.get_tipo_display')

    class Meta:
        model = MedicaoVeiculo
        fields = [
            'id',
            'veiculo',
            'veiculo_descricao',
            'medicao',
            'medicao_tipo',
            'data',
            'valor'
        ]

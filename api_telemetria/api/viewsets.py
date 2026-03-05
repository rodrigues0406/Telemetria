from rest_framework import viewsets
from api_telemetria import models
from api_telemetria.api.serializers import (
    MarcaSerializer,
    ModeloSerializer,
    UnidadeMedidaSerializer,
    VeiculoSerializer,
    MedicaoSerializer,
    MedicaoVeiculoSerializer,
)
from drf_yasg.utils import swagger_auto_schema

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = models.Marca.objects.all()
    serializer_class = MarcaSerializer

    @swagger_auto_schema(
        operation_description= "retorna todas as informações do tipo de marca",
        responses={200: MarcaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_description="Cria um novo tipo de marca",
        responses={201:MarcaSerializer(many=True)}
    )
      
    def create(self, request, *args, **kwargs):
          return super().create(request, *args, **kwargs)
      
    @swagger_auto_schema(
        operation_description="Retorna o registro de tipo de marca conforme o ID informado",
        responses={200: MarcaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
          return super().retrieve(request, *args, **kwargs)
      
    
    @swagger_auto_schema(
        operation_description="Atualiza o registro de tipo de marca conforme o Id ",
        responses={201: MarcaSerializer(many=True)}
    
    )
    def update(self, request, *args, **kwargs):
          return super().update(request, *args, **kwargs)
    


    @swagger_auto_schema(
        operation_description='o produto foi deletado',
        responses={201: MarcaSerializer(many=True)})
       
    def destroy(self, request, *args, **kwargs):
          return super().destroy(request, *args, **kwargs)  
   

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = models.Modelo.objects.all()
    serializer_class = ModeloSerializer
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de tipo de marca conforme o id Informado ",
        responses={200: ModeloSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna todas as informações de tipo de modelos ",
        responses={201:ModeloSerializer(many=True)}
    )
      
    def create(self, request, *args, **kwargs):
          return super().create(request, *args, **kwargs)
      
    @swagger_auto_schema(
        operation_description="Cria um novo tipo de modelo",
        responses={200: ModeloSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
          return super().retrieve(request, *args, **kwargs)
      
    
    @swagger_auto_schema(
        operation_description="retorna o registro de tipo de modelo conforme o Id ",
        responses={201: ModeloSerializer(many=True)}
    
    )
    def update(self, request, *args, **kwargs):
          return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description='o produto foi deletado',
        responses={201: ModeloSerializer(many=True)}
        )
    def destroy(self, request, *args, **kwargs):
          return super().destroy(request, *args, **kwargs)


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = models.UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer

    @swagger_auto_schema(
        operation_description="retorna todas informações da unidade de medida",
        responses={200: UnidadeMedidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria um novo tipo de unidade de medida",
        responses={201: UnidadeMedidaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de tipo de unidade de medida conforme o ID informado",
        responses={200: UnidadeMedidaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Atualiza o registro de tipo de unidade de medida conforme o ID informado",
        responses={200: UnidadeMedidaSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='o produto foi deletado',
        responses={204: UnidadeMedidaSerializer(many=True)})
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    @swagger_auto_schema(
        operation_description="retorna todas as informações do tipo de veiculo",
        responses={200: VeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria um novo tipo de veiculo",
        responses={201: VeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de tipo de veiculo conforme o ID informado",
        responses={200: VeiculoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de tipo de veiculo conforme o ID informado",
        responses={200: VeiculoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="o veiculo foi deletado",
        responses={204: VeiculoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class MedicaoViewSet(viewsets.ModelViewSet):
    queryset = models.Medicao.objects.all()
    serializer_class = MedicaoSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas as informações de tipos de medição",
        responses={200: MedicaoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo tipo de medição",
        responses={201: MedicaoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de tipo de medição conforme o ID informado",
        responses={200: MedicaoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de medição conforme o ID informado",
        responses={200: MedicaoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="o tipo de medição foi deletado",
        responses={204: MedicaoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class MedicaoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.MedicaoVeiculo.objects.all()
    serializer_class = MedicaoVeiculoSerializer

    @swagger_auto_schema(
        operation_description="Retorna todos os registros de medição de veiculo",
        responses={200: MedicaoVeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria um novo registro de medição de veiculo",
        responses={201: MedicaoVeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de medição de veiculo conforme o ID informado",
        responses={200: MedicaoVeiculoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de medição de veiculo conforme o ID informado",
        responses={200: MedicaoVeiculoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="o registro de medição foi deletado",
        responses={204: MedicaoVeiculoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
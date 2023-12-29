from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.views import APIView
from .serializers import ProductSerializer, StoreSerializer
from .models import Product, Store


class ProductAPIView(APIView):
    # define queryset
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            queryset = Product.objects.all()
            return Response({'products': ProductSerializer(queryset, many=True).data})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": f"Product with ID '{pk}' was not found"}, status=HTTP_404_NOT_FOUND)

        return Response({'product': ProductSerializer(instance=instance).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'product': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "PUT is not allowed"}, status=HTTP_405_METHOD_NOT_ALLOWED)

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "ID was not found"}, status=HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'product': serializer.data})


class StoreAPIView(APIView):
    # define queryset
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            queryset = Store.objects.all()
            return Response({'stores': StoreSerializer(queryset, many=True).data})
        
        try:
            inst = Store.objects.get(pk=pk)
        except:
            return Response({"error": "Wrong Store ID"}, status=HTTP_404_NOT_FOUND)
        return Response({'store': StoreSerializer(instance=inst).data})

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'store': serializer.data})

    def patch(self, request, *args, **kwargs):
                
        pk = kwargs.get('pk')
        if pk is None:
            return Response({'error': 'Method PUT is not allowed'}, status=HTTP_405_METHOD_NOT_ALLOWED)
        
        try:
            inst = Store.objects.get(pk=pk)
        except:
            return Response({"error": "Wrong Store ID"}, status=HTTP_404_NOT_FOUND)

        current_values = StoreSerializer(instance=inst).data
        current_values |= request.data
        # for k, v in request.data:
        #     current_values[k] = v
        serializer = StoreSerializer(data=current_values, instance=inst)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'store': serializer.data})


class StoreProductAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            return Response({'error': 'PK was not found'}, status=HTTP_405_METHOD_NOT_ALLOWED)
        
        try:
            inst = Store.objects.get(pk=pk)
        except:
            return Response({"error": "Wrong Store ID"}, status=HTTP_404_NOT_FOUND)
        
        return Response({'products': ProductSerializer(inst.products, many=True).data})

    # def post(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     if pk is None:
    #         return Response({'error': 'PK was not found'}, status=HTTP_405_METHOD_NOT_ALLOWED)
        
    #     try:
    #         inst = Store.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Wrong Store ID"}, status=HTTP_404_NOT_FOUND)
        
        
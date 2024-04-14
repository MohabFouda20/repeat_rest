from . models import Product



from rest_framework import generics
from . serializers import productSerializer

# Create your views here.
class productDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    
product_view = productDetailAPIView.as_view() # this is a class based view
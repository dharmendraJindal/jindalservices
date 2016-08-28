from rest_framework import routers

from product.views.ProductViewSet import ProductViewSet
from product.views.ProductCategoryViewSet import ProductCategoryViewSet

router = routers.SimpleRouter()

router.register(r'categories', ProductCategoryViewSet, base_name='categories')
router.register(r'products', ProductViewSet, base_name='product')

urlpatterns = router.urls

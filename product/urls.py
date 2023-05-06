from .views import CategoryViewSet, ProductViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('categories', CategoryViewSet)
router.register('products', ProductViewset)

urlpatterns = [

]
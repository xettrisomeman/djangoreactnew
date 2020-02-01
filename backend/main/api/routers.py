from rest_framework import routers

from .views import PostViewSet

router = routers.DefaultRouter()

router.register('' , PostViewSet , basename='postview')


urlpatterns = router

from rest_framework import routers

from . import views


router = routers.SimpleRouter()

router.register(r"", views.TagViewSet)

urlpatterns = router.urls

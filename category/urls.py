from rest_framework.routers import DefaultRouter
from category.views import CategoryViewSet


class NoTrailingSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(NoTrailingSlashRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = ""


router = NoTrailingSlashRouter()
router.register("v1/close/category", CategoryViewSet, basename="category")

urlpatterns = router.urls

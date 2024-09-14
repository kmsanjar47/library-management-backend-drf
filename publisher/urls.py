from rest_framework.routers import DefaultRouter
from publisher.views import PublisherApiView


class NoTrailingSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(NoTrailingSlashRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = ""


router = NoTrailingSlashRouter()
router.register("v1/close/publisher", PublisherApiView, basename="publisher")

urlpatterns = router.urls

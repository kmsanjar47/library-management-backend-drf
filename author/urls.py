
from rest_framework.routers import DefaultRouter

from author.views import AuthorAPIView


class NoTrailingSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(NoTrailingSlashRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = ""


router = NoTrailingSlashRouter()
router.register("v1/close/author", AuthorAPIView, basename="author")

urlpatterns = router.urls


from rest_framework.routers import DefaultRouter
from book.views import BookAPIView


class NoTrailingSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(NoTrailingSlashRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = ""


router = NoTrailingSlashRouter()
router.register("v1/close/book", BookAPIView, basename="book")

urlpatterns = router.urls

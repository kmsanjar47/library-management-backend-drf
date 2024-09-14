from rest_framework.routers import DefaultRouter
from loan.views import LoanApiView


class NoTrailingSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(NoTrailingSlashRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = ""


router = NoTrailingSlashRouter()
router.register("v1/close/loan", LoanApiView, basename="loan")

urlpatterns = router.urls

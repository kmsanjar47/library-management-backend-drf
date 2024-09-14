from rest_framework.routers import DefaultRouter
from branch.views import BranchAPIView


class NoTrailingSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(NoTrailingSlashRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = ""


router = NoTrailingSlashRouter()
router.register("v1/close/branch", BranchAPIView, basename="branch")

urlpatterns = router.urls

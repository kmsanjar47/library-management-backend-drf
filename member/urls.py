from rest_framework.routers import DefaultRouter
from member.views import MemberApiView

class NoTrailingSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(NoTrailingSlashRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = ""


router = NoTrailingSlashRouter()
router.register("v1/close/member", MemberApiView, basename="member")

urlpatterns = router.urls

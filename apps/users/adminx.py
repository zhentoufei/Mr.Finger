from .models import UserProfile
import xadmin

# class UserProfileAdmin(object):
#     pass
#
# xadmin.site.register(UserProfile, UserProfileAdmin)
from .models import UserAbout
import xadmin


class AboutAdmin(object):
    list_display = ['about', 'date_time']
    style_fields = {"about":"ueditor"}



xadmin.site.register(UserAbout, AboutAdmin)

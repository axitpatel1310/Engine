from django.contrib import admin
from .models import Search,Ads,user,UserActivity,Ads_3rd_Party,gen_notification,per_notification,contact_us
# Register your models here.
admin.site.register(Search)
admin.site.register(Ads)
admin.site.register(user)
admin.site.register(UserActivity)
admin.site.register(Ads_3rd_Party)
admin.site.register(gen_notification)
admin.site.register(per_notification)
admin.site.register(contact_us)
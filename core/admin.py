from django.contrib import admin
from core.models import Profiles ,  Posts ,Follows, Likes

admin.site.register(Profiles);
admin.site.register(Posts);
admin.site.register(Follows);
admin.site.register(Likes);

# Register your models here.

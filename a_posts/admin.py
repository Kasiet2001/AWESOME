from django.contrib import admin
from .models import *


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(LikedPost)
admin.site.register(LikedComment)
admin.site.register(LikedReply)
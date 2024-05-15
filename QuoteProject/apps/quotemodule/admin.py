from django.contrib import admin
from .models import Quote
from django.contrib.auth.models import User,Group

admin.site.register(Quote)
admin.site.unregister(User)
admin.site.unregister(Group)

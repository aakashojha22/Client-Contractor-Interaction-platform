from django.contrib import admin

# Register your models here.
from .models import ClientLogin,Bid
# Register your models here.
admin.site.register(ClientLogin)
admin.site.register(Bid)
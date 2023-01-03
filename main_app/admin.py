from django.contrib import admin
from .models import Bear, Feeding, Toy
# Register your models here.
admin.site.register(Bear)
admin.site.register(Feeding)
admin.site.register(Toy)
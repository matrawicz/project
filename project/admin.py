from django.contrib import admin

# Register your models here.
from project.models import *

admin.site.register(WorkStation)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(DiscountSupplier)
admin.site.register(DiscountCustomer)
admin.site.register(Material)
admin.site.register(DocumentSupplier)
admin.site.register(Good)
admin.site.register(DocumentCustomer)
admin.site.register(GoodMaterial)
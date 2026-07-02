from django.contrib import admin
from orders.models import Orders,OrderedItems

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        "owner",
        "order_status",
    ]
    search_fields = (
        "owner__user__username",
        "id",
    )

admin.site.register(Orders,OrderAdmin)
admin.site.register(OrderedItems)


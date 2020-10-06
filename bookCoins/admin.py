from django.contrib import admin
from .models import OrderCoin, OrderChapter, OrderChapterLineItem


class OrderCoinAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date',
              'full_name', 'email', 'phone_number', 'town_or_city',
              'street_address1', 'street_address2', 'county', 'country',
              'coins', 'stripe_pid')

    list_display = ('order_number', 'date', 'user_profile',
                    'full_name', 'coins',)

    ordering = ('-date',)


class OrderChapterLineItemAdminInline(admin.TabularInline):
    model = OrderChapterLineItem
    readonly_fields = ('chapter_no', 'book', 'lineitem_total',)


class OrderChapterAdmin(admin.ModelAdmin):
    inlines = (OrderChapterLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'grand_total',)

    fields = ('order_number', 'user_profile', 'date',)

    list_display = ('order_number', 'user_profile',
                    'date', 'grand_total',)

    ordering = ('-date',)


admin.site.register(OrderCoin, OrderCoinAdmin)
admin.site.register(OrderChapter, OrderChapterAdmin)
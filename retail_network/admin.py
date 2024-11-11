from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from retail_network.models import Product, Network


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', "release_date")


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    "country",
                    'city',
                    'street',
                    'house_number',
                    'supplier_link',
                    )

    def clear_debt(self, request, queryset):
        """
        Очищает задолженность перед поставщиком у выбранных объектов.
        """
        updated_count = queryset.update(debt_to_supplier=0.00)  # Обновляем задолженность
        self.message_user(request, f"Задолженность очищена для {updated_count} объектов.")

    clear_debt.short_description = "Очистить задолженность перед поставщиком"  # Описание действия в админке

    actions = [clear_debt]

    def supplier_link(self, obj):
        """
        Генерирует ссылку на страницу поставщика.
        """
        if obj.supplier:
            link = reverse('admin:retail_network_network_change', args=[obj.supplier.id])
            return format_html('<a href=%s>%s(%s)</a>' % (link, obj.supplier.name, obj.supplier.country))
        return None

    supplier_link.short_description = 'Поставщик'

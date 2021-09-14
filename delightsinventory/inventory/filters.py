import django_filters

from .models import Purchase

class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = ('menu_item', 'date', 'time')
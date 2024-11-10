from django.db import models
from django.db.models import PositiveIntegerField


class Product(models.Model):
    """
    Модель для представления продукта.
    """

    title = models.CharField(max_length=20, verbose_name="название")
    model = models.CharField(max_length=50, verbose_name="модель")
    release_date = models.DateField(verbose_name="дата выхода на рынок")

    def __str__(self):
        """
        Возвращает строковое представление объекта Product.
        """
        return f"{self.title} - {self.model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Network(models.Model):
    """
    Модель для представления звена сети.
    """

    LEVELS = {
        ("0", "Завод"),
        ("1", "Розничная сеть"),
        ("2", "Индивидуальный предприниматель"),
    }
    name = models.CharField(max_length=50, verbose_name="название")
    email = models.EmailField(unique=True, verbose_name="почта")
    country = models.CharField(max_length=50, verbose_name="страна")
    city = models.CharField(max_length=50, verbose_name="город")
    street = models.CharField(max_length=100, verbose_name="улица")
    house_number = PositiveIntegerField(max_length=10, verbose_name="номер дома")
    levels = models.IntegerField(choices=LEVELS, verbose_name="уровень сеть", null=True, blank=True)
    supplier = models.ForeignKey("self", verbose_name="поставщик", on_delete=models.SET_NULL, null=True, blank=True)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="задолженность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    product = models.ManyToManyField(Product, verbose_name="продукты", related_name="network_nodes")

    def __str__(self):
        """
        Возвращает строковое представление объекта Network.
        """
        return f"{self.name}, {self.email}, {self.country}"

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

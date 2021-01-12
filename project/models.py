from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse

from project.validators import validate_norm, validate_symbols_nip, validate_len_nip, validate_value_discount, \
    validate_len_index


class WorkStation(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa stanowiska pracy', null=False, unique=True)
    norm = models.PositiveIntegerField(verbose_name='Dzienna norma produkcyjna', validators=[validate_norm])

    def __str__(self):
        return f'{self.name} - norma wynosi: {self.norm}'

    def get_delete_url(self):
        return reverse('deleteWorkStation', args=(self.pk,))

    def get_update_url(self):
        return reverse('updateWorkStation', args=(self.pk,))


class Supplier(models.Model):
    INDUSTY = [
        ('BHP', 'BHP'),
        ('SPA', 'SPAWALNICTWO'),
        ('SZL', 'SZLIFIERSTWO'),
        ('AUT', 'AUTOMATYKA PRZEMYSŁOWA')
    ]

    name = models.CharField(max_length=64, unique=True, null=False, verbose_name='Nazwa')
    address = models.TextField(null=False, verbose_name='Adres')
    nip = models.CharField(max_length=10, unique=True, null=False, verbose_name='NIP', help_text='Wprowadź 10 liczb w ciągu', validators=[validate_len_nip, validate_symbols_nip])
    industy = models.CharField(max_length=3, verbose_name='Branża', null=True, choices=INDUSTY)

    def __str__(self):
        return f'{self.name} {self.nip}'


    def get_delete_url(self):
        return reverse('deleteSupplier', args=(self.pk,))

    def get_update_url(self):
        return reverse('updateSupplier', args=(self.pk,))




class Customer(models.Model):
    INDUSTY = [
        ('BHP', 'BHP'),
        ('SPA', 'SPAWALNICTWO'),
        ('SZL', 'SZLIFIERSTWO'),
        ('AUT', 'AUTOMATYKA PRZEMYSŁOWA'),
        ('HAN', 'HANDEL PRZEMYSŁOWY'),
        ('BUD', 'BUDOWNICTWO')
    ]

    name = models.CharField(max_length=64, unique=True, null=False, verbose_name='Nazwa')
    address = models.TextField(null=False, verbose_name='Adres')
    delivery_address = models.TextField(null=False, verbose_name='Adres dostawy')
    nip = models.CharField(max_length=10, unique=True, null=False, verbose_name='NIP',
                           help_text='Wprowadź 10 liczb w ciągu', validators=[validate_len_nip, validate_symbols_nip])
    industy = models.CharField(max_length=3, verbose_name='Branża', null=True, choices=INDUSTY)

    def __str__(self):
        return f'{self.name} {self.nip}'

    def get_delete_url(self):
        return reverse('deleteCustomer', args=(self.pk,))

    def get_update_url(self):
        return reverse('updateCustomer', args=(self.pk,))


class DiscountSupplier(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, verbose_name='Nazwa rabatu')
    value_percent = models.PositiveIntegerField(null=False, verbose_name='Wartość procentowa', help_text='Ustalona wartość z dostawcą', validators=[validate_value_discount])
    supplier = models.OneToOneField(Supplier, verbose_name='Rabat dla dostawcy', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} dla {self.supplier} o wartości {self.value_percent}%'

    def get_delete_url(self):
        return reverse('deleteDiscountSupplier', args=(self.pk,))

    def get_update_url(self):
        return reverse('updateDiscountSupplier', args=(self.pk,))


class DiscountCustomer(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, verbose_name='Nazwa rabatu')
    value_percent = models.PositiveIntegerField(null=False, verbose_name='Wartość procentowa',
                                                help_text='Nie powinna przekraczać 35', validators=[validate_value_discount])
    customer = models.OneToOneField(Customer, verbose_name='Rabat dla klienta', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} dla {self.customer} o wartości {self.value_percent}%'

    def get_delete_url(self):
        return reverse('deleteDiscountCustomer', args=(self.pk,))

    def get_update_url(self):
        return reverse('updateDiscountCustomer', args=(self.pk,))


class Material(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, verbose_name='Nazwa pozycji')
    index = models.PositiveBigIntegerField(unique=True, null=False, verbose_name='Indeks', validators=[validate_len_index])
    description = models.TextField(null=True, verbose_name='Opis szczegółowy')
    quantity = models.PositiveBigIntegerField(null=False, default=0, verbose_name='Ilość na stanie magazynowym', help_text='Kontroluj ilość systemową ze stanem fizycznym!')
    supplier = models.ForeignKey(Supplier, null=True, verbose_name='Dostawca', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.index} | {self.name} | stan: {self.quantity} | dostawca: {self.supplier}'

    def get_delete_url(self):
        return reverse('deleteMaterial', args=(self.pk,))

    def get_update_url(self):
        return reverse('updateMaterial', args=(self.pk,))


class DocumentSupplier(models.Model):
    # DESTINATION = [
    #     ('REC', 'REKLAMACJA'),
    #     ('PUR', 'ZAKUP'),
    #     ('TES', 'TESTY'),
    #     ('GRA', 'GRATIS')
    # ]
    number = models.CharField(max_length=12, unique=True, null=False, verbose_name='Numer dokumentu') #ustawić funkcję
    destination = models.CharField(max_length=24, null=False, verbose_name='Przeznaczenie')
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.PROTECT, verbose_name='Dostawca')
    materials = models.ManyToManyField(Material, verbose_name='Pozycje na dokumencie')

    def __str__(self):
        return f'{self.number}'

    def get_delete_url(self):
        return reverse('deleteDocumentSupplier', args=(self.pk,))

    def get_update_url(self):
        return reverse('updateDocumentSupplier', args=(self.pk,))


class Good(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, verbose_name='Nazwa pozycji')
    index = models.PositiveBigIntegerField(unique=True, null=False, verbose_name='Indeks')
    description = models.TextField(null=True, verbose_name='Opis szczegółowy')
    quantity = models.PositiveBigIntegerField(null=False, default=0, verbose_name='Ilość na stanie magazynowym',
                                           help_text='Kontroluj ilość systemową ze stanem fizycznym!')
    material = models.ManyToManyField(Material, through='GoodMaterial')

    def __str__(self):
        return f'{self.index} | {self.name} | stan: {self.quantity}'

    def get_delete_url(self):
        return reverse('deleteGood', args=(self.pk,))

    def get_update_url(self):
        return reverse('updateGood', args=(self.pk,))

    def get_tryproduce_url(self):
        return reverse('tryProduce', args=(self.pk,))


class DocumentCustomer(models.Model):
    # DESTINATION = [
    #     ('REC', 'REKLAMACJA'),
    #     ('PUR', 'ZAKUP'),
    #     ('TES', 'TESTY'),
    #     ('GRA', 'GRATIS')
    # ]
    number = models.CharField(max_length=12, unique=True, null=False, verbose_name='Numer dokumentu') #ustawić funkcję
    destination = models.CharField(max_length=24, null=False, verbose_name='Przeznaczenie')
    customer = models.ForeignKey(Customer, null=True, on_delete=models.PROTECT, verbose_name='Klient')
    good = models.ManyToManyField(Good, verbose_name='Pozycje na dokumencie')

    def __str__(self):
        return f'{self.number}'

    def get_delete_url(self):
        return reverse('deleteDocumentCustomer', args=(self.pk,))

    def get_update_url(self):
        return reverse('updateDocumentCustomer', args=(self.pk,))


class GoodMaterial(models.Model):
    good = models.ForeignKey(Good, verbose_name='Produkt', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, verbose_name='Element', on_delete=models.PROTECT)
    needed = models.PositiveIntegerField(default=1, null=False, verbose_name='Potrzeba')


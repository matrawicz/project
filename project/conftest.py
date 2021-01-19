import random

import pytest
from django.contrib.auth.models import User

from django.test import Client

from project.models import WorkStation, Supplier, DiscountSupplier, Customer, DiscountCustomer, Material, \
    DocumentSupplier, Good, GoodMaterial, DocumentCustomer


@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def user():
    user = User.objects.create(username='xxx12345')
    user.set_password('xxx12345')
    user.save()
    return user


@pytest.fixture
def workstation():
    for i in range(8):
        WorkStation.objects.create(name=f'WS number {i}', norm=f'{i*10}')
    return WorkStation.objects.all()


@pytest.fixture
def supplier():
    for i in range(7):
        choices = ['BHP', 'SPA', 'SZL', 'AUT']
        random.shuffle(choices)
        nip = f'10000{i+10}000'
        industy = choices[0]
        Supplier.objects.create(name=f'Supplier {i} XYZ', address=f'New York, LongStreet {i*10}', nip=nip, industy=industy)
    return Supplier.objects.all()


@pytest.fixture
def discountsupplier(supplier):
    for i in range(1, 6):
        DiscountSupplier.objects.create(name=f'Discount No.{i}', value_percent=i*2, supplier=supplier[i])
    return DiscountSupplier.objects.all()


@pytest.fixture
def customer():
    for i in range(7):
        choices = ['BHP', 'SPA', 'SZL', 'AUT', 'HAN', 'BUD']
        random.shuffle(choices)
        nip = f'2000{i+10}0000'
        industy = choices[0]
        Customer.objects.create(name=f'Customer No.{i}', address=f'NewStreet {i*13}', delivery_address=f'OldStreet {i*6}',
                                nip=nip, industy=industy)
    return Customer.objects.all()


@pytest.fixture
def discountcustomer(customer):
    for i in range(1, 6):
        DiscountCustomer.objects.create(name=f'Discount No.{i}', value_percent=i*2, customer=customer[i])
    return DiscountCustomer.objects.all()


@pytest.fixture
def material(supplier):
    for i in range(80):
        supplier_id = [1,2,3,4,5,6]
        random.shuffle(supplier_id)
        index = f'30{i+10}000000'
        Material.objects.create(name=f'Material no {i+1}', index=index, description=f'Something {i}', quantity=i*2, supplier=supplier[supplier_id[3]])
    return Material.objects.all()


@pytest.fixture
def documentsupplier(supplier, material):
    for i in range(15):
        supplier_id = [1, 2, 3, 4, 5, 6]
        destination = ['REC', 'PUR', 'TES', 'GRA']
        random.shuffle(supplier_id)
        random.shuffle(destination)
        supplier_obj = supplier[supplier_id[0]]
        materials = Material.objects.filter(supplier=supplier_obj.id)
        if len(materials) == 0:
            DocumentSupplier.objects.create(number=f'{i+3}/2021/SD', destination=destination[0], supplier=supplier_obj)
        elif len(materials) > 0:
            document = DocumentSupplier.objects.create(number=f'{i + 3}/2021/SD', destination=destination[0],
                                            supplier=supplier_obj)
            document.materials.set([materials[0].id])
    return DocumentSupplier.objects.all()


@pytest.fixture
def good(material):
    for i in range(6):
        materials = [material[i+1].id, material[i+2].id, material[i+3].id, material[i+5].id]
        index = f'500{i+10}00000'
        good = Good.objects.create(name=f'Good No{i}', index=index, description=f'Desc about element{i}', quantity=i)
        for j in materials:
            GoodMaterial.objects.create(good=good, material=Material.objects.get(id=j),
                                        needed=5)
    return Good.objects.all(), GoodMaterial.objects.all()


@pytest.fixture
def documentcustomer(customer, good):
    for i in range(15):
        customer_id = [1, 2, 3, 4, 5, 6]
        destination = ['REC', 'PUR', 'TES', 'GRA']
        random.shuffle(customer_id)
        random.shuffle(destination)
        customer_obj = customer[customer_id[0]]
        products = good[0]
        goods = [products[0], products[2], products[4]]
        document = DocumentCustomer.objects.create(number=f'{i + 3}/2021/CD', destination=destination[0],
                                            customer=customer_obj)
        document.good.set(goods)
    return DocumentCustomer.objects.all()


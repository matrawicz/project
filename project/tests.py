import pytest
from django.test import TestCase

# Create your tests here.

from django.urls import reverse

from project.models import WorkStation, Supplier, DiscountSupplier, Customer, Material, DocumentSupplier, Good, \
    DocumentCustomer


#1.
@pytest.mark.django_db
def test_mainpage(client):
    """

    :param client:
    :return: assert result.status_code == 200
    """
    result = client.get('')
    assert result.status_code == 200

#2.
@pytest.mark.django_db
def test_mainpage1(client, user):
    """

    :param client:
    :param user:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get('')
    assert result.status_code == 200

#3.
@pytest.mark.django_db
def test_mainpage2(client):
    """

    :param client:
    :return: assert len(result.content) > 0
    """
    result = client.get('')
    assert len(result.content) > 0

#4.
@pytest.mark.django_db
def test_createWorkStationGet(client, user):
    """

    :param client:
    :param user:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(reverse('createWorkStation'))
    assert result.status_code == 200

#5.
@pytest.mark.django_db
def test_createWorkStationPost(client, user):
    """

    :param client:
    :param user:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    workstation = {'name':'Stacja1', 'norm':500}
    result = client.post(reverse('createWorkStation'),workstation)
    assert result.status_code == 302

#6.
@pytest.mark.django_db
def test_createWorkStationPost1(client):
    """

    :param client:
    :return: assert result.status_code == 302
    """
    workstation = {'name': 'Stacja2', 'norm':400}
    result = client.post(reverse('createWorkStation'), workstation)
    assert result.status_code == 302

#7.
@pytest.mark.django_db
def test_listWorkStation(client, workstation):
    """

    :param client:
    :param workstation:
    :return: assert result.status_code == 200
    """
    result = client.get('/erp/list_work_position/')
    assert result.status_code == 200

#8.
@pytest.mark.django_db
def test_listWorkStation1(client, workstation):
    """

    :param client:
    :param workstation:
    :return: assert workstation.count() == len(result.context['object_list'])
    """
    result = client.get('/erp/list_work_position/')
    assert workstation.count() == len(result.context['object_list'])

#9.
@pytest.mark.django_db
def test_listWorkStation2(client, workstation):
    """

    :param client:
    :param workstation:
    :return: assert obj in workstation
    """
    result = client.get('/erp/list_work_position/')
    for obj in result.context['object_list']:
        assert obj in workstation

#10.
@pytest.mark.django_db
def test_deleteWorkStation(client, workstation):
    """

    :param client:
    :param workstation:
    :return: assert result.status_code == 302
    """
    result = client.get(f'/erp/delete_work_position/{workstation[1].id}/')
    assert result.status_code == 302

#11.
@pytest.mark.django_db
def test_deleteWorkStation1(client, user, workstation):
    """

    :param client:
    :param user:
    :param workstation:
    :return:  assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(f'/erp/delete_work_position/{workstation[5].id}/')
    assert result.status_code == 200

#12.
@pytest.mark.django_db
def test_deleteWorkStation2(client, user, workstation):
    """

    :param client:
    :param user:
    :param workstation:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    result = client.post(f'/erp/delete_work_position/{workstation[4].id}/')
    assert result.status_code == 302

#13.
@pytest.mark.django_db
def test_deleteWorkStation3(client, user, workstation):
    """

    :param client:
    :param user:
    :param workstation:
    :return: assert len(WorkStation.objects.filter(pk=number)) == 0
    """
    client.force_login(user)
    number = workstation[2].id
    client.post(f'/erp/delete_work_position/{number}/')
    assert len(WorkStation.objects.filter(pk=number)) == 0

#14.
@pytest.mark.django_db
def test_updateWorkStation(client, workstation):
    """

    :param client:
    :param workstation:
    :return: assert result.status_code == 302
    """
    number = workstation[0].id
    result = client.get(f'/erp/update_work_position/{number}/')
    assert result.status_code == 302

#15.
@pytest.mark.django_db
def test_updateWorkStation1(client, user, workstation):
    """

    :param client:
    :param user:
    :param workstation:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    update_date = {'name': 'Zmieniona nazwa','norm': 999}
    result = client.post(f'/erp/update_work_position/{workstation[1].id}/', update_date)
    assert result.status_code == 302

#16.
@pytest.mark.django_db
def test_updateWorkStation2(client, user, workstation):
    """

    :param client:
    :param user:
    :param workstation:
    :return: assert id_before_update == id_after_update
    """
    client.force_login(user)
    id_before_update = WorkStation.objects.get(pk=workstation[6].pk).id
    update_date = {'name': 'Zmieniona nazwa','norm': 999}
    client.post(f'/erp/update_work_position/{workstation[6].id}/', update_date)
    id_after_update = WorkStation.objects.get(name='Zmieniona nazwa', norm=999).id
    assert id_before_update == id_after_update

#17.
@pytest.mark.django_db
def test_createSupplier(client, user):
    """

    :param client:
    :param user:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(reverse('createSupplier'))
    assert result.status_code == 200

#18.
@pytest.mark.django_db
def test_createSupplier1(client, user):
    """

    :param client:
    :param user:
    :return: assert len(Supplier.objects.filter(nip='741852741A')) == 0
    """
    client.force_login(user)
    supplier = {'name' : f'XYZ Supplier', 'address' : 'London SienkiewiczStreet', 'nip': '741852741A', 'industry' : 'BHP'}
    client.post('/erp/create_supplier/', supplier)
    assert len(Supplier.objects.filter(nip='741852741A')) == 0


#19.
@pytest.mark.django_db
def test_createSupplier2(client, user):
    """

    :param client:
    :param user:
    :return:  assert result.status_code == 302
    """
    client.force_login(user)
    supplier = {'name' : 'XYZ Supplier', 'address' : 'London SienkiewiczStreet', 'nip': '7418527418', 'industy' : 'BHP'}
    result = client.post(reverse('createSupplier'), supplier)
    assert result.status_code == 302


#20.
@pytest.mark.django_db
def test_listSupplier(client):
    """

    :param client:
    :return: assert client.get(reverse('listSupplier')).status_code == 200
    """
    assert client.get(reverse('listSupplier')).status_code == 200


#21.
@pytest.mark.django_db
def test_listSupplier1(client, user):
    """

    :param client:
    :param user:
    :return: assert client.get(reverse('listSupplier')).status_code == 200
    """
    client.force_login(user)
    assert client.get(reverse('listSupplier')).status_code == 200


#22.
@pytest.mark.django_db
def test_listSupplier2(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert supplier.count() == len(result.context['object_list'])
    """
    result = client.get('/erp/list_supplier/')
    assert supplier.count() == len(result.context['object_list'])

#23.
@pytest.mark.django_db
def test_listSupplier3(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert obj in supplier
    """
    result = client.get('/erp/list_supplier/')
    for obj in result.context['object_list']:
        assert obj in supplier

#24.
@pytest.mark.django_db
def test_updateSupplier(client, supplier):
    """

    :param client:
    :param supplier:
    :return:  assert result.status_code == 302
    """
    number = supplier[5].id
    result = client.get(f'/erp/update_supplier/{number}/')
    assert result.status_code == 302

#25.
@pytest.mark.django_db
def test_updateSupplier1(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(f'/erp/update_supplier/{supplier[4].id}/')
    assert result.status_code == 200

#26.
@pytest.mark.django_db
def test_updateSupplier2(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    supplier_update = {'name' : 'Test pytest', 'address' : 'Pytest-Django Street 5', 'nip' : '1000058409', 'industy' : 'AUT'}
    result = client.post(f'/erp/update_supplier/{supplier[1].id}/', supplier_update)
    assert result.status_code == 302

#27.
@pytest.mark.django_db
def test_updateSupplier3(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert len(Supplier.objects.filter(nip='1000058009')) == 1
    """
    client.force_login(user)
    supplier_update = {'name' : 'Test pytest', 'address' : 'Pytest-Django Street 5', 'nip' : '1000058009', 'industy' : 'AUT'}
    client.post(f'/erp/update_supplier/{supplier[3].id}/', supplier_update)
    assert len(Supplier.objects.filter(nip='1000058009')) == 1

#28.
@pytest.mark.django_db
def test_deleteSupplier1(client, supplier):
    """

    :param client:
    :param supplier:
    :return: assert result.status_code == 302
    """
    number = supplier[5].id
    result = client.get(f'/erp/delete_supplier/{number}/')
    assert result.status_code == 302

#29.
@pytest.mark.django_db
def test_deleteSupplier2(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(f'/erp/delete_supplier/{supplier[3].id}/')
    assert result.status_code == 200

#30.
@pytest.mark.django_db
def test_deleteSupplier3(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    result = client.post(f'/erp/delete_supplier/{supplier[4].id}/')
    assert result.status_code == 302

#31.
@pytest.mark.django_db
def test_deleteSupplier4(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert len(Supplier.objects.filter(pk=number)) == 0
    """
    client.force_login(user)
    number = supplier[5].id
    client.post(f'/erp/delete_supplier/{number}/')
    assert len(Supplier.objects.filter(pk=number)) == 0


#32.
@pytest.mark.django_db
def test_listDiscountSupplier(client, discountsupplier):
    """

    :param client:
    :param discountsupplier:
    :return: assert client.get(reverse('listDiscountSupplier')).status_code == 200
    """
    assert client.get(reverse('listDiscountSupplier')).status_code == 200

#33.
@pytest.mark.django_db
def test_listDiscountSupplier1(client, discountsupplier):
    """

    :param client:
    :param discountsupplier:
    :return:  assert discountsupplier.count() == len(client.get(reverse('listDiscountSupplier')).context['object_list'])
    """
    assert discountsupplier.count() == len(client.get(reverse('listDiscountSupplier')).context['object_list'])

#34.
@pytest.mark.django_db
def test_listDiscountSupplier2(client, discountsupplier):
    """

    :param client:
    :param discountsupplier:
    :return: assert obj in discountsupplier
    """
    for obj in client.get(reverse('listDiscountSupplier')).context['object_list']:
        assert obj in discountsupplier

#35.
@pytest.mark.django_db
def test_createDiscountSupplier(client, user, supplier, discountsupplier):
    """

    :param client:
    :param user:
    :param supplier:
    :param discountsupplier:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    discountsupplier = {'name' : 'Test Discount', 'value_percent':'9', 'supplier': supplier[2].id}
    result = client.post(reverse('createDiscountSupplier'), discountsupplier)
    assert result.status_code == 200

#36.
@pytest.mark.django_db
def test_createDiscountSupplier1(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    discountsupplier = {'name' : 'Test Discount', 'value_percent':'9', 'supplier': supplier[0].id}
    result = client.post(reverse('createDiscountSupplier'), discountsupplier)
    assert result.status_code == 302

#37.
@pytest.mark.django_db
def test_createDiscountSupplier2(client, supplier):
    """

    :param client:
    :param supplier:
    :return: assert result.status_code == 302
    """
    discountsupplier = {'name' : 'Test Discount', 'value_percent':'9', 'supplier': supplier[3].id}
    result = client.post(reverse('createDiscountSupplier'), discountsupplier)
    assert result.status_code == 302


#38.
@pytest.mark.django_db
def test_deleteDiscountSupplier(client, discountsupplier):
    """

    :param client:
    :param discountsupplier:
    :return: assert result.status_code == 302
    """
    number = discountsupplier[3].id
    result = client.get(f'/erp/delete_discount_supplier/{number}/')
    assert result.status_code == 302

#39.
@pytest.mark.django_db
def test_deleteDiscountSupplier1(client, discountsupplier):
    """

    :param client:
    :param discountsupplier:
    :return: assert result.status_code == 302
    """
    number = discountsupplier[2].id
    result = client.post(f'/erp/delete_discount_supplier/{number}/')
    assert result.status_code == 302

#40.
@pytest.mark.django_db
def test_deleteDiscountSupplier2(client, user, discountsupplier):
    """

    :param client:
    :param user:
    :param discountsupplier:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(f'/erp/delete_discount_supplier/{discountsupplier[1].id}/')
    assert result.status_code == 200

#41.
@pytest.mark.django_db
def test_deleteDiscountSupplier3(client, user, discountsupplier):
    """

    :param client:
    :param user:
    :param discountsupplier:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    result = client.post(f'/erp/delete_discount_supplier/{discountsupplier[0].id}/')
    assert result.status_code == 302

#42.
@pytest.mark.django_db
def test_updateDiscountSupplier(client, discountsupplier):
    """

    :param client:
    :param discountsupplier:
    :return: assert result.status_code == 302
    """
    number = discountsupplier[4].id
    result = client.get(f'/erp/update_discount_supplier/{number}/')
    assert result.status_code == 302

#43.
@pytest.mark.django_db
def test_updateDiscountSupplier1(client, discountsupplier):
    """

    :param client:
    :param discountsupplier:
    :return: assert result.status_code == 302
    """
    number = discountsupplier[4].id
    result = client.post(f'/erp/update_discount_supplier/{number}/')
    assert result.status_code == 302

#44.
@pytest.mark.django_db
def test_updateDiscountSupplier2(client, user, supplier, discountsupplier):
    """

    :param client:
    :param user:
    :param supplier:
    :param discountsupplier:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    change_data = {'name' : 'Test Discount1', 'value_percent':'20', 'supplier': supplier[2].id}
    result = client.post(f'/erp/update_discount_supplier/{discountsupplier[3].id}/', change_data)
    assert result.status_code == 200

#45.
@pytest.mark.django_db
def test_updateDiscountSupplier3(client, user, supplier, discountsupplier):
    """

    :param client:
    :param user:
    :param supplier:
    :param discountsupplier:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    change_data = {'name' : 'Test Discount1', 'value_percent':'20', 'supplier': supplier[6].id}
    result = client.post(f'/erp/update_discount_supplier/{discountsupplier[3].id}/', change_data)
    assert result.status_code == 302

#46.
@pytest.mark.django_db
def test_listCustomer(client, customer):
    """

    :param client:
    :param customer:
    :return: assert client.get(reverse('listCustomer')).status_code == 200
    """
    assert client.get(reverse('listCustomer')).status_code == 200

#47.
@pytest.mark.django_db
def test_listCustomer1(client, customer):
    """

    :param client:
    :param customer:
    :return: assert obj in customer
    """
    for obj in client.get(reverse('listCustomer')).context['object_list']:
        assert obj in customer

#48.
@pytest.mark.django_db
def test_listCustomer2(client, customer):
    """

    :param client:
    :param customer:
    :return: assert customer.count() ==  len(client.get(reverse('listCustomer')).context['object_list'])
    """
    assert customer.count() ==  len(client.get(reverse('listCustomer')).context['object_list'])

#49.
@pytest.mark.django_db
def test_createCustomer(client):
    """

    :param client:
    :return: assert client.get(reverse('createCustomer')).status_code == 302
    """
    assert client.get(reverse('createCustomer')).status_code == 302

#50.
@pytest.mark.django_db
def test_createCustomer1(client, user):
    """

    :param client:
    :param user:
    :return: assert client.get(reverse('createCustomer')).status_code == 200
    """
    client.force_login(user)
    assert client.get(reverse('createCustomer')).status_code == 200

#51.
@pytest.mark.django_db
def test_createCustomer2(client, user):
    """

    :param client:
    :param user:
    :return: assert client.post(reverse('createCustomer'), customer).status_code == 200
    """
    client.force_login(user)
    customer = {'name' : 'XXX', 'address' : 'OldStreet 100', 'delivery_address' : 'The same', 'nip' : '7854',
                'industy' : 'BHP'}
    assert client.post(reverse('createCustomer'), customer).status_code == 200

#52.
@pytest.mark.django_db
def test_createCustomer3(client, user):
    """

    :param client:
    :param user:
    :return: assert client.post(reverse('createCustomer'), customer).status_code == 200
    """
    client.force_login(user)
    customer = {'name' : 'XXX', 'address' : 'OldStreet 100', 'delivery_address' : 'The same', 'nip' : '7854pokjuh',
                'industy' : 'BHP'}
    assert client.post(reverse('createCustomer'), customer).status_code == 200

#53.
@pytest.mark.django_db
def test_createCustomer4(client, user, customer, supplier):
    """

    :param client:
    :param user:
    :param customer:
    :param supplier:
    :return: assert client.post(reverse('createCustomer'), customer_new).status_code == 200
    """
    client.force_login(user)
    customer_new = {'name' : 'XXX', 'address' : 'OldStreet 100', 'delivery_address' : 'The same', 'nip' : '7854123652',
                'industy' : 'BHP'}
    customer_new2 = {'name' : 'YYY', 'address' : 'NewStreet 200', 'delivery_address' : 'Rawicz', 'nip' : '7854123652',
                'industy' : 'BHP'}
    client.post(reverse('createCustomer'), customer_new2)
    assert client.post(reverse('createCustomer'), customer_new).status_code == 200


#54.
@pytest.mark.django_db
def test_createCustomer5(client, user, customer, supplier):
    """

    :param client:
    :param user:
    :param customer:
    :param supplier:
    :return: assert client.post(reverse('createCustomer'), customer_new).status_code == 302
    """
    client.force_login(user)
    customer_new = {'name' : 'XXX', 'address' : 'OldStreet 100', 'delivery_address' : 'The same', 'nip' : '7854123652',
                'industy' : 'BHP'}
    assert client.post(reverse('createCustomer'), customer_new).status_code == 302

#55.
@pytest.mark.django_db
def test_updateCustomer(client, customer):
    """

    :param client:
    :param customer:
    :return: assert client.get(f'/erp/update_customer/{customer[6].id}/').status_code == 302
    """
    assert client.get(f'/erp/update_customer/{customer[6].id}/').status_code == 302

#56.
@pytest.mark.django_db
def test_updateCustomer1(client, user):
    """

    :param client:
    :param user:
    :return: assert client.get(f'/erp/update_customer/9/').status_code == 404
    """
    client.force_login(user)
    assert client.get(f'/erp/update_customer/x/').status_code == 404

#57.
@pytest.mark.django_db
def test_updateCustomer2(client, user, customer):
    """

    :param client:
    :param user:
    :param customer:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    change_data = {'name' : 'XXX', 'address' : 'OldStreet 100', 'delivery_address' : 'The same', 'nip' : '2255225522',
                'industy' : 'BHP'}
    result = client.post(f'/erp/update_customer/{customer[4].id}/', change_data)
    assert result.status_code == 302

#58.
@pytest.mark.django_db
def test_updateCustomer3(client, user, customer):
    """

    :param client:
    :param user:
    :param customer:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    change_data = {'name' : 'XXX', 'address' : 'OldStreet 100', 'delivery_address' : 'The same', 'nip' : '22pp225522',
                'industy' : 'BHP'}
    result = client.post(f'/erp/update_customer/{customer[2].id}/', change_data)
    assert result.status_code == 200

#59.
@pytest.mark.django_db
def test_deleteCustomer(client,customer):
    """

    :param client:
    :param customer:
    :return: assert client.get(f'/erp/delete_customer/{number}/').status_code == 302
    """
    number = customer[1].id
    assert client.get(f'/erp/delete_customer/{number}/').status_code == 302

#60.
@pytest.mark.django_db
def test_deleteCustomer1(client, user, customer):
    """

    :param client:
    :param user:
    :param customer:
    :return: assert client.get(f'/erp/delete_customer/{customer[6].id}/').status_code == 200
    """
    client.force_login(user)
    assert client.get(f'/erp/delete_customer/{customer[6].id}/').status_code == 200

#61.
@pytest.mark.django_db
def test_deleteCustomer2(client, user, customer):
    """

    :param client:
    :param user:
    :param customer:
    :return: assert client.post(f'/erp/delete_customer/{customer[6].id}/').status_code == 302
    """
    client.force_login(user)
    assert client.post(f'/erp/delete_customer/{customer[6].id}/').status_code == 302

#62.
@pytest.mark.django_db
def test_deleteCustomer3(client, user, customer):
    """

    :param client:
    :param user:
    :param customer:
    :return: assert len(Customer.objects.filter(pk=number)) == 0
    """
    client.force_login(user)
    number = customer[3].id
    client.post(f'/erp/delete_customer/{number}/')
    assert len(Customer.objects.filter(pk=number)) == 0

#63.
@pytest.mark.django_db
def test_listDiscountCustomer(client, discountcustomer):
    """

    :param client:
    :param discountcustomer:
    :return: assert client.get(reverse('listDiscountCustomer')).status_code == 200
    """
    assert client.get(reverse('listDiscountCustomer')).status_code == 200

#64.
@pytest.mark.django_db
def test_listDiscountCustomer1(client, discountcustomer):
    """

    :param client:
    :param discountcustomer:
    :return: assert discountcustomer.count() == len(client.get(reverse('listDiscountCustomer')).context['object_list'])
    """
    assert discountcustomer.count() == len(client.get(reverse('listDiscountCustomer')).context['object_list'])

#65.
@pytest.mark.django_db
def test_listDiscountCustomer2(client, discountcustomer):
    """

    :param client:
    :param discountcustomer:
    :return: assert obj in discountcustomer
    """
    for obj in client.get(reverse('listDiscountCustomer')).context['object_list']:
        assert obj in discountcustomer

#66.
@pytest.mark.django_db
def test_createDiscountCustomer(client, user, customer, discountcustomer):
    """

    :param client:
    :param user:
    :param customer:
    :param discountcustomer:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    discountcustomer = {'name' : 'Test Discount', 'value_percent':'9', 'customer': customer[2].id}
    result = client.post(reverse('createDiscountSupplier'), discountcustomer)
    assert result.status_code == 200

#67.
@pytest.mark.django_db
def test_createDiscountCustomer1(client, user, customer):
    """

    :param client:
    :param user:
    :param customer:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    discountcustomer = {'name' : 'Test Discount', 'value_percent':'9', 'customer': customer[4].id}
    result = client.post(reverse('createDiscountCustomer'), discountcustomer)
    assert result.status_code == 302

#68.
@pytest.mark.django_db
def test_createDiscountCustomer2(client, customer):
    """

    :param client:
    :param customer:
    :return: assert result.status_code == 302
    """
    discountcustomer = {'name' : 'Test Discount', 'value_percent':'9', 'customer': customer[0].id}
    result = client.post(reverse('createDiscountCustomer'), discountcustomer)
    assert result.status_code == 302


#69.
@pytest.mark.django_db
def test_deleteDiscountCustomer(client, discountcustomer):
    """

    :param client:
    :param discountcustomer:
    :return: assert result.status_code == 302
    """
    number = discountcustomer[2].id
    result = client.get(f'/erp/delete_discount_customer/{number}/')
    assert result.status_code == 302

#70.
@pytest.mark.django_db
def test_deleteDiscountCustomer1(client, discountcustomer):
    """

    :param client:
    :param discountcustomer:
    :return: assert result.status_code == 302
    """
    number = discountcustomer[1].id
    result = client.post(f'/erp/delete_discount_customer/{number}/')
    assert result.status_code == 302

#71.
@pytest.mark.django_db
def test_deleteDiscountCustomer2(client, user, discountcustomer):
    """

    :param client:
    :param user:
    :param discountcustomer:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(f'/erp/delete_discount_customer/{discountcustomer[4].id}/')
    assert result.status_code == 200

#72.
@pytest.mark.django_db
def test_deleteDiscountCustomer3(client, user, discountcustomer):
    """

    :param client:
    :param user:
    :param discountcustomer:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    result = client.post(f'/erp/delete_discount_customer/{discountcustomer[0].id}/')
    assert result.status_code == 302

#73.
@pytest.mark.django_db
def test_updateDiscountCustomer(client, discountcustomer):
    """

    :param client:
    :param discountcustomer:
    :return: assert result.status_code == 302
    """
    number = discountcustomer[2].id
    result = client.get(f'/erp/update_discount_customer/{number}/')
    assert result.status_code == 302

#74.
@pytest.mark.django_db
def test_updateDiscountCustomer1(client, discountcustomer):
    """

    :param client:
    :param discountcustomer:
    :return: assert result.status_code == 302
    """
    number = discountcustomer[2].id
    result = client.post(f'/erp/update_discount_customer/{number}/')
    assert result.status_code == 302

#75.
@pytest.mark.django_db
def test_updateDiscountCustomer2(client, user, customer, discountcustomer):
    """

    :param client:
    :param user:
    :param customer:
    :param discountcustomer:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    change_data = {'name' : 'Test Discount1', 'value_percent':'20', 'customer': customer[1].id}
    result = client.post(f'/erp/update_discount_customer/{discountcustomer[4].id}/', change_data)
    assert result.status_code == 200

#76.
@pytest.mark.django_db
def test_updateDiscountCustomer3(client, user, customer, discountcustomer):
    """

    :param client:
    :param user:
    :param customer:
    :param discountcustomer:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    change_data = {'name' : 'Test Discount1', 'value_percent':'20', 'customer': customer[6].id}
    result = client.post(f'/erp/update_discount_customer/{discountcustomer[2].id}/', change_data)
    assert result.status_code == 302


#77.
@pytest.mark.django_db
def test_listMaterial(client, material):
    """

    :param client:
    :param material:
    :return: assert client.get(reverse('listMaterial')).status_code == 200
    """
    assert client.get(reverse('listMaterial')).status_code == 200


#78.
@pytest.mark.django_db
def test_listMaterial1(client, material):
    """

    :param client:
    :param material:
    :return: assert len(client.get(reverse('listMaterial')).context['object_list']) > 0
    """
    assert len(client.get(reverse('listMaterial')).context['object_list']) > 0


#79.
@pytest.mark.django_db
def test_listMaterial2(client, material):
    """

    :param client:
    :param material:
    :return: assert obj in material
    """
    for obj in client.get(reverse('listMaterial')).context['object_list'] :
        assert obj in material


#80.
@pytest.mark.django_db
def test_createMaterial(client, user):
    """

    :param client:
    :param user:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(reverse('createMaterial'))
    assert result.status_code == 200

#81.
@pytest.mark.django_db
def test_createMaterial1(client, user, supplier):
    """

    :param client:
    :param user:
    :param supplier:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    data = {'name' : 'Material test', 'index' : 9517413215, 'description' : 'Test element', 'quantity' : 3,
            'supplier': supplier[3].id}
    result = client.post(reverse('createMaterial'), data)
    assert result.status_code == 302


#82.
@pytest.mark.django_db
def test_createMaterial2(client, user, supplier, material):
    """

    :param client:
    :param user:
    :param supplier:
    :param material:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    data = {'name' : 'Material test xxx', 'index' : 9517413211, 'description' : 'Test element', 'quantity' : 3,
            'supplier': supplier[4].id}
    result = client.post(reverse('createMaterial'), data)
    assert result.status_code == 302

#83.
@pytest.mark.django_db
def test_createMaterial3(client, supplier, material):
    """

    :param client:
    :param supplier:
    :param material:
    :return: assert result.status_code == 302
    """
    data = {'name' : 'Material test xxx', 'index' : 9517413215, 'description' : 'Test element', 'quantity' : 3,
            'supplier': supplier[0].id}
    result = client.post(reverse('createMaterial'), data)
    assert result.status_code == 302


#84.
@pytest.mark.django_db
def test_upgrateMaterial(client, user, material):
    """

    :param client:
    :param user:
    :param material:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(f'/erp/update_material/{material[4].id}/')
    assert result.status_code == 200


#85.
@pytest.mark.django_db
def test_upgrateMaterial1(client, user, supplier, material):
    """

    :param client:
    :param user:
    :param supplier:
    :param material:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    data = {'name' : 'Material test xxx', 'index' : 9517413215, 'description' : 'Test element', 'quantity' : 3,
            'supplier': supplier[3].id}
    result = client.post(f'/erp/update_material/{material[4].id}/', data)
    assert result.status_code == 302


#86.
@pytest.mark.django_db
def test_upgrateMaterial2(client, user, supplier, material):
    """

    :param client:
    :param user:
    :param supplier:
    :param material:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    data = {'name' : 'Material test xxx', 'index' : 9517413215, 'description' : 'Test element', 'quantity' : 3}
    result = client.post(f'/erp/update_material/{material[4].id}/', data)
    assert result.status_code == 200


#87.
@pytest.mark.django_db
def test_deleteMaterial(client, user, material):
    """

    :param client:
    :param user:
    :param material:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    result = client.post(f'/erp/delete_material/{material[4].id}/')
    assert result.status_code == 302


#88.
@pytest.mark.django_db
def test_deleteMaterial1(client, user, material):
    """

    :param client:
    :param user:
    :param material:
    :return: assert len(Material.objects.filter(pk=number)) == 0
    """
    client.force_login(user)
    number = material[4].id
    client.post(f'/erp/delete_material/{number}/')
    assert len(Material.objects.filter(pk=number)) == 0


#89.
@pytest.mark.django_db
def test_deleteMaterial2(client, material):
    """

    :param client:
    :param material:
    :return: assert len(Material.objects.filter(pk=number)) == 1
    """
    number = material[5].id
    client.post(f'/erp/delete_material/{number}/')
    assert len(Material.objects.filter(pk=number)) == 1


#90.
@pytest.mark.django_db
def test_listDocumentSupplier(client, documentsupplier):
    """

    :param client:
    :param documentsupplier:
    :return: assert client.get(reverse('listDocumentSupplier')).status_code == 200
    """
    assert client.get(reverse('listDocumentSupplier')).status_code == 200


#91.
@pytest.mark.django_db
def test_listDocumentSupplier1(client, documentsupplier):
    """

    :param client:
    :param documentsupplier:
    :return: assert documentsupplier.count() == client.get(reverse('listDocumentSupplier')).context['object_list'].count()
    """
    assert documentsupplier.count() == client.get(reverse('listDocumentSupplier')).context['object_list'].count()


#92.
@pytest.mark.django_db
def test_listDocumentSupplier2(client, documentsupplier):
    """

    :param client:
    :param documentsupplier:
    :return: assert obj in documentsupplier
    """
    for obj in client.get(reverse('listDocumentSupplier')).context['object_list']:
        assert obj in documentsupplier

#93.
@pytest.mark.django_db
def test_createDocumentSupplier(client, user, supplier, material):
    """

    :param client:
    :param user:
    :param supplier:
    :param material:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    number_supplier = supplier[5].id
    result = client.get(f'/erp/create_document/supplier/{number_supplier}/')
    assert result.status_code == 200


#94.
@pytest.mark.django_db
def test_createDocumentSupplier1(client, user, supplier, material):
    """

    :param client:
    :param user:
    :param supplier:
    :param material:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    number_supplier = supplier[2].id
    materials = Material.objects.filter(supplier_id=number_supplier)
    data = {'number' : 'Test xyz1', 'destination' : 'PUR', 'supplier' : number_supplier, 'materials' : [materials[0].id, materials[1].id]}
    result = client.post(f'/erp/create_document/supplier/{number_supplier}/', data)
    assert result.status_code == 302


#95.
@pytest.mark.django_db
def test_createDocumentSupplier2(client, user, supplier, material):
    """

    :param client:
    :param user:
    :param supplier:
    :param material:
    :return: assert DocumentSupplier.objects.last().supplier == supplier[4]
    """
    client.force_login(user)
    number_supplier = supplier[4].id
    materials = Material.objects.filter(supplier_id=number_supplier)
    data = {'number' : f'{number_supplier} yzx', 'destination' : 'PUR', 'supplier' : number_supplier, 'materials' : [materials[0].id, materials[1].id]}
    client.post(f'/erp/create_document/supplier/{number_supplier}/', data)
    assert DocumentSupplier.objects.last().supplier == supplier[4]


#96.
@pytest.mark.django_db
def test_createDocumentSupplier3(client, user, supplier, material):
    """

    :param client:
    :param user:
    :param supplier:
    :param material:
    :return: assert object in DocumentSupplier.objects.last().materials.all()
    """
    client.force_login(user)
    number_supplier = supplier[3].id
    materials = Material.objects.filter(supplier_id=number_supplier)
    data = {'number': f'{number_supplier} yzx', 'destination': 'PUR', 'supplier': number_supplier,
            'materials': [materials[0].id, materials[1].id, materials[3].id]}
    client.post(f'/erp/create_document/supplier/{number_supplier}/', data)
    for object in [materials[0], materials[1], materials[3]]:
        assert object in DocumentSupplier.objects.last().materials.all()


#97.
@pytest.mark.django_db
def test_deleteDocumentSupplier(client, user, documentsupplier):
    """

    :param client:
    :param user:
    :param documentsupplier:
    :return: assert client.get(f'/erp/delete_document_supplier/{documentsupplier[8].id}/').status_code == 200
    """
    client.force_login(user)
    assert client.get(f'/erp/delete_document_supplier/{documentsupplier[8].id}/').status_code == 200

#98.
@pytest.mark.django_db
def test_deleteDocumentSupplier1(client, user, documentsupplier):
    """

    :param client:
    :param user:
    :param documentsupplier:
    :return: assert client.post(f'/erp/delete_document_supplier/{documentsupplier[2].id}/').status_code == 302
    """
    client.force_login(user)
    assert client.post(f'/erp/delete_document_supplier/{documentsupplier[2].id}/').status_code == 302

#99.
@pytest.mark.django_db
def test_deleteDocumentSupplier2(client, user, documentsupplier):
    """

    :param client:
    :param user:
    :param documentsupplier:
    :return: assert len(DocumentSupplier.objects.filter(pk=number)) == 0
    """
    client.force_login(user)
    number = documentsupplier[4].id
    client.post(f'/erp/delete_document_supplier/{number}/')
    assert len(DocumentSupplier.objects.filter(pk=number)) == 0


#100.
@pytest.mark.django_db
def test_updateDocumentSupplier(client, documentsupplier):
    """

    :param client:
    :param documentsupplier:
    :return: assert client.get(f'/erp/update_document_supplier/{number}/').status_code == 302
    """
    number = documentsupplier[3].id
    assert client.get(f'/erp/update_document_supplier/{number}/').status_code == 302

#101.
@pytest.mark.django_db
def test_updateDocumentSupplier1(client, user, documentsupplier):
    """

    :param client:
    :param user:
    :param documentsupplier:
    :return: assert client.get(f'/erp/update_document_supplier/{number}/').status_code == 200
    """
    client.force_login(user)
    number = documentsupplier[3].id
    assert client.get(f'/erp/update_document_supplier/{number}/').status_code == 200

#102.
@pytest.mark.django_db
def test_updateDocumentSupplier2(client, user, documentsupplier, supplier, material):
    """

    :param client:
    :param user:
    :param documentsupplier:
    :param supplier:
    :param material:
    :return: assert client.post(f'/erp/update_document_supplier/{number}/', data).status_code == 302
    """
    client.force_login(user)
    number = documentsupplier[3].id
    number_supplier = documentsupplier[3].supplier_id
    materials = Material.objects.filter(supplier_id=number_supplier)
    data = {'number': f'{number_supplier} yzx', 'destination': 'PUR', 'supplier': number_supplier,
            'materials': [materials[0].id, materials[1].id, materials[3].id]}
    assert client.post(f'/erp/update_document_supplier/{number}/', data).status_code == 302


#103.
@pytest.mark.django_db
def test_listGood(client, good):
    """

    :param client:
    :param good:
    :return: assert client.get(reverse('listGood')).status_code == 200
    """
    assert client.get(reverse('listGood')).status_code == 200


#104.
@pytest.mark.django_db
def test_listGood1(client, good):
    """

    :param client:
    :param good:
    :return: assert obj in good[0
    """
    for obj in client.get(reverse('listGood')).context['object_list']:
        assert obj in good[0]


#105.
@pytest.mark.django_db
def test_listGood2(client, good):
    """

    :param client:
    :param good:
    :return: assert good[0].count() == client.get(reverse('listGood')).context['object_list'].count()
    """
    assert good[0].count() == client.get(reverse('listGood')).context['object_list'].count()


#106.
@pytest.mark.django_db
def test_createGood(client, user):
    """

    :param client:
    :param user:
    :return: assert result.status_code == 302
    """
    data = {'name' : 'Good test xxx', 'index' : 9517413215, 'description' : 'Test element', 'quantity' : 3,
            }
    client.force_login(user)
    result = client.post(reverse('createGood'), data)
    assert result.status_code == 302


#107.
@pytest.mark.django_db
def test_createGood1(client, user, material):
    """

    :param client:
    :param user:
    :param material:
    :return: assert result.status_code == 302
    """
    materials = [material[1].id, material[2].id, material[3].id, material[5].id]
    data = {'name' : 'Good test xxx', 'index' : '8521652314', 'description' : 'Test element', 'quantity' : 3, 'material' : materials}
    client.force_login(user)
    result = client.post(reverse('createGood'), data)
    assert result.status_code == 302


#108.
@pytest.mark.django_db
def test_createGood2(client, user):
    """

    :param client:
    :param user:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    result = client.get(reverse('createGood'))
    assert result.status_code == 200


#109.
@pytest.mark.django_db
def test_deleteGood(client, user, good):
    """

    :param client:
    :param user:
    :param good:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    good_list = good[0]
    number = good_list[2].id
    result = client.post(f'/erp/delete_good/{number}/')
    assert result.status_code == 302


#110.
@pytest.mark.django_db
def test_deleteGood1(client, user, good):
    """

    :param client:
    :param user:
    :param good:
    :return: assert len(Good.objects.filter(pk=number)) == 0
    """
    client.force_login(user)
    good_list = good[0]
    number = good_list[2].id
    client.post(f'/erp/delete_good/{number}/')
    assert len(Good.objects.filter(pk=number)) == 0


#111.
@pytest.mark.django_db
def test_deleteGood2(client, good):
    """

    :param client:
    :param good:
    :return: assert len(Good.objects.filter(pk=number)) == 1
    """
    good_list = good[0]
    number = good_list[1].id
    client.post(f'/erp/delete_good/{number}/')
    assert len(Good.objects.filter(pk=number)) == 1


#112.
@pytest.mark.django_db
def test_upgrateGood(client, user, good, material):
    """

    :param client:
    :param user:
    :param good:
    :param material:
    :return: assert result.status_code == 200
    """
    good_list = good[0]
    number = good_list[1].id
    client.force_login(user)
    result = client.get(f'/erp/update_good/{number}/')
    assert result.status_code == 200


#113.
@pytest.mark.django_db
def test_upgrateGood1(client, user, good, material):
    """

    :param client:
    :param user:
    :param good:
    :param material:
    :return: assert result.status_code == 302
    """
    good_list = good[0]
    number = good_list[2].id
    materials = [material[1].id, material[2].id, material[3].id, material[5].id]
    client.force_login(user)
    data = {'name' : 'Good test xxx', 'index' : '1111511114', 'description' : 'Test element', 'quantity' : 10, 'material' : materials}
    result = client.post(f'/erp/update_good/{number}/', data)
    assert result.status_code == 302


#114.
@pytest.mark.django_db
def test_upgrateGood2(client, user, good, material):
    """

    :param client:
    :param user:
    :param good:
    :param material:
    :return: assert result.status_code == 302
    """
    client.force_login(user)
    good_list = good[0]
    number = good_list[2].id
    materials = [material[10].id, material[20].id, material[30].id]
    data = {'name' : 'Good 1 test xxx', 'index' : 9517413215, 'description' : 'Test element', 'quantity' : 300, 'material' : materials}
    result = client.post(f'/erp/update_good/{number}/', data)
    assert result.status_code == 302


#115.
@pytest.mark.django_db
def test_listDocumentCustomer(client, documentcustomer):
    """

    :param client:
    :param documentcustomer:
    :return:     assert client.get(reverse('listDocumentCustomer')).status_code == 200

    """
    assert client.get(reverse('listDocumentCustomer')).status_code == 200


#116.
@pytest.mark.django_db
def test_listDocumentCustomer1(client, documentcustomer):
    """

    :param client:
    :param documentcustomer:
    :return: assert documentcustomer.count() == client.get(reverse('listDocumentCustomer')).context['object_list'].count()
    """
    assert documentcustomer.count() == client.get(reverse('listDocumentCustomer')).context['object_list'].count()


#117.
@pytest.mark.django_db
def test_listDocumentCustomer2(client, documentcustomer):
    """

    :param client:
    :param documentcustomer:
    :return: assert obj in documentcustomer
    """
    for obj in client.get(reverse('listDocumentCustomer')).context['object_list']:
        assert obj in documentcustomer


#118.
@pytest.mark.django_db
def test_deleteDocumentCustomer(client, user, documentcustomer):
    """

    :param client:
    :param user:
    :param documentcustomer:
    :return: assert client.get(f'/erp/delete_document_customer/{documentcustomer[8].id}/').status_code == 200
    """
    client.force_login(user)
    assert client.get(f'/erp/delete_document_customer/{documentcustomer[8].id}/').status_code == 200

#119.
@pytest.mark.django_db
def test_deleteDocumentCustomer1(client, user, documentcustomer):
    """

    :param client:
    :param user:
    :param documentcustomer:
    :return: assert client.post(f'/erp/delete_document_customer/{documentcustomer[2].id}/').status_code == 302
    """
    client.force_login(user)
    assert client.post(f'/erp/delete_document_customer/{documentcustomer[2].id}/').status_code == 302

#120.
@pytest.mark.django_db
def test_deleteDocumentCustomer2(client, user, documentcustomer):
    """

    :param client:
    :param user:
    :param documentcustomer:
    :return: assert len(DocumentCustomer.objects.filter(pk=number)) == 0
    """
    client.force_login(user)
    number = documentcustomer[4].id
    client.post(f'/erp/delete_document_customer/{number}/')
    assert len(DocumentCustomer.objects.filter(pk=number)) == 0


#121.
@pytest.mark.django_db
def test_createDocumentCustomer(client, user, good, customer):
    """

    :param client:
    :param user:
    :param good:
    :param customer:
    :return: assert result.status_code == 302
    """
    products = good[0]
    goods = [products[0].id, products[1].id, products[3].id, products[5].id]
    client.force_login(user)
    number = customer[4].id
    data = {'number' : 'No 95 CD', 'destination' : 'TES', 'customer' : customer[4].id, 'good' : goods}
    result = client.post(f'/erp/create_document/customer/{number}/', data)
    assert result.status_code == 302


#122.
@pytest.mark.django_db
def test_createDocumentCustomer1(client, user, good, customer):
    """

    :param client:
    :param user:
    :param good:
    :param customer:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    number = customer[4].id
    result = client.get(f'/erp/create_document/customer/{number}/')
    assert result.status_code == 200


#123.
@pytest.mark.django_db
def test_createDocumentCustomer2(client, customer):
    """

    :param client:
    :param customer:
    :return: assert result.status_code == 302
    """
    number = customer[4].id
    result = client.get(f'/erp/create_document/customer/{number}/')
    assert result.status_code == 302


#124.
@pytest.mark.django_db
def test_updateDocumentCustomer(client, documentcustomer):
    """

    :param client:
    :param documentcustomer:
    :return: assert client.get(f'/erp/update_document_customer/{number}/').status_code == 302
    """
    number = documentcustomer[2].id
    assert client.get(f'/erp/update_document_customer/{number}/').status_code == 302


#125.
@pytest.mark.django_db
def test_updateDocumentCustomer1(client, user, documentcustomer):
    """

    :param client:
    :param user:
    :param documentcustomer:
    :return: assert client.get(f'/erp/update_document_customer/{number}/').status_code == 200
    """
    client.force_login(user)
    number = documentcustomer[2].id
    assert client.get(f'/erp/update_document_customer/{number}/').status_code == 200


#126.
@pytest.mark.django_db
def test_updateDocumentCustomer2(client, user, documentcustomer, customer, good):
    """

    :param client:
    :param user:
    :param documentcustomer:
    :param customer:
    :param good:
    :return: assert client.post(f'/erp/update_document_customer/{number}/', data).status_code == 302
    """
    client.force_login(user)
    number_customer = documentcustomer[3].customer_id
    products = good[0]
    goods = [products[0].id, products[1].id, products[3].id, products[5].id]
    number = documentcustomer[4].id
    data = {'number': 'No 95 CD', 'destination': 'TES', 'customer': number_customer, 'good': goods}
    assert client.post(f'/erp/update_document_customer/{number}/', data).status_code == 302


#127.
@pytest.mark.django_db
def test_tryProduce(client, user, good):
    """

    :param client:
    :param user:
    :param good:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    good_list = good[0]
    number = good_list[5].id
    result = client.get(f'/erp/try_produce/{number}/')
    assert result.status_code == 200

#128.
@pytest.mark.django_db
def test_tryProduce1(client, user, good):
    """

    :param client:
    :param user:
    :param good:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    good_list = good[0]
    number = good_list[1].id
    data = {'produce_quantity' : -1}
    result = client.post(f'/erp/try_produce/{number}/', data)
    assert result.status_code == 200


#129.
@pytest.mark.django_db
def test_tryProduce2(client, user, good):
    """

    :param client:
    :param user:
    :param good:
    :return: assert result.status_code == 200
    """
    client.force_login(user)
    good_list = good[0]
    number = good_list[0].id
    data = {'produce_quantity' : 3}
    result = client.post(f'/erp/try_produce/{number}/', data)
    assert result.status_code == 200



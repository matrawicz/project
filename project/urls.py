from django.contrib import admin
from django.urls import path

from project.views import MainPage, CreateWorkStation, ListWorkStation, UpdateWorkStation, DeleteWorkStation, \
    CreateSupplier, ListSupplier, UpdateSupplier, DeleteSupplier, CreateDiscountSupplier, ListDiscountSupplier, \
    UpdateDiscountSupplier, DeleteDiscountSupplier, CreateCustomer, ListCustomer, UpdateCustomer, DeleteCustomer, \
    CreateDiscountCustomer, ListDiscountCustomer, UpdateDiscountCustomer, DeleteDiscountCustomer, CreateMaterial, \
    ListMaterial, UpdateMaterial, DeleteMaterial, CreateDocumentSupplier, ListDocumentSupplier, UpdateDocumentSupplier, \
    DeleteDocumentSupplier, CreateGood, ListGood, UpdateGood, DeleteGood, CreateDocumentCustomer, ListDocumentCustomer, \
    UpdateDocumentCustomer, DeleteDocumentCustomer, TryPoduceGood

urlpatterns = [
    path('create_work_position/', CreateWorkStation.as_view(), name='createWorkStation'),
    path('list_work_position/', ListWorkStation.as_view(), name='listWorkStation'),
    path('update_work_position/<int:pk>/', UpdateWorkStation.as_view(), name='updateWorkStation'),
    path('delete_work_position/<int:pk>/', DeleteWorkStation.as_view(), name='deleteWorkStation'),
    path('create_supplier/', CreateSupplier.as_view(), name='createSupplier'),
    path('list_supplier/', ListSupplier.as_view(), name='listSupplier'),
    path('update_supplier/<int:pk>/', UpdateSupplier.as_view(), name='updateSupplier'),
    path('delete_supplier/<int:pk>/', DeleteSupplier.as_view(), name='deleteSupplier'),
    path('create_discount_supplier/', CreateDiscountSupplier.as_view(), name='createDiscountSupplier'),
    path('list_discount_supplier/', ListDiscountSupplier.as_view(), name='listDiscountSupplier'),
    path('update_discount_supplier/<int:pk>/', UpdateDiscountSupplier.as_view(), name='updateDiscountSupplier'),
    path('delete_discount_supplier/<int:pk>/', DeleteDiscountSupplier.as_view(), name='deleteDiscountSupplier'),
    path('create_customer/', CreateCustomer.as_view(), name='createCustomer'),
    path('list_customer/', ListCustomer.as_view(), name='listCustomer'),
    path('update_customer/<int:pk>/', UpdateCustomer.as_view(), name='updateCustomer'),
    path('delete_customer/<int:pk>/', DeleteCustomer.as_view(), name='deleteCustomer'),
    path('create_discount_customer/', CreateDiscountCustomer.as_view(), name='createDiscountCustomer'),
    path('list_discount_customer/', ListDiscountCustomer.as_view(), name='listDiscountCustomer'),
    path('update_discount_customer/<int:pk>/', UpdateDiscountCustomer.as_view(), name='updateDiscountCustomer'),
    path('delete_discount_customer/<int:pk>/', DeleteDiscountCustomer.as_view(), name='deleteDiscountCustomer'),
    path('create_material/', CreateMaterial.as_view(), name='createMaterial'),
    path('list_material/', ListMaterial.as_view(), name='listMaterial'),
    path('update_material/<int:pk>/', UpdateMaterial.as_view(), name='updateMaterial'),
    path('delete_material/<int:pk>/', DeleteMaterial.as_view(), name='deleteMaterial'),
    path('create_document/supplier/<int:pk>/', CreateDocumentSupplier.as_view(), name='createDocumentSupplier'),
    path('list_document_supplier/', ListDocumentSupplier.as_view(), name='listDocumentSupplier'),
    path('update_document_supplier/<int:pk>/', UpdateDocumentSupplier.as_view(), name='updateDocumentSupplier'),
    path('delete_document_supplier/<int:pk>/', DeleteDocumentSupplier.as_view(), name='deleteDocumentSupplier'),
    path('create_good/', CreateGood.as_view(), name='createGood'),
    path('list_good/', ListGood.as_view(), name='listGood'),
    path('update_good/<int:pk>/', UpdateGood.as_view(), name='updateGood'),
    path('delete_good/<int:pk>/', DeleteGood.as_view(), name='deleteGood'),
    path('create_document/customer/<int:pk>/', CreateDocumentCustomer.as_view(), name='createDocumentCustomer'),
    path('list_document_customer/', ListDocumentCustomer.as_view(), name='listDocumentCustomer'),
    path('update_document_customer/<int:pk>/', UpdateDocumentCustomer.as_view(), name='updateDocumentCustomer'),
    path('delete_document_customer/<int:pk>/', DeleteDocumentCustomer.as_view(), name='deleteDocumentCustomer'),
    path('try_produce/<int:pk>/', TryPoduceGood.as_view(), name='tryProduce')




]

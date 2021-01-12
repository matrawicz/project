from django.contrib.auth.models import User
from django.forms import forms
from django import forms

from project.models import Supplier, Customer, Material, Good


class UserForm(forms.ModelForm):

    class Meta:
        fields = ('username', 'password', 'is_superuser')
        model = User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CreateSupplierForm(forms.ModelForm):

        class Meta:
            model = Supplier
            fields = '__all__'

        def clean_nip(self):
            nip = self.cleaned_data.get('nip')
            nip_customer = Customer.objects.filter(nip=nip)
            print(len(nip_customer), f'Customer')
            nip_supplier = Supplier.objects.filter(nip=nip)
            print(nip_supplier, f'Supplier')
            if len(nip_customer) == 0 and len(nip_supplier) == 0:
                return nip
            raise forms.ValidationError(f'NIP jest już używany! Proszę o weryfikację!')


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def clean_nip(self):
        nip = self.cleaned_data.get('nip')
        nip_customer = Customer.objects.filter(nip=nip)
        nip_supplier = Supplier.objects.filter(nip=nip)
        if len(nip_customer) == 0 and len(nip_supplier) == 0:
            return nip
        raise forms.ValidationError(f'NIP jest już używany! Proszę o weryfikację!')


class CreateMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

    def clean_index(self):
        index = self.cleaned_data.get('index')
        index_material = Material.objects.filter(index=index)
        index_good = Good.objects.filter(index=index)
        if len(index_good) == 0 and len(index_material) == 0:
            return index
        raise forms.ValidationError(f'Indeks nie ma dokładnie 10 znaków lub jest zajęty')






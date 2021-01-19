from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from project.forms import UserForm, LoginForm, CreateSupplierForm, CreateCustomerForm, CreateMaterialForm
from project.functions import get_number_supplier_document, get_number_customer_document
from project.models import WorkStation, Supplier, DiscountSupplier, Customer, DiscountCustomer, Material, \
    DocumentSupplier, Good, GoodMaterial, DocumentCustomer


class MainPage(View):
    """
    PL: Widok wyświetlający stronę główną projektu.
    EN: View that displays the project's home page.
    """
    def get(self, request):
        return render(request, 'mainpage.html')


class AddUserView(View):
    """
    PL: Prosty widok umożliwiający dodanie użytkownika.
    EN: A simple view for adding a user.
    """

    def get(self, request):
        form = UserForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("/")
        return render(request, 'form.html', {'form': form})


class LoginView(View):
    """
    PL: Widok logowania użytkownika.
    EN: User login view.
    """

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form':form})


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next = request.GET.get('next', '/')
                return redirect(next)
        return render(request, 'form.html', {'form': form, "message":'Błędny login lub hasło'})



class LogoutView(View):
    """
    PL: Widok umożliwiający wylogowania.
    EN: Logout view.
    """

    def get(self, request):
        logout(request)
        return redirect('/')


class CreateWorkStation(LoginRequiredMixin, CreateView):
    """
    PL: Generyczny widok do tworzenia obiektu WorkStation.
    EN: Generic view for creating a WorkStation.
    """
    model = WorkStation
    fields = '__all__'
    template_name = 'create.html'
    success_url = reverse_lazy('listWorkStation')


class ListWorkStation(ListView):
    """
    PL: Generyczny widok listy obiektów WorkStation.
    EN: Generic List View of WorkStation Objects
    """
    model = WorkStation
    template_name = 'list.html'


class UpdateWorkStation(LoginRequiredMixin, UpdateView):
    """
    PL: Generyczny widok aktualizacji obiektu WorkStation.
    EN: WorkStation Generic Update View.
    """
    model = WorkStation
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('listWorkStation')


class DeleteWorkStation(LoginRequiredMixin, DeleteView):
    """
    PL: Generyczny widok usuwania obiektu WorkStation.
    EN: WorkStation Generic Delete View.
    """
    model = WorkStation
    template_name = 'delete.html'
    success_url = reverse_lazy('listWorkStation')


class CreateSupplier(LoginRequiredMixin, CreateView):
    """
    PL: Generyczny widok tworzenia obiektu Supplier.
    EN: Supplier Generic Create View.
    """
    model = Supplier
    form_class = CreateSupplierForm
    template_name = 'create.html'
    success_url = reverse_lazy('listSupplier')


class ListSupplier(ListView):
    """
    PL: Generyczny widok listy obiektów Supplier.
    EN: Supplier Generic List View.
    """
    model = Supplier
    template_name = 'listsupplier.html'


class UpdateSupplier(LoginRequiredMixin, UpdateView):
    """
    PL: Generyczny widok aktualizacji obiektu Supplier.
    EN: Supplier Generic Update View.
    """
    model = Supplier
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('listSupplier')


class DeleteSupplier(LoginRequiredMixin, View):
    def get(self, request, pk):
        """

        :param request:
        :param pk:
        :return: render(request, 'deleteprotected.html', {'object':object})
        """
        object = Supplier.objects.get(pk=pk)
        return render(request, 'deleteprotected.html', {'object':object})

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return: render(request, 'deleteprotected.html', {'message' : message})
        """
        try:
            object = Supplier.objects.get(pk=pk)
            object.delete()
            return redirect('listSupplier')
        except ProtectedError as e:
            message = f'Próbujesz usunąć obiekt powiązany z innymi obiektami. Najpierw usuń powiązanie. Typ błędu: {e}'
            return render(request, 'deleteprotected.html', {'message' : message})


class CreateDiscountSupplier(LoginRequiredMixin, CreateView):
    """
    PL: Generyczny widok tworzenia obiektów DiscountSupplier.
    EN: DiscountSupplier Generic Create View.
    """
    model = DiscountSupplier
    fields = '__all__'
    template_name = 'create.html'
    success_url = reverse_lazy('listDiscountSupplier')


class ListDiscountSupplier(ListView):
    """
    PL: Generyczny widok listy obiektów DiscountSupplier.
    EN: DiscountSupplier Generic List View.
    """
    model = DiscountSupplier
    template_name = 'list.html'


class UpdateDiscountSupplier(LoginRequiredMixin, UpdateView):
    """
    PL: Generyczny widok aktualizacji obiektu DiscountSupplier.
    EN: DiscountSupplier Generic Update View.
    """
    model = DiscountSupplier
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('listDiscountSupplier')


class DeleteDiscountSupplier(LoginRequiredMixin, DeleteView):
    """
    PL: Generyczny widok usuwania obiektu DiscountSupplier.
    EN: DiscountSupplier Generic Delete View.
    """
    model = DiscountSupplier
    template_name = 'delete.html'
    success_url = reverse_lazy('listDiscountSupplier')


class CreateCustomer(LoginRequiredMixin, CreateView):
    """
    PL: Generyczny widok do tworzenia obiektu Customer.
    EN: Generic view for creating a Customer.
    """
    model = Customer
    form_class = CreateCustomerForm
    template_name = 'create.html'
    success_url = reverse_lazy('listCustomer')


class ListCustomer(ListView):
    """
    PL: Generyczny widok listy obiektów Customer.
    EN: Customer Generic List View.
    """
    model = Customer
    template_name = 'listcustomer.html'


class UpdateCustomer(LoginRequiredMixin, UpdateView):
    """
    PL: Generyczny widok aktualizacji obiektu Customer.
    EN: Customer Generic Update View.
    """
    model = Customer
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('listCustomer')


class DeleteCustomer(LoginRequiredMixin, View):
    def get(self, request, pk):
        """

        :param request:
        :param pk:
        :return:render(request, 'deleteprotected.html', {'object':object})
        """

        object = Customer.objects.get(pk=pk)
        return render(request, 'deleteprotected.html', {'object':object})

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return:render(request, 'deleteprotected.html', {'message' : message})
        """
        try:
            object = Customer.objects.get(pk=pk)
            object.delete()
            return redirect('listCustomer')
        except ProtectedError as e:
            message = f'Próbujesz usunąć obiekt powiązany z innymi obiektami. Najpierw usuń powiązanie. Typ błędu: {e}'
            return render(request, 'deleteprotected.html', {'message' : message})


class CreateDiscountCustomer(LoginRequiredMixin, CreateView):
    """
    PL: Generyczny widok do tworzenia obiektu DiscountCustomer.
    EN: Generic view for creating a DiscountCustomer.
    """
    model = DiscountCustomer
    fields = '__all__'
    template_name = 'create.html'
    success_url = reverse_lazy('listDiscountCustomer')


class ListDiscountCustomer(ListView):
    """
    PL: Generyczny widok listy obiektów DiscountCustomer.
    EN: Customer Generic List View.
    """
    model = DiscountCustomer
    template_name = 'list.html'


class UpdateDiscountCustomer(LoginRequiredMixin, UpdateView):
    """
    PL: Generyczny widok aktualizacji obiektu DiscountCustomer.
    EN: DiscountCustomer Generic Update View.
    """
    model = DiscountCustomer
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('listDiscountCustomer')


class DeleteDiscountCustomer(LoginRequiredMixin, DeleteView):
    """
    PL: Generyczny widok usuwania obiektu DiscountCustomer.
    EN: DiscountCustomer Generic Delete View.
    """
    model = DiscountCustomer
    template_name = 'delete.html'
    success_url = reverse_lazy('listDiscountCustomer')


class CreateMaterial(LoginRequiredMixin, CreateView):
    """
    PL: Generyczny widok do tworzenia obiektu Material.
    EN: Generic view for creating a Material.
    """
    model = Material
    form_class = CreateMaterialForm
    template_name = 'create.html'
    success_url = reverse_lazy('listMaterial')


class ListMaterial(ListView):
    """
    PL: Generyczny widok listy obiektów Material.
    EN: Material Generic List View.
    """
    model = Material
    template_name = 'list.html'


class UpdateMaterial(LoginRequiredMixin, UpdateView):
    """
    PL: Generyczny widok aktualizacji obiektu Material.
    EN: Material Generic Update View.
    """
    model = Material
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('listMaterial')


class DeleteMaterial(LoginRequiredMixin, View):
    def get(self, request, pk):
        """

        :param request:
        :param pk:
        :return:render(request, 'deleteprotected.html', {'object':object})
        """
        object = Material.objects.get(pk=pk)
        return render(request, 'deleteprotected.html', {'object':object})

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return:render(request, 'deleteprotected.html', {'message' : message})
        """
        try:
            object = Material.objects.get(pk=pk)
            object.delete()
            return redirect('listMaterial')
        except ProtectedError as e:
            message = f'Próbujesz usunąć obiekt powiązany z innymi obiektami. Najpierw usuń powiązanie. Typ błędu: {e}'
            return render(request, 'deleteprotected.html', {'message' : message})


class CreateDocumentSupplier(LoginRequiredMixin, View):
    def get(self, request, pk):
        """

        :param request:
        :param pk:
        :return:render(request, 'createdocumentsuppliermanual.html', {'supplier':supplier,
                                                                     'materials':materials, 'number':number, 'destinations': destinations})
        """
        supplier = Supplier.objects.get(pk=pk)
        materials = Material.objects.filter(supplier_id=supplier.id)
        number = get_number_supplier_document()
        destinations = ['Reklamacja', 'Zakup', 'Testy', 'Gratis']
        return render(request, 'createdocumentsuppliermanual.html', {'supplier':supplier,
                                                                     'materials':materials, 'number':number, 'destinations': destinations})

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return:redirect('listDocumentSupplier')
        """
        materials = request.POST.getlist('materials')
        supplier = Supplier.objects.get(pk=pk)
        number = request.POST.get('number')
        destination = request.POST.get('destination')
        document = DocumentSupplier.objects.create(supplier=supplier, number=number, destination=destination)
        document.materials.set(materials)
        return redirect('listDocumentSupplier')


class ListDocumentSupplier(ListView):
    """
    PL: Generyczny widok listy obiektów DocumentSupplier.
    EN: DocumentSupplier Generic List View.
    """
    model = DocumentSupplier
    template_name = 'list.html'


class UpdateDocumentSupplier(LoginRequiredMixin, View):
    def get(self, request, pk):
        """
        :param request:
        :param pk:
        :return:render(request, 'updatedocumentsuppliermanual.html', context)
        """
        document = DocumentSupplier.objects.get(pk=pk)
        supplier = document.supplier
        materials = document.materials.all()
        destination = document.destination
        number = document.number
        materials_supplier = Material.objects.filter(supplier_id=supplier)
        destinations = ['Reklamacja', 'Zakup', 'Testy', 'Gratis']
        context = {'number' : number, 'supplier' : supplier, 'materials' : materials, 'destination' : destination,
                   'materials_supplier' : materials_supplier, 'destinations' : destinations}
        return render(request, 'updatedocumentsuppliermanual.html', context)

    def post(self, request, pk):
        """
        :param request:
        :param pk:
        :return:redirect('listDocumentSupplier')
        """
        materials = request.POST.getlist('materials')
        number = request.POST.get('number')
        destination = request.POST.get('destination')
        document = DocumentSupplier.objects.get(pk=pk)
        document.number = number
        document.destination = destination
        document.save()
        document.materials.set(materials)
        return redirect('listDocumentSupplier')


class DeleteDocumentSupplier(LoginRequiredMixin, DeleteView):
    """
    PL: Generyczny widok usuwania obiektu DocumentSupplier.
    EN: DocumentSupplier Generic Delete View.
    """
    model = DocumentSupplier
    template_name = 'delete.html'
    success_url = reverse_lazy('listDocumentSupplier')


class CreateGood(LoginRequiredMixin, View):
    def get(self, request):
        """
        :param request:
        :return:render(request, 'creategoodmanual.html', {'materials':materials})
        """
        materials = Material.objects.all()
        return render(request, 'creategoodmanual.html', {'materials':materials})

    def post(self, request):
        """
        :param request:
        :return:redirect('listGood')
        """
        name = request.POST.get('name')
        index = request.POST.get('index')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        if len(Material.objects.filter(index=index)) == 0 and len(Good.objects.filter(index=index)) == 0:
            pass
        else:
            materials = Material.objects.all()
            index_error = f'Indeks zajęty, proszę zweryfikować'
            return render(request, 'creategoodmanual.html', {'materials':materials, 'index_error':index_error} )
        materials = request.POST.getlist('materials')
        needs = []
        good = Good.objects.create(name=name, index=index, description=description, quantity=quantity)
        for info in materials:
            needs.append(int(request.POST.get(info)))
            GoodMaterial.objects.create(good=good, material=Material.objects.get(id=int(info)), needed=int(request.POST.get(info)))
        return redirect('listGood')



class ListGood(ListView):
    """
    PL: Generyczny widok listy obiektów Good.
    EN: Good Generic List View.
    """
    model = Good
    template_name = 'list.html'



class UpdateGood(LoginRequiredMixin, View):
    def get(self, request, pk):
        """

        :param request:
        :param pk:
        :return:render(request, 'updategoodmanual.html', {'good' : good,
                                                         'needs' : needs, 'rest_materials': rest_materials})
        """
        good = Good.objects.get(pk=pk)
        materials = good.material.all()
        needs = []
        material_all = Material.objects.all()
        rest_materials = []
        for material in material_all:
            if material in materials:
                pass
            else:
                rest_materials.append(material)
        for material in materials:
            needs.append((material, GoodMaterial.objects.get(good=good, material=material).needed))
        return render(request, 'updategoodmanual.html', {'good' : good,
                                                         'needs' : needs, 'rest_materials': rest_materials})

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return:redirect('listGood')
        """
        good = Good.objects.get(pk=pk)
        name = request.POST.get('name')
        index = request.POST.get('index')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        if len(Material.objects.filter(index=index)) == 0 and len(Good.objects.filter(index=index)) == 0:
            pass
        else:
            materials = Material.objects.all()
            index_error = f'Indeks zajęty, proszę zweryfikować'
            return render(request, 'creategoodmanual.html', {'rest_materials':materials, 'index_error':index_error, 'good':good} )
        good.name = name
        good.index = index
        good.description = description
        good.quantity = quantity
        materials = request.POST.getlist('materials')
        needs = []
        good.material.clear()
        for info in materials:
            needs.append(int(request.POST.get(info)))
            GoodMaterial.objects.create(good=good, material=Material.objects.get(id=int(info)), needed=int(request.POST.get(info)))
        return redirect('listGood')


class DeleteGood(LoginRequiredMixin, DeleteView):
    """
    PL: Generyczny widok usuwania obiektu Good.
    EN: Good Generic Delete View.
    """
    model = Good
    template_name = 'delete.html'
    success_url = reverse_lazy('listGood')


class CreateDocumentCustomer(LoginRequiredMixin, View):
    def get(self, request, pk):
        """

        :param request:
        :param pk:
        :return:render(request, 'createdocumentcustomermanual.html', {'customer':customer,
                                                                     'goods':goods, 'number':number, 'destinations': destinations})
        """
        customer = Customer.objects.get(pk=pk)
        goods = Good.objects.all()
        number = get_number_customer_document()
        destinations = ['Reklamacja', 'Sprzedaż', 'Testy', 'Gratis']
        return render(request, 'createdocumentcustomermanual.html', {'customer':customer,
                                                                     'goods':goods, 'number':number, 'destinations': destinations})

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return:redirect('listDocumentCustomer')
        """
        goods = request.POST.getlist('goods')
        customer = Customer.objects.get(pk=pk)
        number = request.POST.get('number')
        destination = request.POST.get('destination')
        document = DocumentCustomer.objects.create(customer=customer, number=number, destination=destination)
        document.good.set(goods)
        return redirect('listDocumentCustomer')


class ListDocumentCustomer(ListView):
    """
    PL: Generyczny widok listy obiektów DocumentCustomer.
    EN: DocumentCustomer Generic List View.
    """
    model = DocumentCustomer
    template_name = 'list.html'


class UpdateDocumentCustomer(LoginRequiredMixin, UpdateView):
    """
    PL: Generyczny widok aktualizacji obiektu DocumentCustomer.
    EN: DocumentCustomer Generic Update View.
    """
    model = DocumentCustomer
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('listDocumentCustomer')


class DeleteDocumentCustomer(LoginRequiredMixin, DeleteView):
    """
    PL: Generyczny widok usuwania obiektu DocumentCustomer.
    EN: DocumentCustomer Generic Delete View.
    """
    model = DocumentCustomer
    template_name = 'delete.html'
    success_url = reverse_lazy('listDocumentCustomer')


class TryPoduceGood(LoginRequiredMixin, View):
    def get(self, request, pk):
        """

        :param request:
        :param pk:
        :return:render(request, 'tryproduce.html', context)
        """
        good = Good.objects.get(pk=pk)
        materials = good.material.all()
        needs = []
        for material in materials:
            needs.append((material, GoodMaterial.objects.get(good=good, material=material).needed))
        context = {'good':good, 'needs':needs}
        return render(request, 'tryproduce.html', context)

    def post(self, request, pk):
        """

        :param request:
        :param pk:
        :return:render(request, 'tryproduce.html', context)
        """
        produce_quantity = int(request.POST.get('produce_quantity'))
        good = Good.objects.get(pk=pk)
        materials = good.material.all()
        needs = []
        error_needs = []
        for material in materials:
            needs.append((material, GoodMaterial.objects.get(good=good, material=material).needed))
        for element in needs:
            if element[0].quantity >= (element[1] * produce_quantity):
                pass
            else:
                error_needs.append(f'Za mała ilość {element[0].name}, zweryfikuj stan/zakup materiał. Potrzeba {element[1] * produce_quantity}, zabrakło {(element[1] * produce_quantity)-element[0].quantity}')
        if len(error_needs) > 0:
            context = {'good': good, 'needs': needs, 'error_needs': error_needs, 'produce_quantity': produce_quantity}
            return render(request, 'tryproduce.html', context)
        else:
            for element in needs:
                element[0].quantity = element[0].quantity - (element[1] * produce_quantity)
                element[0].save()
        good.quantity += produce_quantity
        good.save()
        context = {'message': f'Wyprodukowano {produce_quantity} szt.', 'needs': needs, 'good':good}
        return render(request, 'tryproduce.html', context)


# class UpdateDocumentSupplier(UpdateView):
#     model = DocumentSupplier
#     form_class = UpdateDocSupplierForm
#     form.fields['materials'].queryset = Material.objects.filter(supplier=model.supplier_id)
#     template_name = 'update.html'
#     success_url = reverse_lazy('listDocumentSupplier')
#
#
# class UpdateDocumentSupplier(UpdateView):
#     model = DocumentSupplier
#     form_class = UpdateDocSupplierForm
#     template_name = 'update.html'
#     success_url = reverse_lazy('listDocumentSupplier')


# class UpdateGood(LoginRequiredMixin, UpdateView):
#     model = Good
#     fields = '__all__'
#     template_name = 'update.html'
#     success_url = reverse_lazy('listGood')
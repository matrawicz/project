import datetime

from project.models import DocumentSupplier, DocumentCustomer


def get_number_supplier_document():
    try:
        last_number = DocumentSupplier.objects.last().id
        year = datetime.datetime.now().year
        return f'{last_number + 1}/{year}/SD'
    except:
        year = datetime.datetime.now().year
        return f'1/{year}/SD'


def get_number_customer_document():
    try:
        last_number = DocumentCustomer.objects.last().id
        year = datetime.datetime.now().year
        return f'{last_number + 1}/{year}/CD'
    except:
        year = datetime.datetime.now().year
        return f'1/{year}/CD'
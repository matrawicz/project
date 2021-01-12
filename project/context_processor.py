from django.utils.timezone import now


def first_context_processor(request):
    context = {
        'today' : now(),
        'author' : 'Mateusz Cichy',
        'version' : '1.01'
    }
    return context
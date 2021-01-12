from django.core.exceptions import ValidationError


def validate_len_nip(value):
    if len(value) != 10:
        raise ValidationError('Błąd ilości znaków')
    return value

def validate_symbols_nip(value):
    for i in value:
        if i not in ['1','2','3','4','5','6','7','8','9','0']:
            raise ValidationError('Wprowadzono literę bądź separator - proszę wprowadzić same cyfry!')
    return value


def validate_value_discount(value):
    if value > 35:
        raise ValidationError(f'Za duży rabat!')
    return value

# def validate_unique_index(value):
#     if Material.objects.filter(index=value) == [] and Good.objects.filter(index=value) == []:
#         return value
#     raise ValidationError(f'Indeks zajęty, proszę zweryfikować')

def validate_len_index(value):
    if value >= 1000000000 and value <= 9999999999:
        return value
    raise ValidationError(f'Indeks nie ma dokładnie 10 znaków lub jest zarezerwowany')

def validate_norm(value):
    if value == 0:
        raise ValidationError(f'Norma nie może wynosić 0!')
    return value
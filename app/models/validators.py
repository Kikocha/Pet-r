from django import forms


def min_value(value):
    if value < 0:
        raise forms.ValidationError('Value should be a positive number')
    return value


def contains_only_digits(value):
    for letter in value:
        if not letter.isdigit():
            raise forms.ValidationError('This filed should contain only digits')
    return value

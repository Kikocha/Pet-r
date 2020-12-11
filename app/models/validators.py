from django import forms


def min_months_value(value):
    if value < 0:
        raise forms.ValidationError('Months should be a positive number')
    return value


def max_months_value(value):
    if value > 200:
        raise forms.ValidationError('Months should be between 0 and 200')
    return value


def contains_only_digits(value):
    for letter in value:
        if not letter.isdigit():
            raise forms.ValidationError('This filed should contain only digits')
    return value

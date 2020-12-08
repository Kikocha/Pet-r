from django import forms


def max_value_years(value):
    if value > 100:
        raise forms.ValidationError('Years should be below 101')
    return value


def max_value_months(value):
    if value > 11:
        raise forms.ValidationError('Months should be below 12')
    return value


def max_value_weeks(value):
    if value > 4:
        raise forms.ValidationError('Weeks should be below 5')
    return value


def min_value(value):
    if value < 0:
        raise forms.ValidationError('Value should be a positive number')
    return value

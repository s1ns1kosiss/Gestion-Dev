from django import template

register = template.Library()

def clp_format(value):
    try:
        value = int(round(float(value)))
        return "$ {:,}".format(value).replace(",", ".")
    except (ValueError, TypeError):
        return value

register.filter('clp', clp_format) 
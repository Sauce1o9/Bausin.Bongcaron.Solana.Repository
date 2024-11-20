from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter
def attr(field, attributes):
    attrs = dict(item.split(":") for item in attributes.split(","))
    return field.as_widget(attrs=attrs)
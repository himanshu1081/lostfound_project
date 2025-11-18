from django import template
from tailwind.utils import compile_css

register = template.Library()

@register.simple_tag
def tailwind_css():
    return compile_css()

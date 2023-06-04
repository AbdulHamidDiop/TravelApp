from django import template

register = template.Library()
#used in the tripsfeed template to display each potss user
@register.filter
def getItem(dictionary, key):
    return dictionary.get(key)
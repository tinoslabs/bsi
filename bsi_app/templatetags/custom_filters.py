from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    print(f"get_item called with dictionary: {dictionary} and key: {key}")  
    return dictionary.get(key)

print(f"Registered filters: {register.filters}")  
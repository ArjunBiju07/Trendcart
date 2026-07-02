from django import template

register = template.Library()

@register.simple_tag(name = 'getstatus')
def getstatus(status):
    match(status):
        case 1:
            return "Confirmed"
        case 2:
            return "Processed"
        case 3:
            return "Deliverd"
        case 4:
            return "Rejected"
        case _:
            return "Error"
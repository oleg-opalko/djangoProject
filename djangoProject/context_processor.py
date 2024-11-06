from home.models import MenuItem
from django.utils.translation import gettext as _


def menu_context(request):
    menus = MenuItem.objects.filter(parent=None)
    return {'menus': menus}

def static_text(request):
    context = {
        'page_title': 'My Website',
        'home_page': 'Home Page',
    }
    return {
        'static_text': context
    }

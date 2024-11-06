from home.models import MenuItem
from django.utils.translation import gettext as _


def menu_context(request):
    menus = MenuItem.objects.filter(parent=None)
    return {'menus': menus}

def static_text(request):
    context = {
        'page_title': _('My Website'),
        'home_page': _('Home Page'),
        'english': _('English'),
        'ukrainian': _('Ukrainian'),
        'privacy_policy': _('Privacy Policy'),
        'terms_of_service': _('Terms of Service')
    }
    return {
        'static_text': context
    }

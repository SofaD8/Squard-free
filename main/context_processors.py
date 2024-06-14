"""
    View for providing the applications.
    Returns:
        dict: A dictionary containing the applications.
"""


def app_title(request):
    return {'app_title': '<span>Squadfree</span>'}


def app_hero_title(request):
    return {'app_hero_title': 'Welcome to Squad'}


def app_hero(request):
    return {'app_hero': 'We are team of talented designers making websites with Bootstrap'}


def app_about(request):
    return {'app_about': 'About us'}


def app_address(request):
    return {'app_address': 'A108 Adam Street, New York, NY 535022'}


def app_phone(request):
    return {'app_phone': '+1 5589 55488 55'}


def app_contact(request):
    return {'app_contact': 'contact@example.com'}


def app_info(request):
    return {'app_info': 'info@example.com'}


def app_title_cta(request):
    return {'app_title_cta': 'Call To Action'}


def app_cta(request):
    return {
        'app_cta': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum '
                   'dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, '
                   'sunt in culpa qui officia deserunt mollit anim id est laborum.'
    }


def app_button(request):
    return {'app_button': 'Call To Action'}

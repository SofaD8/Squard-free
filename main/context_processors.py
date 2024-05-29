"""
    View for providing the applications.
    Returns:
        dict: A dictionary containing the applications.
"""
def app_title(request):
    return {
        'app_title': '<span>Squadfree</span>'
    }


def app_address(request):
    return {
        'app_address': 'A108 Adam Street, New York, NY 535022'
    }


def app_phone(request):
    return {
        'app_phone': '+1 5589 55488 55'
    }


def app_contact(request):
    return {
        'app_contact': 'contact@example.com'
    }


def app_info(request):
    return {
        'app_info': 'info@example.com'
    }

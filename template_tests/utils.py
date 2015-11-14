from django.conf import settings

def get_template_dirs():
    try:
        templates = settings.TEMPLATES
    except AttributeError:
        templates = ()

    # settings.TEMPLATES can be missing /or/ empty due to both settings
    # existing in some releases.
    if templates:
        for x in templates:
            for y in x['DIRS']:
                yield y
    else:
        for x in settings.TEMPLATE_DIRS:
            yield x

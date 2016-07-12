from .base import *
import logging, copy
from django.utils.log import DEFAULT_LOGGING


DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

SECRET_KEY = 'u%nx#*fi-w1-8mb2h0r-t*poga81u+f$*jjo8ft%90z9&a%5qx'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# hide annoying deprecation errors
# http://stackoverflow.com/questions/29562070/how-to-suppress-the-deprecation-warnings-in-django/31103483#31103483
LOGGING = copy.deepcopy(DEFAULT_LOGGING)
LOGGING['filters']['suppress_deprecated'] = {
    '()': 'vannevar.settings.SuppressDeprecated'  
}
LOGGING['handlers']['console']['filters'].append('suppress_deprecated')

class SuppressDeprecated(logging.Filter):
    def filter(self, record):
        WARNINGS_TO_SUPPRESS = [
            'RemovedInDjango18Warning',
            'RemovedInDjango19Warning',
            'RemovedInDjango110Warning',
        ]
        # Return false to suppress message.
        return not any([warn in record.getMessage() for warn in WARNINGS_TO_SUPPRESS])




try:
    from .local import *
except ImportError:
    pass

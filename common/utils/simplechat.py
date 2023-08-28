from django.utils import timezone
from django.conf import settings 
from django.template.defaultfilters import date 

def datetime_message() -> tuple:
    datetime_object = timezone.now()
    datetime_format = date(datetime_object, settings.DATETIME_FORMAT)
    return datetime_object, datetime_format

#!/usr/bin/env python

import sys
import os
import django
import csv

# directory = os.path.abspath(os.path.join(os.path.dirname( __file__ ))) #, '..', 'myproject')
# sys.path.append(directory)
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
# django.setup()
#
# ## putting data into database using models
# # http://stackoverflow.com/questions/20794901/configuring-django
# # http://stackoverflow.com/questions/35584734/configuring-django-settings-after-moving-to-another-directory?rq=1
#
#
# # to avoid django.core.exceptions.ImproperlyConfigured: Requested setting DEFAULT_INDEX_TABLESPACE, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
# # http://stackoverflow.com/questions/20794901/configuring-django

def csv2djangomodel(fp = '../../../jam4changedata/committees.csv', model = 'Committees'):
    
    # # import module
    # module = __import__('models', fromlist=[model])
    # print module
    # print getattr(module, model)
    # obj = getattr(module, model)
    
    with open(fp, 'r') as f:
        reader = csv.DictReader(f, delimiter = '|')
        for row in reader:
            print row


if __name__ == '__main__':
    csv2djangomodel()
#!/usr/bin/env python

import sys
import os
import django
import csv

directory = os.path.abspath(os.path.join(os.path.dirname( __file__ ))) #, '..', 'myproject')
sys.path.append(directory)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

## putting data into database using models
# http://stackoverflow.com/questions/20794901/configuring-django
# http://stackoverflow.com/questions/35584734/configuring-django-settings-after-moving-to-another-directory?rq=1

def csv2djangomodel(fp = 'models_data.csv', model = 'Committee'):
    
    # import module
    module = __import__('models', fromlist=[model])
    print module
    print getattr(module, model)
    obj = getattr(module, model)
    
    with open(fp, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print row


if __name__ == '__main__':
    csv2djangomodel()
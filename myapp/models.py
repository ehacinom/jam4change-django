from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Committee(models.Model):
    
    CommitteeName = models.CharField(max_length = 100)
    CommitteeType = models.CharField(max_length = 8)
    Link = models.CharField(max_length = 250)
    Header = models.CharField(max_length = 200)
    Chair = models.CharField(max_length = 40)
    CoChair = models.CharField(max_length = 60)
    ViceChair = models.CharField(max_length = 100)
    CommitteeClerk = models.CharField(max_length = 80)
    LegislativeCouncilStaff = models.CharField(max_length = 50)
    Members = models.CharField(max_length = 450)
    OtherMembers = models.CharField(max_length = 150)
    Hearings = models.CharField(max_length = 2000)
    
    class Meta:
        db_table = "Committee"

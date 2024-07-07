from django.db import models
import uuid

class CompanyTable(models.Model):
    companyId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    companyName = models.CharField(max_length=100)
    companyLocation = models.CharField(max_length=500)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(("It", "IT"), ("Non-IT", "Non-IT"), ("mobile", "Mobile")))

    def __str__(self):
        return self.companyName

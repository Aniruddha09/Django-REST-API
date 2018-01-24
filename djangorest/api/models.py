from django.db import models

class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.user',
    related_name='bucketlists',
	null=True,
	on_delete=models.CASCADE )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    lastname = models.CharField(max_length=255,blank=False,null=True)
    location  = models.CharField(max_length=255,blank=False,null=True)
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

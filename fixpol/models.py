from django.db import models

# Create your models here.
class Location(models.Model):
    """A location helps filter which legislation to look at."""
    desc = models.CharField(max_length=80)
    shortname = models.CharField(max_length=20)
    hierarchy = models.CharField(max_length=200)
    govlevel = models.CharField(max_length=80)
    parent = models.ForeignKey('self', null=True, 
            related_name='child', on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.desc

class Impact(models.Model):
    """A location helps filter which legislation to look at."""
    text = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Profile(models.Model):
    """A profile holds the location and impact areas."""
    user = models.OneToOneField(User, on_delete=models.PROTECT, 
        related_name='profile')

    location = models.ForeignKey('Location', null=True,
        related_name='location', on_delete=models.SET_NULL)

    impacts = models.ManyToManyField(Location)





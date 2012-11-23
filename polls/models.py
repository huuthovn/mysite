from django.db import models
from django.utils import timezone
#from django.utils.encoding import force_unicode
import datetime

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')        
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
<<<<<<< HEAD
    
=======
     
>>>>>>> d8871be3ecf852411f7eb57494ce796405c86f63
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __str__(self):
        return self.choice_text

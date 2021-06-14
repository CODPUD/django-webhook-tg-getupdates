from django.db import models

# Create your models here.
class user_tg(models.Model):
    chat_id = models.IntegerField()
    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return "%r" % self.chat_id
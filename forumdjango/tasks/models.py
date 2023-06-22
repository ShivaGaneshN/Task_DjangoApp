from django.db import models

# Create your models here.
class Task(models.Model):
    class Meta(object):
        db_table = 'task'
    taskname = models.CharField('Taskname', blank=False, null=False, max_length=14, db_index=True, default='Anonymous')
    taskbody = models.CharField('Taskbody', blank=True, null=True, max_length=140, db_index=True)
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
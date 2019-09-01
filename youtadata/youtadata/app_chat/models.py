from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model
import jdatetime


User = get_user_model()


class Chat(models.Model):
    message = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    code = models.TextField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    create_datetime = models.DateTimeField(auto_now_add=True, null=True)
    seen_datetime = models.DateTimeField(null=True)
    seen  = models.BooleanField(null=True, default=False)
    
    def jd_create_datetime(self):
        jdatetime.set_locale('fa_IR')
        jdatetime.datetime.now().strftime('%A %B')
        jd_datetime = jdatetime.datetime.fromgregorian(
             year = self.create_datetime.year(),
             month = self.create_datetime.month(),
             hour = self.create_datetime.hour(),
             minute = self.create_datetime.minute(),
             second = self.create_datetime.second()
            )
        return dj_datetime.strftime("%A, %d %B %y %H:%M:%S")

    @property
    def is_student(self):
        return 'students' in [group.name for group in self.user.groups.all()]

    
    def __str__(self):
        return self.message[:30]

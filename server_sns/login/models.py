from django.db import models

# Create your models here.

class loginUser(models.Model):

   user_id = models.CharField(max_length=20, unique=True, null=False, default=False)
   user_pw = models.CharField(max_length=256, null=False, default=False)

   class Meta :
       db_table = 'login_user'
       verbose_name = '로그인 테스트 테이블'
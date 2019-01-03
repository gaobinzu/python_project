from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class User(models.Model):
#     '''用户模型类'''
#     sys_root = (
#         (0, '普通用户'),
#         (1, '超级用户')
#     )
#     username =models.CharField(max_length=30, verbose_name='用户名')
#     password = models.CharField(max_length=130, verbose_name='密码')
#     is_active = models.BooleanField(default=False, verbose_name='是否激活')
#     root = models.SmallIntegerField(choices=sys_root, default=0, verbose_name='用户权限')
#
#     class Meta:
#         db_table = 'df_user'
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name


class User(AbstractUser, BaseModel):
    '''用户模型类'''

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

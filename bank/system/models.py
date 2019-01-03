from django.db import models


class Opeartion_log(models.Model):
    operation = models.CharField(max_length=50, verbose_name='操作详情')
    operate_time = models.DateTimeField(null=False)
    # handlers = models.ForeignKey('user.User', verbose_name='操作者', on_delete=models.CASCADE)
    username = models.CharField(max_length=20, verbose_name='用户名')
    remark = models.CharField(max_length=100,verbose_name='备注')
    hostname = models.CharField(max_length=20, verbose_name='主机名称', null=True)
    ip = models.CharField(max_length=20, verbose_name='ip地址', null=True)
    # operate_pro = models.ForeignKey('project_management.Project', verbose_name='项目ID',on_delete=models.CASCADE)

    class Meta:
        db_table = 'operation_log'
        verbose_name = '操作日志'
        verbose_name_plural = verbose_name



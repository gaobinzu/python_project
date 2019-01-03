from db.base_model import BaseModel
from django.db import models


class Project(models.Model):
    p_num = models.CharField(max_length=10, verbose_name='项目编号')
    p_name = models.CharField(max_length=20, verbose_name='项目名称')
    p_start_time = models.DateField(null=False)
    p_stop_time = models.DateField(null=True)
    p_user = models.ForeignKey('user.User', verbose_name='项目负责人', on_delete=models.CASCADE)

    class Meta:
        db_table = 'project'
        verbose_name = '项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.p_name


class Project_dateils(models.Model):
    type_ = (
        (0, '计划'),
        (1, '实际'),
    )
    type = models.SmallIntegerField(choices=type_, default=0)
    analysis = models.CharField(max_length=20)  # 分析阶段
    design = models.CharField(max_length=20)  # 设计阶段
    realize = models.CharField(max_length=20)  # 实现阶段
    SIT_jd = models.CharField(max_length=20)  # SIT
    UAT_jd = models.CharField(max_length=20)  # UAT
    verify = models.CharField(max_length=20)  # 验证阶段
    online = models.CharField(max_length=20)  # 上线
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    class Meta:
        db_table = 'project_dateils'
        verbose_name = '项目详情'
        verbose_name_plural = verbose_name


class Pro_dateils_jihua(models.Model):
    project_jh = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='项目计划')
    pro_name = models.CharField(max_length=30, verbose_name='项目阶段名称')  # 项目阶段名称
    pro_start_time = models.DateField(verbose_name='项目阶段开始时间')  # 开始时间
    pro_stop_time = models.DateField(verbose_name='项目阶段完成时间')  # 结束时间
    pro_desc = models.CharField(max_length=100, verbose_name='项目阶段描述')  # 项目阶段描述

    class Meta:
        db_table = 'pro_dateils_jihua'
        verbose_name = '项目详情-计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pro_name

class Pro_dateils_shiji(models.Model):
    project_sj = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='项目实际进展')
    pro_name = models.CharField(max_length=30, verbose_name='项目阶段名称')  # 项目阶段名称
    pro_start_time = models.DateField(verbose_name='项目阶段开始时间')  # 实际开始时间
    pro_stop_time = models.DateField(verbose_name='项目阶段完成时间')  # 实际结束时间
    pro_start_time_jh = models.DateField(verbose_name='项目阶段开始时间', null=True)  # 计划开始时间
    pro_stop_time_jh = models.DateField(verbose_name='项目阶段开始时间', null=True)  # 计划结束时间
    pro_desc = models.CharField(max_length=100, verbose_name='项目阶段描述')  # 项目阶段描述


    class Meta:
        db_table = 'pro_dateils_shiji'
        verbose_name = '项目详情-实际'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pro_name
#coding:utf-8
from django.db import models

# Create your models here.
# from django.contrib.auth.models import AbstractUser

class wy_user(models.Model):
    user_name = models.CharField(u'用户名',max_length=10,unique=True)
    phonenumber = models.CharField(u'电话号码',max_length=20,)

    class Meta():
        ordering = ['-user_name']
        verbose_name = u"用户"
        verbose_name_plural = u"用户"
    def __unicode__(self):
        return self.user_name

class homework(models.Model):
    owner = models.ForeignKey(wy_user,related_name="CODEUSER",verbose_name=u"拥有者")
    desc = models.CharField(u'描述',max_length=100)
    # link = models.CharField(max_length=200,)
    link = models.FileField(u'文件',upload_to="./media/uploads")
    comment = models.TextField(u'评论',default=u"暫無評論")
    create_time = models.DateTimeField(u'提交时间',auto_now_add=True)
    class Meta():
        ordering = ['-pk']
        verbose_name = u"代码作业"
        verbose_name_plural = u"代码作业"
    def __unicode__(self):
        return self.owner.user_name+self.desc
class design(models.Model):
    owner = models.ForeignKey(wy_user,related_name="DESIGNUSER",verbose_name=u"拥有者")
    desc = models.CharField(u'描述',max_length=100)
    # link = models.CharField(max_length=200,)
    link = models.FileField(u'文件',upload_to="./media/uploads")
    comment = models.TextField(u'评论',default=u"暫無評論")
    create_time = models.DateTimeField(u'提交时间',auto_now_add=True)
    class Meta():
        ordering = ['-pk']
        verbose_name = u"设计作业"
        verbose_name_plural = u"设计作业"
    def __unicode__(self):
        return self.owner.user_name+self.desc
class newhomework(models.Model):
    owner = models.CharField(max_length=100,verbose_name="部门")
    desc = models.CharField(u'简介',max_length=100)
    # link = models.CharField(max_length=200,)
    link = models.FileField(u'文件',upload_to="./media/uploads")
    comment = models.TextField(u'详情',default=u"暫無")
    class Meta():
        ordering = ['-pk']
        verbose_name = u"布置新作业"
        verbose_name_plural = u"布置新作业"
    def __unicode__(self):
        return self.desc

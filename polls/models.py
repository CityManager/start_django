from django.db import models

# Create your models here.


class Question(models.Model):  # 一个继承models.Model对象的类 代表一个模型,即一张表
    question_text = models.CharField(max_length=200)  # Field对象为字段,变量名为字段名
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

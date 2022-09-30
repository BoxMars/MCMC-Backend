from django.db import models

# Create your models here.
class token(models.Model):
    token=models.CharField(max_length=64, default="")
    notes=models.TextField()

class news(models.Model):
    title=models.CharField(max_length=1024,default="")
    pic_url=models.CharField(max_length=1024,default="")
    news_url=models.CharField(max_length=1024,default="")
    submit_by=models.CharField(max_length=1024,default="")

    def info(self):
        res={
            'title':self.title,
            'pic_url':self.pic_url,
            'news_url':self.news_url
        }
        return res
class head_num(models.Model):
    num=models.IntegerField(default=6)
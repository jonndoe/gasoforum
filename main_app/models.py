# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GasTheme(models.Model):
    #just the name of learning theme about gascarriers
    text = models.CharField(max_length=200)
    sub_text = models.CharField(max_length=200)
    order = models.CharField(max_length=3)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    photo = models.ImageField(upload_to="pictures", blank=True)
    
    def __str__(self):
    #returns string represantation of the text
        return self.text


class GasTopic(models.Model):
    #just the name of random topic about gas carriers
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    avatar = models.ImageField(upload_to = "pictures", blank=True)
    def __str__(self):
        if len(self.text) < 25:
            return self.text
        else:
            return self.text[:25] + "..."


class GasThemeText(models.Model):
    # this is the main text of particular GasTheme
    gas_theme = models.ForeignKey(GasTheme)
    order = models.CharField(max_length=3)
    title = models.CharField(max_length=50, default='no')
    subtitle = models.CharField(max_length=50, default='no')
    text = models.TextField(default='no')
    date_added = models.DateTimeField(auto_now_add=True)
    
    photo = models.ImageField(upload_to = "pictures", blank=True)
    photo_text = models.CharField(max_length=300, default='no')
    photo2 = models.ImageField(upload_to = "pictures", blank=True)
    photo2_text = models.CharField(max_length=300, default='no')
    photo3 = models.ImageField(upload_to = "pictures", blank=True)
    photo3_text = models.CharField(max_length=300, default='no')

    class Meta:
        verbose_name_plural = 'gas_theme_textes'
  
    def __str__(self):
        #return string represantation of the model
        return self.text


class GasTopicText(models.Model):
    # this is the main text of particular GasTopic
    gas_topic = models.ForeignKey(GasTopic)
    order = models.CharField(max_length=3, default='1')
    title = models.CharField(max_length=50,default='no')
    subtitle = models.CharField(max_length=50,default='no')
    text = models.TextField(default='текст абзаца')
    date_added = models.DateTimeField(auto_now_add=True)


    photo = models.ImageField(upload_to = "pictures", blank=True)
    photo_text = models.CharField(max_length=300, default='no')
    photo2 = models.ImageField(upload_to = "pictures", blank=True)
    photo2_text = models.CharField(max_length=300, default='no')
    photo3 = models.ImageField(upload_to = "pictures", blank=True)
    photo3_text = models.CharField(max_length=300, default='no')

    class Meta:
        verbose_name_plural = 'gas_topic_textes'
  
    def __str__(self):
        #return string represantation of the model
        return self.text[:50] + '...'


class GasThemeComment(models.Model):
    # comments for particular gasthemetext
    gas_topic = models.ForeignKey(GasTheme)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'gas_theme_comments'

    def __str__(self):
        #return string represantation of the model
        return self.text


class GasThemeCommentReply(models.Model):
    # reply for comments
    gasthemecomment = models.ForeignKey(GasThemeComment)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name_plural = 'gas_theme_comments_replyies'

    def __str__(self):
        # return string represantation of the model
        return self.text


class GasTopicComment(models.Model):
    # comments for particular gasTopic
    gas_topic = models.ForeignKey(GasTopic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'gas_topic_comments'

    def __str__(self):
        #return string represantation of the model
        return self.text


class PhotoAlbum(models.Model):
    # photoalbum class which will contain a bunch of single photos
    owner = models.ForeignKey(User)
    text = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to = "pictures", blank=True)
    date_added = models.DateTimeField(default=timezone.now())
    def __str__(self):
        #return string represantation of the model
        return self.text


class Photo(models.Model):

    photoalbum = models.ForeignKey(PhotoAlbum)
    owner = models.ForeignKey(User)
    picture = models.ImageField(upload_to = "pictures")
    text = models.CharField(max_length=200, default='text')
    date_added = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.text




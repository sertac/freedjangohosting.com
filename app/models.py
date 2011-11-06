from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
#yto

STATUS = (
    ('DRAFT', 'DRAFT'),
    ('PUBLISHED', 'PUBLISHED'),
)


TYPE = (
    ('FREE', 'FREE'),
    ('PAID', 'PAID'),
)


class Hosting(models.Model):
   name = models.CharField(max_length=100)
   website = models.URLField(verify_exists=True,blank=True,null=True)
   description=models.TextField(blank=True,null=True)
   status=models.CharField(max_length=15,choices=STATUS,default='DRAFT')
   type=models.CharField(max_length=15,choices=TYPE,default='PAID')
   logo=models.ImageField(upload_to='uploads/logo',blank=True,null=True)
   num_of_users= models.PositiveSmallIntegerField(default=0)
   add_date=models.DateTimeField(auto_now_add=True,editable=False)
   update_date=models.DateTimeField(auto_now=True,auto_now_add=True,editable=False)
   
   class Meta:
     ordering = ["-num_of_users"]

   def __unicode__(self):
      return u'%s' % (self.name)
   
   def get_absolute_url(self):
      return '/%s' % slugify(self.name)

class Vote(models.Model):
    hosting=models.ForeignKey(Hosting)   
    ip=models.IPAddressField()
    add_date=models.DateTimeField(auto_now_add=True,editable=False)

class Feedback(models.Model):
    hosting=models.ForeignKey(Hosting)   
    name = models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    comment=models.TextField()
    ip=models.IPAddressField()
    add_date=models.DateTimeField(auto_now_add=True,editable=False)

    def __unicode__(self):
      return u'%s' % (self.comment)


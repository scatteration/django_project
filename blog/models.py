from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name="Baslik Giriniz",
                             help_text="Baslik Bilgisi Burada Girilir.")
    icerik = models.TextField(max_length=1000, blank=False, null=True, verbose_name="Icerik Giriniz")
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    class Meta:
        verbose_name ="Blog"
        ordering = ['title']

    def __str__(self):
        return "%s" % (self.title)
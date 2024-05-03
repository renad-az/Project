from django.bd import models

class Quot(models.Model):
  author = modls.CharField(max_length=50)
  text = models.TextField()
  data = models.DataField()

  def __str__(self):
    return self.author

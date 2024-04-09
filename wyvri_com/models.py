from django.db import models

class Art(models.Model):
    fileName = models.ImageField(upload_to="art/")
    desc = models.CharField(max_length=200,null=True)

    def __str__(self) -> str:
        return f"{self.fileName}, {self.desc}"
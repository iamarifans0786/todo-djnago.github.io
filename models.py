from django.db import models

# Create your models here.


class todo_list(models.Model):
    title=models.CharField(max_length=200)
    check_status=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

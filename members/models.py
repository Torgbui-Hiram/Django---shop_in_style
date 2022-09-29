from django.db import models




class NewUser(models.Model):
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    username = models.CharField('Username', max_length=30)
    email = models.EmailField('User email', blank=True, null=True)
    birth_date = models.DateField('Birth date')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

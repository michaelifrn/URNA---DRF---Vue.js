from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=32, default='')
    number = models.IntegerField(primary_key = True, default=0)
    registration = models.IntegerField(default= 0)

    def __str__(self):
        return f'Nome: {self.name} | Número: {self.number} | Matrícula: {self.registration}'


class Vote(models.Model):
    registration = models.IntegerField(default=0)
    number = models.ForeignKey(Candidate, on_delete=models.PROTECT, related_name="votes")

    def __str__(self):
        return f'Matrícula: {self.registration}'

class Voters(models.Model):
    reg = models.IntegerField(default=0)
    status = models.BooleanField(default=False)


    def __str__(self):
        return f'Matrícula: {self.reg} | Voted: {self.status}'
    
    class Meta:
        verbose_name = "Voter"
        db_table = "Voter"
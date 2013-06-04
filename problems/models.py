from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    hidden = models.BooleanField()
    max_score = models.IntegerField()


def getFileName(subtask, filename):
    return '/'.join(['problems', subtask.problem.id, subtask.num])

class Subtask(models.Model):
    name = models.CharField(max_length=100)
    problem = models.ManyToManyField(Problem)
    hidden = models.BooleanField()
    num = models.IntegerField()
    correct = models.FileField(upload_to=getFileName)

class Submissions(models.Model):
    score = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    problem = models.ForeignKey(Problem)
    #user = models.ForeignKey(User)

    # None here indicates success
    failed = models.IntegerField(default=None)
    output = models.TextField(default=None)

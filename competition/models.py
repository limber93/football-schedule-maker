from django.db import models

class Competition(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Match(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    home_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='away_team')
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

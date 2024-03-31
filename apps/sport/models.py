from django.db import models

# Create your models here.


class Sport(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Chempionship(models.Model):
    name = models.CharField(max_length=128)
    sport = models.ForeignKey(
        Sport, on_delete=models.CASCADE, related_name="chempionship"
    )

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="teams")
    chempionships = models.ManyToManyField(Chempionship)

    def __str__(self):
        return self.name


class Match(models.Model):
    # date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='matches')
    chempionship = models.ForeignKey(Chempionship, on_delete=models.CASCADE)
    team_1 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="matches_as_1"
    )
    team_2 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="matches_as_2"
    )
    winner = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="matches_as_win"
    )

    def __str__(self):
        return f"{self.team_1} - {self.team_2}"


class Rating(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="ratings")
    chempionship = models.ForeignKey(Chempionship, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return f"{self.team} - {self.rating} - {self.chempionship}"

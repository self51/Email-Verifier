"""EmailVerifier's model."""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class History(models.Model):
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=30, blank=False)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'History for {0} is ({1}) with score: {2}'.format(
            self.email, self.status, self.score,
        )

    class Meta:
        verbose_name_plural = 'Histories'

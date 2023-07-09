from django.db import models
from users.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.name} made a payment on {self.payment_date}"

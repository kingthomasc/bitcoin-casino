from django.db import models
from django.contrib.auth.models import User
from django_bitcoin.models import BitcoinAddress, new_bitcoin_address, Wallet
import random
import string

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length="500")
    phone_number = models.CharField(max_length="100")
    secret_code = models.CharField(max_length="50")
    bitcoin_address = models.OneToOneField(BitcoinAddress, blank=True)
    balance = models.DecimalField(max_digits=16, decimal_places=8)
    
    def save(self, *args, **kwargs):
        if not self.address:
            address = new_bitcoin_address()
            wallet = Wallet.objects.get(label='master')
            wallet.addresses.add(address)
            wallet.save()
            self.address = address
        if not self.secret_code:
            self.secret_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
        super(UserProfile, self).save(*args, **kwargs)
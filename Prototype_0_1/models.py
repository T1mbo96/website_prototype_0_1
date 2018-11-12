from django.db import models
from django.contrib.auth.models import User


class PhoneToll(models.Model):
    telekom = models.DecimalField
    vodafone = models.DecimalField
    o2 = models.DecimalField
    international_flat = models.BooleanField


class Provider(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    Logo = models.ImageField

    def __str__(self):
        return self.name


class Advantage(models.Model):
    online = models.DecimalField
    cashback = models.DecimalField


class Price(models.Model):
    advantage_id = models.ForeignKey(Advantage, verbose_name="advantage id", on_delete=None)
    first_six_month = models.DecimalField
    second_six_month = models.DecimalField
    third_six_month = models.DecimalField
    fourth_six_month = models.DecimalField
    shipping = models.DecimalField
    willing_commitment_fee = models.DecimalField
    several_numbers = models.DecimalField
    average_price = models.DecimalField


class Contract(models.Model):
    CONNECTION_TYPE = (
        ('K', 'Cable'),
        ('D', 'DSL'),
        ('S', 'Satellite'),
        ('G', 'Glass Fibre'),
        ('L', 'LTE/UMTS'),
        ('W', 'WiMAX')
    )

    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name="provider id")
    price_id = models.ForeignKey(Price, verbose_name="price id", on_delete=None)
    phone_toll_id = models.ForeignKey(PhoneToll, verbose_name="phone toll id", on_delete=None)
    name = models.CharField(max_length=250)
    download_rate = models.DecimalField
    upload_rate = models.DecimalField
    young = models.BooleanField
    minimum_term = models.CharField(max_length=250)
    internet_flat = models.BooleanField
    phone_flat = models.BooleanField
    tv_flat = models.BooleanField
    connection_typ = models.CharField(max_length=1, choices=CONNECTION_TYPE)
    renewal = models.CharField(max_length=250)
    call_by_call = models.BooleanField
    throttling = models.CharField(max_length=250)
    throttling_rate = models.CharField(max_length=250)
    desired_schedule = models.CharField(max_length=250)
    product_information = models.URLField
    provider_information = models.CharField(max_length=250)
    wlan_modem = models.BooleanField
    surfstick = models.BooleanField
    installation_service = models.BooleanField
    email_mailboxes = models.CharField(max_length=250)
    url = models.URLField
    advise = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class RemainingTerm(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user id")
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name="contract id")
    end_date = models.DateField


class Rating(models.Model):
    STARS = (
        ('1', '*'),
        ('2', '**'),
        ('3', '***'),
        ('4', '****'),
        ('5', '*****'),
    )
    user_id = models.ForeignKey(User, verbose_name="user id", on_delete=models.CASCADE)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name="contract id")
    stars = models.CharField(max_length=1, choices=STARS)


class Comment(models.Model):
    text = models.TextField(max_length=250)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE, verbose_name="rating id")


class SearchQuery(models.Model):
    STATES = (
        ('BW', 'Baden-Württemberg'),
        ('BY', 'Bayern'),
        ('BE', 'Berlin'),
        ('BB', 'Brandenburg'),
        ('HB', 'Bremen'),
        ('HH', 'Hamburg'),
        ('HE', 'Hessen'),
        ('MV', 'Mecklenburg-Vorpommern'),
        ('NI', 'Niedersachsen'),
        ('NW', 'Nordrhein-Westfalen'),
        ('RP', 'Rheinland-Pfalz'),
        ('SL', 'Saarland'),
        ('SN', 'Sachsen'),
        ('ST', 'Sachsen-Anhalt'),
        ('SH', 'Schleswig-Holstein'),
        ('TH', 'Thüringen'),
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user_id')
    state = models.CharField(max_length=2, choices=STATES)
    place = models.CharField(max_length=30)
    zip = models.IntegerField(default=0000)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

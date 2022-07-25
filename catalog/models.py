from django.db import models


class Features(models.Model):
    exchange_id = models.CharField(max_length=200)
    feature_name = models.CharField(max_length=200)
    feature_value = models.CharField(max_length=200)


class Inventories(models.Model):
    exchange_id = models.CharField(max_length=200)
    inventories_name = models.CharField(max_length=200)
    vendor_code = models.OneToOneField('VendorCodes', on_delete=models.CASCADE)
    feature = models.ForeignKey('Features', on_delete=models.CASCADE)
    property = models.ManyToManyField(
        Features,
        through='Properties',
        through_fields=('inventories', 'features')
    )


class VendorCodes(models.Model):
    vendor_code_company = models.CharField(max_length=20)
    vendor_code_supplier = models.CharField(max_length=20)


class Properties(models.Model):
    exchange_id = models.CharField(max_length=200)
    inventories = models.ForeignKey(Inventories, on_delete=models.CASCADE)
    features = models.ForeignKey(Features, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=200)


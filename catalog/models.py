from django.db import models


class PropertyName(models.Model):
    property_name = models.CharField(max_length=200)

    def __str__(self):
        return self.property_name


class Properties(models.Model):
    name = models.ForeignKey('PropertyName', on_delete=models.CASCADE)
    property_value = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}: {self.property_value}'


class PropertySet(models.Model):
    exchange_id = models.CharField(max_length=200)
    property_set_name = models.CharField(max_length=200)
    properties = models.ManyToManyField('Properties')

    def __str__(self):
        j = str()
        k = self.properties.all()
        for i, item in enumerate(k):
            j += str(item)
            if i != len(k) - 1:
                j += '; '
        return f'{j}'


class FeatureName(models.Model):
    exchange_id = models.CharField(max_length=200)
    feature_name = models.CharField(max_length=200)

    def __str__(self):
        return self.feature_name


class Features(models.Model):
    name = models.ForeignKey('FeatureName', on_delete=models.CASCADE)
    feature_value = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return f'{self.name}: {self.feature_value}'


class Inventories(models.Model):
    exchange_id = models.CharField(max_length=200)
    inventory_name = models.CharField(max_length=200)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    features = models.ManyToManyField('Features')
    property_set = models.ManyToManyField('PropertySet')
    vendor_codes = models.OneToOneField('VendorCodes', on_delete=models.CASCADE)

    def __str__(self):
        return self.inventory_name


class VendorCodes(models.Model):
    vendor_code_company = models.CharField(max_length=20)
    vendor_code_supplier = models.CharField(max_length=20)

    def __str__(self):
        return self.vendor_code_company


class GroupPath(models.Model):
    ancestor = models.ForeignKey('Group', null=True, db_column='ancestor', blank=True, related_name="ancestor", on_delete=models.CASCADE)
    descendant = models.ForeignKey('Group', null=True, db_column='descendant', blank=True, related_name="descendants", on_delete=models.CASCADE)
    path_length = models.IntegerField(null=True, db_column='PathLength', blank=True)

    class Meta:
        db_table = u'GroupPath'


class Group(models.Model):
    exchange_id = models.CharField(max_length=200)
    group_name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name='children', on_delete=models.CASCADE)
    group_path = models.ManyToManyField('Group', through='GroupPath', through_fields=('ancestor', 'descendant'))

    class Meta:
        db_table = u'Group'

    def __str__(self):
        return self.group_name

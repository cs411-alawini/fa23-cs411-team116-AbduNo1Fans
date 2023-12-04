# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Crimefilter(models.Model):
    username = models.OneToOneField('Users', models.DO_NOTHING, db_column='Username', primary_key=True)  # Field name made lowercase. The composite primary key (Username, crime_code) found, that is not supported. The first column is selected.
    crime_code = models.ForeignKey('Crimetype', models.DO_NOTHING, db_column='crime_code')

    class Meta:
        managed = False
        db_table = 'CrimeFilter'
        unique_together = (('username', 'crime_code'),)


class Crimetype(models.Model):
    crime_code = models.IntegerField(primary_key=True)
    crime_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CrimeType'


class Crimes(models.Model):
    dr_no = models.IntegerField(primary_key=True)
    date_occ = models.DateField(blank=True, null=True)
    time_occ = models.TimeField(blank=True, null=True)
    crime_code = models.ForeignKey(Crimetype, models.DO_NOTHING, db_column='crime_code', blank=True, null=True)
    weapon_code = models.ForeignKey('Weapontype', models.DO_NOTHING, db_column='weapon_code', blank=True, null=True)
    premis_code = models.ForeignKey('Premistype', models.DO_NOTHING, db_column='premis_code', blank=True, null=True)
    vict_age = models.IntegerField(blank=True, null=True)
    vict_sex = models.CharField(max_length=255, blank=True, null=True)
    vict_descent = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Crimes'


class Premisfilter(models.Model):
    username = models.OneToOneField('Users', models.DO_NOTHING, db_column='Username', primary_key=True)  # Field name made lowercase. The composite primary key (Username, premis_code) found, that is not supported. The first column is selected.
    premis_code = models.ForeignKey('Premistype', models.DO_NOTHING, db_column='premis_code')

    class Meta:
        managed = False
        db_table = 'PremisFilter'
        unique_together = (('username', 'premis_code'),)


class Premistype(models.Model):
    premis_code = models.IntegerField(primary_key=True)
    premis_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PremisType'


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'


class Views(models.Model):
    view_id = models.IntegerField(primary_key=True)
    longitude = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Views'


class Weaponfilter(models.Model):
    username = models.OneToOneField(Users, models.DO_NOTHING, db_column='Username', primary_key=True)  # Field name made lowercase. The composite primary key (Username, weapon_code) found, that is not supported. The first column is selected.
    weapon_code = models.ForeignKey('Weapontype', models.DO_NOTHING, db_column='weapon_code')

    class Meta:
        managed = False
        db_table = 'WeaponFilter'
        unique_together = (('username', 'weapon_code'),)


class Weapontype(models.Model):
    weapon_code = models.IntegerField(primary_key=True)
    weapon_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WeaponType'

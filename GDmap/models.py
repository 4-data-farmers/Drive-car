from django.db import models


class Car(models.Model):
    车辆编号 = models.IntegerField(primary_key=True)
    soc值 = models.FloatField(db_column='SOC值', blank=True, null=True)  # Field name made lowercase.
    soh值 = models.FloatField(db_column='SOH值', blank=True, null=True)  # Field name made lowercase.
    起始位置 = models.CharField(max_length=1, blank=True, null=True)
    目的位置 = models.CharField(max_length=1, blank=True, null=True)
    充电到达充电桩编号 = models.IntegerField(blank=True, null=True)
    开始行使时间 = models.TimeField(blank=True, null=True)
    结束行使时间 = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car'


class Chargingstation(models.Model):
    充电站编号 = models.IntegerField(primary_key=True)
    经度 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    纬度 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chargingstation'
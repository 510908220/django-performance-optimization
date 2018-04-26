from django.db import models

# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True
    created = models.DateTimeField(auto_now_add=True)


class City(BaseModel):
    class Meta:
        db_table = "city"
    name = models.CharField(max_length=30,  unique=True)

    def __str__(self):
        return self.name


class House(BaseModel):
    class Meta:
        db_table = "house"
    HEATING_METHODS = (
        ('concentrated', '集中供暖'),
        ('selfburning', '自烧锅炉'),
    )
    city = models.ForeignKey(City, related_name='houses')
    name = models.CharField(max_length=30,  unique=True)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=255)  # 地址
    area = models.PositiveIntegerField()  # 占地面积
    parking_spaces = models.PositiveIntegerField()  # 车位数
    property_company = models.CharField(max_length=255)  # 物业公司
    property_costs = models.PositiveIntegerField()  # 物业费用
    heating_method = models.CharField(choices=HEATING_METHODS,
                                      default=HEATING_METHODS[0][0],
                                      max_length=20)

    def __str__(self):
        return "{}-{}".format(self.city.name, self.name)

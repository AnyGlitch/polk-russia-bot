from tortoise import Model
from tortoise.fields import IntField, TextField, TimeField

__all__ = ["HikingModel"]


class HikingModel(Model):
    id = IntField(pk=True)
    city = TextField()
    location = TextField()
    time = TimeField()

    class Meta:
        table = "hiking"

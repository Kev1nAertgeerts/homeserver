from django.db import models

# Create your models here.
class GeneratorField(models.Field):
    description = "A field to store generators"

    def __init__(self, *args, **kwargs):
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'TextField'

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return eval(value)

    def to_python(self, value):
        if isinstance(value, str):
            return eval(value)
        return value

    def get_prep_value(self, value):
        if value is None:
            return None
        return repr(value)

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    generator_field = GeneratorField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generator = None

    def save(self, *args, **kwargs):
        if self.generator:
            # Converting the generator to a list before saving
            self.generator_field = list(self.generator)
        super().save(*args, **kwargs)
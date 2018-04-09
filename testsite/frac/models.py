from django.db import models

# Create your models here.
class Project(models.Model):
    customer_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cr = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Well(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project, related_name='wells', on_delete=models.CASCADE)
    total_stages = models.PositiveIntegerField()
    total_wi = models.DecimalField(default=0, blank=True, decimal_places=3, max_digits=10)
    has_water_tracers = models.BooleanField(default=False)
    has_water_global = models.BooleanField(default=False)
    has_oil_tracers = models.BooleanField(default=False)
    has_gas_tracers = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Tracer(models.Model):
    phase = models.CharField(max_length=30, choices=(
                                ('W', 'Water'),
                                ('WG', 'Water Global'),
                                ('O', 'Oil'),
                                ('G', 'Gas'),
    ))
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Injection(models.Model):
    phase = models.CharField(max_length=30, choices=(
                                ('W', 'Water'),
                                ('WG', 'Water Global'),
                                ('O', 'Oil'),
                                ('G', 'Gas'),
    ))
    grams_injected = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    stage = models.PositiveIntegerField()
    tracer = models.ForeignKey(Tracer, related_name='injections', on_delete=models.CASCADE)
    tracer_alias = models.CharField(max_length=30)
    well = models.ForeignKey(Well, related_name='injections', on_delete=models.CASCADE)

    def __str__(self):
        return 'W{0}:STG{1}'.format(self.well.name, self.stage)
    # injection_start = models.DateTimeField()
    # injection_end = models.DateTimeField()
    # injection_details as a separate model? (itag data)

class Sample(models.Model):
    datetime = models.DateTimeField()
    well = models.ForeignKey(Well, related_name='samples', on_delete=models.CASCADE)
    reference = models.CharField(max_length=30)
    phase = models.CharField(max_length=30, choices=(
                                ('W', 'Water'),
                                ('O', 'Oil'),
                                ('G', 'Gas'),
    ))

class Analysis(models.Model):
    sample = models.ForeignKey(Sample, related_name='analyses', on_delete=models.CASCADE)
    tracer = models.ForeignKey(Tracer, on_delete=models.CASCADE)
    ppb_raw = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    # updated_by

class ProdData(models.Model):
    well = models.ForeignKey(Well, related_name='production_data', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    whp = models.DecimalField(blank=True, decimal_places=3, max_digits=10)
    choke = models.DecimalField(blank=True, decimal_places=3, max_digits=10)
    cum_oil = models.DecimalField(blank=True, decimal_places=3, max_digits=10)
    cum_wat = models.DecimalField(blank=True, decimal_places=3, max_digits=10)
    cum_gas = models.DecimalField(blank=True, decimal_places=3, max_digits=10)
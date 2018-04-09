# Generated by Django 2.0.4 on 2018-04-09 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppb_raw', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Injection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.CharField(choices=[('W', 'Water'), ('WG', 'Water Global'), ('O', 'Oil'), ('G', 'Gas')], max_length=30)),
                ('grams_injected', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('stage', models.PositiveIntegerField()),
                ('tracer_alias', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProdData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('whp', models.DecimalField(blank=True, decimal_places=3, max_digits=10)),
                ('choke', models.DecimalField(blank=True, decimal_places=3, max_digits=10)),
                ('cum_oil', models.DecimalField(blank=True, decimal_places=3, max_digits=10)),
                ('cum_wat', models.DecimalField(blank=True, decimal_places=3, max_digits=10)),
                ('cum_gas', models.DecimalField(blank=True, decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('cr', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('reference', models.CharField(max_length=30)),
                ('phase', models.CharField(choices=[('W', 'Water'), ('O', 'Oil'), ('G', 'Gas')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tracer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.CharField(choices=[('W', 'Water'), ('WG', 'Water Global'), ('O', 'Oil'), ('G', 'Gas')], max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('total_stages', models.PositiveIntegerField()),
                ('total_wi', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10)),
                ('has_water_tracers', models.BooleanField(default=False)),
                ('has_water_global', models.BooleanField(default=False)),
                ('has_oil_tracers', models.BooleanField(default=False)),
                ('has_gas_tracers', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wells', to='frac.Project')),
            ],
        ),
        migrations.AddField(
            model_name='sample',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='frac.Well'),
        ),
        migrations.AddField(
            model_name='proddata',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_data', to='frac.Well'),
        ),
        migrations.AddField(
            model_name='injection',
            name='tracer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='injections', to='frac.Tracer'),
        ),
        migrations.AddField(
            model_name='injection',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='injections', to='frac.Well'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analyses', to='frac.Sample'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='tracer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frac.Tracer'),
        ),
    ]

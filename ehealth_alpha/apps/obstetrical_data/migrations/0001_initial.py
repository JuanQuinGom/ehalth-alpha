# Generated by Django 3.1.6 on 2021-02-15 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Obstetricos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parejas_sexuales', models.IntegerField()),
                ('gestas_previas', models.IntegerField()),
                ('partos', models.IntegerField()),
                ('abortos', models.IntegerField()),
                ('cesareas', models.IntegerField()),
                ('vaginales', models.IntegerField()),
                ('nacidos_vivos', models.IntegerField()),
                ('viven', models.IntegerField()),
                ('folio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personal_data.datos_personas')),
            ],
        ),
    ]

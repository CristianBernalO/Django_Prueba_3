# Generated by Django 4.1.2 on 2024-07-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id_navbar', models.AutoField(db_column='idNavbar', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='quienesSomos',
            fields=[
                ('id_quienes_somos', models.AutoField(db_column='idQuienesSomos', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('cuerpo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(db_column='idServicio', primary_key=True, serialize=False)),
                ('nombre_servicio', models.CharField(max_length=50)),
                ('tipo_servicio', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('nombre_imagen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonios',
            fields=[
                ('id_testimonio', models.AutoField(db_column='idTestimonio', primary_key=True, serialize=False)),
                ('nombre_persona', models.CharField(max_length=100)),
                ('testimonio', models.TextField()),
            ],
        ),
    ]

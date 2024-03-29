# Generated by Django 2.2.2 on 2019-07-10 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190619_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10, unique=True)),
                ('modelo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='automoviles')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca')),
            ],
            options={
                'verbose_name': 'Productos',
            },
        ),
    ]

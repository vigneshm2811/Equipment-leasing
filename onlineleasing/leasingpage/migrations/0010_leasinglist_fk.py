# Generated by Django 4.0.1 on 2022-03-11 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leasingpage', '0009_leasinglist_containers_id_alter_leasinglist_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='leasinglist',
            name='fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leasingpage.container'),
        ),
    ]

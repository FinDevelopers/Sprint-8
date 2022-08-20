# Generated by Django 4.0.6 on 2022-08-20 20:50

from django.db import migrations
import random

def relacion_empleado_user(apps, schema_editor):
    Empleado = apps.get_model('Clientes', 'Empleado')
    User = apps.get_model('auth', 'User')
    for empleado in Empleado.objects.all():
        username = f'{empleado.employee_name}{empleado.employee_surname}{str(empleado.employee_id)}'
        email = f'{username}@gmail.com'
        password = str(random.randint(10000000, 99999999))
        user = User.objects.create_user(username, email, password)
        user.first_name = empleado.employee_name
        user.last_name = empleado.employee_surname
        user.save()
        empleado.user = user
        empleado.save()

class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0027_empleado_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'managed': True, 'ordering': ['employee_id'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleadosssss'},
        ),
        migrations.RunPython(relacion_empleado_user)
    ]
# Generated by Django 3.0 on 2019-12-10 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import request.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('ref_code', models.CharField(default=request.models.random_string, editable=False, max_length=30, unique=True)),
                ('time_edited', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Progress', 'In Progress'), ('Complete', 'Complete'), ('On Hold', 'On Hold'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50)),
                ('assign_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AssgnedToGroup', to='auth.Group')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('author_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
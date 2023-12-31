# Generated by Django 4.2.2 on 2023-06-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(db_index=True, default='Anonymous', max_length=14, verbose_name='Taskname')),
                ('taskbody', models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='Taskbody')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]

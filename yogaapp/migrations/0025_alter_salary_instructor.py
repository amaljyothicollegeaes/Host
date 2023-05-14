# Generated by Django 4.1.1 on 2023-04-30 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yogaapp', '0024_alter_salary_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='instructor',
            field=models.ForeignKey(limit_choices_to={'user__id': models.F('courses__user_id')}, on_delete=django.db.models.deletion.CASCADE, to='yogaapp.registeredinstructor'),
        ),
    ]

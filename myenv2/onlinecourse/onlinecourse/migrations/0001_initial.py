# Generated by Django 5.0.2 on 2024-02-16 09:15

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='online course', max_length=30)),
                ('image', models.ImageField(upload_to='course_images/')),
                ('description', models.CharField(max_length=1000)),
                ('pub_date', models.DateField(null=True)),
                ('total_enrollment', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField(default=django.utils.timezone.now)),
                ('mode', models.CharField(choices=[('audit', 'Audit'), ('honor', 'Honor'), ('BETA', 'BETA')], default='audit', max_length=5)),
                ('rating', models.FloatField(default=5.0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(through='onlinecourse.Enrollment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_time', models.BooleanField(default=True)),
                ('total_learners', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='onlinecourse.instructor'),
        ),
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(choices=[('student', 'Student'), ('developer', 'Developer'), ('data_scientist', 'Data Scientist'), ('dba', 'Database Admin')], default='student', max_length=20)),
                ('social_link', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=200)),
                ('order', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('grade', models.IntegerField(default=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='onlinecourse.choice')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.enrollment')),
            ],
        ),
    ]

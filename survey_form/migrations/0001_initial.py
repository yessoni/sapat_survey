# Generated by Django 4.2 on 2023-04-12 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=255)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_form.category')),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_name', models.CharField(max_length=255)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_form.category')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_form.channel')),
            ],
        ),
        migrations.CreateModel(
            name='ServayEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionId', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_form.area')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_survey', to='survey_form.shows')),
            ],
        ),
    ]
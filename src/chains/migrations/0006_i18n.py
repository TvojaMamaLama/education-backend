# Generated by Django 3.2.12 on 2022-03-19 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_CourseDisplayInLMS'),
        ('chains', '0005_MessageAdminSpeedup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chain',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='chain',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='chain',
            name='sending_is_active',
            field=models.BooleanField(default=False, verbose_name='Sending is active'),
        ),
        migrations.AlterField(
            model_name='message',
            name='chain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chains.chain', verbose_name='Chain'),
        ),
        migrations.AlterField(
            model_name='message',
            name='delay',
            field=models.BigIntegerField(default=0, help_text='86400 for day, 604800 for week', verbose_name='Delay (minutes)'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='message',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='Messages without parent will be sent upon start', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='chains.message', verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='message',
            name='template_id',
            field=models.CharField(max_length=256, verbose_name='Template id'),
        ),
    ]
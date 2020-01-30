# Generated by Django 2.2.3 on 2020-01-10 05:05

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0006_auto_20191122_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfindinglink',
            name='references',
            field=tinymce.models.HTMLField(blank=True, help_text='Provide solid references for this finding, such as links to reference materials, tooling, and white papers', null=True, verbose_name='References'),
        ),
    ]
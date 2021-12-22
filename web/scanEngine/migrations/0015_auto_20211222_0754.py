# Generated by Django 3.2.4 on 2021-12-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0014_remove_installedexternaltool_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installedexternaltool',
            name='subdomain_extra_command',
        ),
        migrations.RemoveField(
            model_name='installedexternaltool',
            name='subdomain_output_command',
        ),
        migrations.RemoveField(
            model_name='installedexternaltool',
            name='subdomain_proxy_command',
        ),
        migrations.RemoveField(
            model_name='installedexternaltool',
            name='subdomain_target_command',
        ),
        migrations.AddField(
            model_name='installedexternaltool',
            name='github_clone_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='installedexternaltool',
            name='is_github_cloned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='installedexternaltool',
            name='subdomain_gathering_command',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

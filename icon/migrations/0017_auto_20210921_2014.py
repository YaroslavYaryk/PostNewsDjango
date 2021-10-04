# Generated by Django 3.2.7 on 2021-09-21 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('icon', '0016_alter_likedcomment_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='woman',
            name='views',
        ),
        migrations.AlterField(
            model_name='woman',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('post_news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ip', to='icon.woman')),
            ],
        ),
    ]

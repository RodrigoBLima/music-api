# Generated by Django 3.2.7 on 2021-10-02 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('playlist', '0001_initial'),
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='playlist.album'),
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together={('album', 'order')},
        ),
    ]

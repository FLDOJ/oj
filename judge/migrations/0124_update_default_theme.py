# Generated by Django 2.2.24 on 2021-12-26 02:07

from django.db import migrations, models


def set_default_ace_theme(apps, schema_editor):
    Profile = apps.get_model('judge', 'Profile')
    Profile.objects.filter(ace_theme='github').update(ace_theme='tomorrow')


def unset_default_ace_theme(apps, schema_editor):
    Profile = apps.get_model('judge', 'Profile')
    Profile.objects.filter(ace_theme='tomorrow').update(ace_theme='github')


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0123_auto_20211225_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ace_theme',
            field=models.CharField(choices=[('ambiance', 'Ambiance'), ('chaos', 'Chaos'), ('chrome', 'Chrome'), ('clouds', 'Clouds'), ('clouds_midnight', 'Clouds Midnight'), ('cobalt', 'Cobalt'), ('crimson_editor', 'Crimson Editor'), ('dawn', 'Dawn'), ('dreamweaver', 'Dreamweaver'), ('eclipse', 'Eclipse'), ('github', 'Github'), ('idle_fingers', 'Idle Fingers'), ('katzenmilch', 'Katzenmilch'), ('kr_theme', 'KR Theme'), ('kuroir', 'Kuroir'), ('merbivore', 'Merbivore'), ('merbivore_soft', 'Merbivore Soft'), ('mono_industrial', 'Mono Industrial'), ('monokai', 'Monokai'), ('pastel_on_dark', 'Pastel on Dark'), ('solarized_dark', 'Solarized Dark'), ('solarized_light', 'Solarized Light'), ('terminal', 'Terminal'), ('textmate', 'Textmate'), ('tomorrow', 'Tomorrow'), ('tomorrow_night', 'Tomorrow Night'), ('tomorrow_night_blue', 'Tomorrow Night Blue'), ('tomorrow_night_bright', 'Tomorrow Night Bright'), ('tomorrow_night_eighties', 'Tomorrow Night Eighties'), ('twilight', 'Twilight'), ('vibrant_ink', 'Vibrant Ink'), ('xcode', 'XCode')], default='tomorrow', max_length=30),
        ),
        migrations.RunPython(set_default_ace_theme, unset_default_ace_theme),
    ]

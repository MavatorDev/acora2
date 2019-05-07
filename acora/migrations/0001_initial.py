# Generated by Django 2.2 on 2019-04-17 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('codigo', models.CharField(default='0', max_length=20, primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=False)),
                ('temporizador', models.TimeField(default='50:00')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('idRanking', models.CharField(default='0', max_length=200, primary_key=True, serialize=False)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acora.Partida')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('cod', models.CharField(default='0', max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('puntaje', models.IntegerField(default=0)),
                ('idPista', models.CharField(default='0', max_length=20)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acora.Partida')),
            ],
        ),
    ]
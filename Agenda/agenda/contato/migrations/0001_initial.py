# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('contato_id', models.AutoField(serialize=False, primary_key=True)),
                ('contato_nome', models.CharField(max_length=45)),
                ('contato_nascimento', models.DateField()),
                ('contato_sexo', models.CharField(max_length=50, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')])),
                ('contato_estado_civil', models.CharField(max_length=50, verbose_name=b'Estado Civil', choices=[('solteiro', 'Solteiro'), ('casado', 'Casado'), ('divorciado', 'Divorciado'), ('viuvo', 'Viuvo')])),
                ('contato_email', models.CharField(max_length=50)),
                ('contato_favorito', models.BooleanField(verbose_name=b'Favorito')),
            ],
        ),
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('tarefa_id', models.AutoField(serialize=False, primary_key=True)),
                ('tarefa_nome', models.CharField(max_length=120)),
                ('tarefa_data_inicio', models.DateField()),
                ('conclusao', models.BooleanField(verbose_name=b'Concluido')),
            ],
        ),
    ]

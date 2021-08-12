# Generated by Django 3.2.5 on 2021-08-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Tarefa')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('end_date', models.DateField(verbose_name='Data final')),
                ('priority', models.CharField(choices=[('B', 'Baixa'), ('M', 'Média'), ('A', 'Alta')], max_length=1, verbose_name='Prioridade')),
                ('status', models.CharField(choices=[('EX', 'Em execução'), ('PD', 'Pendente'), ('CD', 'Concluída')], max_length=2, verbose_name='status')),
                ('category', models.ManyToManyField(to='tasks.Category')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
                'ordering': ['id'],
            },
        ),
    ]

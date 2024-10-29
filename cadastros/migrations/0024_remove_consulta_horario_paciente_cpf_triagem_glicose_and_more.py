# Generated by Django 5.1.2 on 2024-10-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0023_paciente_usuario_cadastrador_alter_paciente_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='horario',
        ),
        migrations.AddField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='cpf'),
        ),
        migrations.AddField(
            model_name='triagem',
            name='glicose',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='glicose'),
        ),
        migrations.AddField(
            model_name='triagem',
            name='peso',
            field=models.FloatField(default='00000000000', verbose_name='peso_corporal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triagem',
            name='temperatura',
            field=models.FloatField(default='00000000000', verbose_name='temperatura'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero_sus',
            field=models.CharField(max_length=15, verbose_name='numero_sus'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sintomas',
            field=models.CharField(max_length=150, verbose_name='sintomas'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefone',
            field=models.CharField(max_length=11, verbose_name='telefone'),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='horario',
            field=models.DateTimeField(verbose_name='horario'),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-29 14:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0026_alter_triagem_data_alter_triagem_horario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remedio', models.CharField(max_length=255, verbose_name='remedio')),
                ('diagnostico', models.TextField(max_length=255, verbose_name='diagnostico')),
                ('recomendacoes', models.TextField(blank=True, max_length=255, null=True, verbose_name='recomendacoes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('catalogo', '0001_initial')]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=150)),
                ('fecha_publicacion', models.DateField()),
            ],
            options={'ordering': ['titulo']},
        ),
    ]

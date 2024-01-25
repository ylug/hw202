from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='count_of_views',
            field=models.IntegerField(default=0, verbose_name='количество просмотров'),
        ),
    ]
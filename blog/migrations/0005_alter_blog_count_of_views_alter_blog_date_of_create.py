from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_blogpost_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='count_of_views',
            field=models.PositiveIntegerField(default=0, verbose_name='количество просмотров'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_of_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]
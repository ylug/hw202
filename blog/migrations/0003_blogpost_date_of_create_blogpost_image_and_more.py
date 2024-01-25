from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_count_of_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date_of_create',
            field=models.DateTimeField(auto_now=True, verbose_name='дата создания'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='изображение'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='post_content',
            field=models.TextField(blank=True, null=True, verbose_name='содержимое'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='publication_sign',
            field=models.BooleanField(default=True, verbose_name='признак публикации'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default='', max_length=100, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='заголовок'),
        ),
    ]
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение')),
                ('price', models.IntegerField(verbose_name='цена за покупку')),
                ('date_making', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('date_changing', models.DateTimeField(auto_now_add=True, verbose_name='дата последнег оизменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category',
                                               verbose_name='категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]

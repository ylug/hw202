from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_date_of_create_blogpost_image_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Blog',
        ),
    ]
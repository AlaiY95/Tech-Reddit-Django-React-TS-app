# Generated by Django 4.0.4 on 2022-04-18 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('weight', models.CharField(choices=[('IMPORTANT', 'Important'), ('LITTLE', 'Little'), ('KINDA_RELATES', 'Kinda Relates')], default='KINDA_RELATES', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
        migrations.AlterModelManagers(
            name='post',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(through='post.CategoryPost', to='category.category'),
        ),
        migrations.AddField(
            model_name='categorypost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
        migrations.AlterUniqueTogether(
            name='categorypost',
            unique_together={('post_id', 'category_id')},
        ),
    ]
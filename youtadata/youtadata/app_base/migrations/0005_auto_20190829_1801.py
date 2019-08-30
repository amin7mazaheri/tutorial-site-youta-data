# Generated by Django 2.1.5 on 2019-08-29 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app_base', '0004_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attach-files/%y-%m-%d_%H:%M')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('aparat_video', models.TextField(null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_base.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='attachmentsfiles',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='sessioncourse',
            name='course',
        ),
        migrations.AlterField(
            model_name='coursesessionexercise',
            name='course_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_base.CourseSession'),
        ),
        migrations.RenameModel(
            old_name='SessionExercise',
            new_name='CourseSessionExercise',
        ),
        migrations.DeleteModel(
            name='AttachmentsFiles',
        ),
        migrations.DeleteModel(
            name='SessionCourse',
        ),
    ]
# Generated by Django 4.2 on 2023-04-17 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Position adi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Position haqqinda')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Hirponorms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255, verbose_name='Bacariq')),
                ('skilltype', models.CharField(blank=True, choices=[('Soft', 'Soft'), ('Hard', 'Hard')], max_length=5, null=True, verbose_name='skilltype')),
                ('department', models.CharField(max_length=255, verbose_name='Department')),
                ('position', models.CharField(max_length=255, verbose_name='Position')),
                ('norm', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MainSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Bacariq adi')),
                ('skilltype', models.CharField(blank=True, choices=[('Soft', 'Soft'), ('Hard', 'Hard')], max_length=5, null=True, verbose_name='skilltype')),
                ('description', models.TextField(blank=True, null=True)),
                ('norm', models.PositiveIntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.departmentposition')),
            ],
            options={
                'verbose_name': 'Main SKill',
                'verbose_name_plural': 'Main Skills',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255, verbose_name='Project adi')),
                ('employee_number', models.PositiveIntegerField(verbose_name='Isci sayi')),
                ('industry', models.CharField(choices=[('IT', 'IT'), ('Construction', 'Construction')], max_length=30, verbose_name='Company field')),
                ('companyLeader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.allscores')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.mainskill')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Department adi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Department haqqinda')),
                ('employee_number', models.PositiveIntegerField(blank=True, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='wizard.project')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_number', models.PositiveSmallIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('period_position', models.CharField(blank=True, max_length=150, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='period', to='wizard.project')),
            ],
            options={
                'verbose_name': 'Period',
                'verbose_name_plural': 'Periods',
            },
        ),
        migrations.CreateModel(
            name='Evaluation_frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frequency', to='wizard.period')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='User adi')),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='User soyadi')),
                ('salary', models.PositiveIntegerField(blank=True, null=True)),
                ('hire_date', models.DateField(auto_now_add=True, null=True)),
                ('is_systemadmin', models.BooleanField(blank=True, default=False, null=True)),
                ('positionName', models.CharField(blank=True, max_length=40, null=True)),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='wizard.departmentposition', verbose_name='position level')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='wizard.project')),
                ('report_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wizard.employee')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ['-position'],
            },
        ),
        migrations.AddField(
            model_name='departmentposition',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departmentpositions', to='wizard.projectdepartment'),
        ),
        migrations.AddField(
            model_name='departmentposition',
            name='report_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wizard.departmentposition'),
        ),
        migrations.AddField(
            model_name='allscores',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myscore', to='wizard.employee'),
        ),
        migrations.AddField(
            model_name='allscores',
            name='evaluation_frequency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='freq', to='wizard.evaluation_frequency'),
        ),
        migrations.AddField(
            model_name='allscores',
            name='rater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycomment', to='wizard.employee'),
        ),
    ]

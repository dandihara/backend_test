# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class Answer(models.Model):
    question = models.ForeignKey('Question', models.CASCADE, blank=True, null=True)
    content = models.TextField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'answer'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.CASCADE)
    permission = models.ForeignKey('AuthPermission', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.CASCADE)
    group = models.ForeignKey(AuthGroup, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.CASCADE)
    permission = models.ForeignKey(AuthPermission, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClinicalNote(models.Model):
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_note'


class Concept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=255, blank=True, null=True)
    domain_id = models.CharField(max_length=20, blank=True, null=True)
    vocabulary_id = models.CharField(max_length=20, blank=True, null=True)
    concept_class_id = models.CharField(max_length=20, blank=True, null=True)
    standard_concept = models.CharField(max_length=1, blank=True, null=True)
    concept_code = models.CharField(max_length=50, blank=True, null=True)
    valid_start_date = models.DateField(blank=True, null=True)
    valid_end_date = models.DateField(blank=True, null=True)
    invalid_reason = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concept'


class ConditionOccurrence(models.Model):
    condition_occurrence_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey('Person', models.CASCADE, blank=True, null=True)
    condition_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True,related_name='condition_concept')
    condition_start_date = models.DateField(blank=True, null=True)
    condition_start_datetime = models.DateTimeField(blank=True, null=True)
    condition_end_date = models.DateField(blank=True, null=True)
    condition_end_datetime = models.DateTimeField(blank=True, null=True)
    condition_type_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True, related_name='condition_type')
    condition_status_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True , related_name='condition_status')
    stop_reason = models.CharField(max_length=20, blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', models.CASCADE, blank=True, null=True, related_name='visit_occurrence')
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    condition_source_value = models.CharField(max_length=50, blank=True, null=True)
    condition_source_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True , related_name='condition_source')
    condition_status_source_value = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condition_occurrence'


class Death(models.Model):
    person = models.ForeignKey('Person', models.CASCADE, blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    death_datetime = models.DateTimeField(blank=True, null=True)
    death_type_concept_id = models.IntegerField(blank=True, null=True)
    cause_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True,related_name='cause_concept')
    cause_source_value = models.IntegerField(blank=True, null=True)
    cause_source_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True, related_name='cause_source_concept')

    class Meta:
        managed = False
        db_table = 'death'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DrugExposure(models.Model):
    drug_exposure_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey('Person', models.CASCADE, blank=True, null=True)
    drug_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True,related_name='drug_concept')
    drug_exposure_start_date = models.DateField(blank=True, null=True)
    drug_exposure_start_datetime = models.DateTimeField(blank=True, null=True)
    drug_exposure_end_date = models.DateField(blank=True, null=True)
    drug_exposure_end_datetime = models.DateTimeField(blank=True, null=True)
    verbatim_end_date = models.DateField(blank=True, null=True)
    drug_type_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True, related_name='drug_type_concept')
    stop_reason = models.CharField(max_length=20, blank=True, null=True)
    refills = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_supply = models.IntegerField(blank=True, null=True)
    sig = models.TextField(blank=True, null=True)
    route_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True, related_name='route_concept')
    lot_number = models.CharField(max_length=50, blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', models.CASCADE, blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    drug_source_value = models.CharField(max_length=50, blank=True, null=True)
    drug_source_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True)
    route_source_value = models.CharField(max_length=50, blank=True, null=True)
    dose_unit_source_value = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_exposure'


class DrugPair(models.Model):
    drug_concept_id1 = models.IntegerField(blank=True, null=True)
    drug_concept_id2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_pair'


class Orders(models.Model):
    user_id = models.CharField(max_length=100)
    buy_count = models.IntegerField()
    order_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'orders'


class Orderss(models.Model):
    user_id = models.CharField(max_length=100)
    buy_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orderss'


class Person(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    gender_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True,related_name='gender_concept')
    year_of_birth = models.IntegerField(blank=True, null=True)
    month_of_birth = models.IntegerField(blank=True, null=True)
    day_of_birth = models.IntegerField(blank=True, null=True)
    birth_datetime = models.DateTimeField(blank=True, null=True)
    race_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True, related_name='race_concept')
    ethnicity_concept_id = models.IntegerField(blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.BigIntegerField(blank=True, null=True)
    person_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_concept_id = models.IntegerField(blank=True, null=True)
    race_source_value = models.CharField(max_length=50, blank=True, null=True)
    race_source_concept_id = models.IntegerField(blank=True, null=True)
    ethnicity_source_value = models.CharField(max_length=50, blank=True, null=True)
    ethnicity_source_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'question'


class Users(models.Model):
    user_id = models.CharField(max_length=100)
    user_level = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'


class VisitOccurrence(models.Model):
    visit_occurrence_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey(Person, models.CASCADE, blank=True, null=True)
    visit_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True, related_name='visit_concept')
    visit_start_date = models.DateField(blank=True, null=True)
    visit_start_datetime = models.DateTimeField(blank=True, null=True)
    visit_end_date = models.DateField(blank=True, null=True)
    visit_end_datetime = models.DateTimeField(blank=True, null=True)
    visit_type_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True, related_name='visit_type_concept')
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.BigIntegerField(blank=True, null=True)
    visit_source_value = models.CharField(max_length=50, blank=True, null=True)
    visit_source_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True, related_name='visit_source_concept')
    admitted_from_concept_id = models.IntegerField(blank=True, null=True)
    admitted_from_source_value = models.CharField(max_length=50, blank=True, null=True)
    discharge_to_source_value = models.CharField(max_length=50, blank=True, null=True)
    discharge_to_concept = models.ForeignKey(Concept, models.CASCADE, blank=True, null=True,related_name='discharge_to_concept')
    preceding_visit_occurrence = models.ForeignKey('self', models.CASCADE, blank=True, null=True, related_name='preceding_isiti_occurrence')

    class Meta:
        managed = False
        db_table = 'visit_occurrence'

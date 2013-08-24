# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Businessid(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.TextField(blank=True)
    address = models.TextField()
    address2 = models.TextField(blank=True)
    addresscity = models.TextField(db_column='addressCity') # Field name made lowercase.
    addressstate = models.TextField(db_column='addressState') # Field name made lowercase.
    addresszip = models.IntegerField(db_column='addressZip') # Field name made lowercase.
    joindate = models.DateField(null=True, db_column='joinDate', blank=True) # Field name made lowercase.
    visits = models.IntegerField(null=True, blank=True)
    cuisine = models.IntegerField(null=True, blank=True)
    corerating = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='coreRating', blank=True) # Field name made lowercase.
    offrating = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='offRating', blank=True) # Field name made lowercase.
    waitressrating = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='waitressRating', blank=True) # Field name made lowercase.
    dealsoffered = models.IntegerField(null=True, db_column='dealsOffered', blank=True) # Field name made lowercase.
    lowage = models.IntegerField(null=True, db_column='lowAge', blank=True) # Field name made lowercase.
    highage = models.IntegerField(null=True, db_column='highAge', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'businessID'

class Businessvisitdb(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    startdatetime = models.DateTimeField(null=True, db_column='startDateTime', blank=True) # Field name made lowercase.
    enddatetime = models.DateTimeField(null=True, db_column='endDateTime', blank=True) # Field name made lowercase.
    userid = models.IntegerField(null=True, db_column='userID', blank=True) # Field name made lowercase.
    waitressid = models.IntegerField(null=True, db_column='waitressID', blank=True) # Field name made lowercase.
    businessrating = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='businessRating', blank=True) # Field name made lowercase.
    waitressrating = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='waitressRating', blank=True) # Field name made lowercase.
    businessid = models.IntegerField(null=True, db_column='businessID', blank=True) # Field name made lowercase.
    businessratingnotes = models.TextField(db_column='businessRatingNotes', blank=True) # Field name made lowercase.
    businessdealid = models.IntegerField(null=True, db_column='businessDealID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'businessVisitDB'

class Cuisineid(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    cuisine = models.TextField(blank=True)
    visits = models.IntegerField()
    visitsbyage1017 = models.IntegerField(db_column='visitsbyAge1017') # Field name made lowercase.
    visitsbyage1823 = models.IntegerField(db_column='visitsByAge1823') # Field name made lowercase.
    visitsbyage2430 = models.IntegerField(db_column='visitsByAge2430') # Field name made lowercase.
    visitsbyage3140 = models.IntegerField(db_column='visitsByAge3140') # Field name made lowercase.
    visitsbyage4150 = models.IntegerField(db_column='visitsByAge4150') # Field name made lowercase.
    visitsbyage5165 = models.IntegerField(db_column='visitsByAge5165') # Field name made lowercase.
    visitsbyage66120 = models.IntegerField(db_column='visitsByAge66120') # Field name made lowercase.
    class Meta:
        db_table = 'cuisineID'

class Dealdb(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    businessid = models.IntegerField(null=True, db_column='businessID', blank=True) # Field name made lowercase.
    dealtype = models.TextField(db_column='dealType', blank=True) # Field name made lowercase.
    dealamount = models.TextField(db_column='dealAmount', blank=True) # Field name made lowercase.
    startdatetime = models.DateTimeField(null=True, db_column='startDateTime', blank=True) # Field name made lowercase.
    enddatetime = models.DateTimeField(null=True, db_column='endDateTime', blank=True) # Field name made lowercase.
    daysavailable = models.TextField(db_column='daysAvailable') # Field name made lowercase.
    timesavailable = models.TextField(db_column='timesAvailable') # Field name made lowercase.
    minratings = models.IntegerField(db_column='minRatings') # Field name made lowercase.
    mintips = models.IntegerField(db_column='minTips') # Field name made lowercase.
    dineoutfrequency = models.IntegerField(db_column='dineOutFrequency') # Field name made lowercase.
    weekdaysonly = models.BooleanField(db_column='weekdaysOnly') # Field name made lowercase.
    weekendsonly = models.BooleanField(db_column='weekendsOnly') # Field name made lowercase.
    cuisineonly = models.BooleanField(db_column='cuisineOnly') # Field name made lowercase.
    distance = models.IntegerField()
    targetage = models.BooleanField(db_column='targetAge') # Field name made lowercase.
    reviewratings = models.IntegerField(db_column='reviewRatings') # Field name made lowercase.
    spendratings = models.IntegerField(db_column='spendRatings') # Field name made lowercase.
    class Meta:
        db_table = 'dealDB'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class Ratingsdb(models.Model):
    userid = models.IntegerField(primary_key=True, db_column='userID') # Field name made lowercase.
    reviewrating = models.IntegerField(null=True, db_column='reviewRating', blank=True) # Field name made lowercase.
    spendrating = models.IntegerField(null=True, db_column='spendRating', blank=True) # Field name made lowercase.
    tiprating = models.IntegerField(null=True, db_column='tipRating', blank=True) # Field name made lowercase.
    rating = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'ratingsDB'

class Userid(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.TextField()
    joindate = models.DateField(db_column='joinDate') # Field name made lowercase.
    visits = models.IntegerField(null=True, blank=True)
    gender = models.TextField(blank=True)
    address = models.TextField()
    address2 = models.TextField(blank=True)
    addresscity = models.TextField(db_column='addressCity') # Field name made lowercase.
    addressstate = models.TextField(db_column='addressState') # Field name made lowercase.
    addresszip = models.IntegerField(db_column='addressZip') # Field name made lowercase.
    rating = models.IntegerField()
    lastvisit = models.DateField(null=True, db_column='lastVisit', blank=True) # Field name made lowercase.
    topcuisine1 = models.IntegerField(null=True, db_column='topCuisine1', blank=True) # Field name made lowercase.
    topcuisine2 = models.IntegerField(null=True, db_column='topCuisine2', blank=True) # Field name made lowercase.
    topcuisine3 = models.IntegerField(null=True, db_column='topCuisine3', blank=True) # Field name made lowercase.
    topcuisine4 = models.IntegerField(null=True, db_column='topCuisine4', blank=True) # Field name made lowercase.
    topcuisine5 = models.IntegerField(null=True, db_column='topCuisine5', blank=True) # Field name made lowercase.
    dealsparticipatedin = models.IntegerField(db_column='dealsParticipatedIn') # Field name made lowercase.
    privateoffersparticipatedin = models.IntegerField(db_column='privateOffersParticipatedIn') # Field name made lowercase.
    privateofferssent = models.IntegerField(db_column='privateOffersSent') # Field name made lowercase.
    toprestaurant1 = models.IntegerField(db_column='topRestaurant1') # Field name made lowercase.
    toprestaurant2 = models.IntegerField(db_column='topRestaurant2') # Field name made lowercase.
    toprestaurant3 = models.IntegerField(db_column='topRestaurant3') # Field name made lowercase.
    dob = models.DateField(null=True, blank=True)
    tipsrating = models.IntegerField(null=True, db_column='tipsRating', blank=True) # Field name made lowercase.
    visitsweekday = models.IntegerField(null=True, db_column='visitsWeekDay', blank=True) # Field name made lowercase.
    visitsweekend = models.IntegerField(null=True, db_column='visitsWeekend', blank=True) # Field name made lowercase.
    reviewrating = models.IntegerField(null=True, db_column='reviewRating', blank=True) # Field name made lowercase.
    spendrating = models.IntegerField(null=True, db_column='spendRating', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'userID'

class Userlogin(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    email = models.TextField(blank=True)
    password = models.TextField(blank=True)
    class Meta:
        db_table = 'userLogin'

class Uservisitdb(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    startdatetime = models.DateTimeField(null=True, db_column='startDateTime', blank=True) # Field name made lowercase.
    enddatetime = models.DateTimeField(null=True, db_column='endDateTime', blank=True) # Field name made lowercase.
    duration = models.TextField(blank=True) # This field type is a guess.
    behaviorrating = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='behaviorRating', blank=True) # Field name made lowercase.
    spend = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    weightedspend = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='weightedSpend', blank=True) # Field name made lowercase.
    tip = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    weightedtip = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='weightedTip', blank=True) # Field name made lowercase.
    leftreview = models.BooleanField(null=True, db_column='leftReview', blank=True) # Field name made lowercase.
    businessid = models.IntegerField(null=True, db_column='businessID', blank=True) # Field name made lowercase.
    dealid = models.IntegerField(null=True, db_column='dealID', blank=True) # Field name made lowercase.
    businessrating = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='businessRating', blank=True) # Field name made lowercase.
    waitressrating = models.DecimalField(decimal_places=65535, null=True, max_digits=65535, db_column='waitressRating', blank=True) # Field name made lowercase.
    waitress = models.IntegerField(null=True, blank=True)
    userid = models.BigIntegerField(null=True, db_column='userID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'userVisitDB'

class Waitressid(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    businessid = models.IntegerField(null=True, db_column='businessID', blank=True) # Field name made lowercase.
    ratings = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    class Meta:
        db_table = 'waitressID'


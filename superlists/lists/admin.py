from django.contrib import admin
from lists.models import jobs
from lists.models import wip
from lists.models import donejob

admin.site.register(jobs)
admin.site.register(wip)
admin.site.register(donejob)
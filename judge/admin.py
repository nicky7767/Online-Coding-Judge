from django.contrib import admin

# Register your models here.

from .models import Problem,Solution,TestCase

admin.site.register(Problem)
admin.site.register(Solution)
admin.site.register(TestCase)
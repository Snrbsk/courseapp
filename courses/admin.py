from django.contrib import admin
from courses.models import Course,Categories

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug")
    list_display_links = ("title","slug")
    readonly_fields = ("slug",)
    list_filter = ("isActive",)
    list_editable = ("isActive",)
    search_fields = ("title","description")

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass


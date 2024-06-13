from django.contrib import admin
from .models import Category, Course
# Register your models here.

admin.site.site_header = "Courses admin"
admin.site.site_title = "My courses"
admin.site.index_title = "Welcome to the Courses admin area"


class CourseInline(admin.TabularInline):
    model = Course
    exclude = ["created_ad"]
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_ad")
    fieldsets = [(None, {"fields": ["title"]}),
                 ("Dates", {
                     "fields": ["created_ad"],
                     "classes": ["collapse"]
                 })]
    inlines = [CourseInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)

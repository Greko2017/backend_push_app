from django.contrib import admin

# Register your models here.
from .models import * 

@admin.action(description='Notify employees')
def send_notification(modeladmin, request, queryset):
    employees = queryset.employess
    for employee in employees:
        employee.update(push_status=2)


# class EmployeeInline(admin.StackedInline):
#     model = Employee
#     # filter_horizontal = ('employees',)

class ReviewAdmin(admin.ModelAdmin):
    # inlines = [EmployeeInline]
    list_display = ('title', 'slug', 'created_on')
    list_filter = ("slug",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = [send_notification]

admin.site.register(Review, ReviewAdmin)


# class ReviewInline(admin.StackedInline):
#     model = Review
#     filter_horizontal = ('policy',)

class EmployeeAdmin(admin.ModelAdmin):
    # list_display = ('__all__')
    list_filter = ("is_staff",)
    search_fields = ['username', 'first_name']
    # inlines = [ReviewInline]

admin.site.register(Employee, EmployeeAdmin)
# https://stackoverflow.com/questions/8043881/django-admin-manytomanyfield
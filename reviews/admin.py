from django.contrib import admin
import requests
from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)

from requests.exceptions import ConnectionError, HTTPError

# Register your models here.
from .models import * 
# https://docs.expo.dev/push-notifications/sending-notifications/
@admin.action(description='Notify employees')
def send_notification(modeladmin, request, queryset):
    # employees = queryset.employees
    print('-- queryset', queryset)
    for qs in queryset:
        review = list(Review.objects.filter(id=qs.id).values())[0]
        employees = qs.employees.all()
        for employee in employees:
            print('-- employee', employee.push_token)
            if employee.push_token is not None:
                send_push_message(employee.push_token, "OverXLS", f"Please, read and confirm the Policy {review['title']}")
        # print('-- user', request.user)

    #     for employee in :
    #         if (employee.push_token is not None):
    #             print('-- token', employee.push_token )
    #             send_push_message(employee.push_token, 'message from admin interface')
    #         status = Status.objects.get(employee = employee.id)
    #         status.update(name=2)


# class EmployeeInline(admin.StackedInline):
#     model = Employee
    # filter_horizontal = ('employees',)

class ReviewAdmin(admin.ModelAdmin):
    # inlines = [EmployeeInline]
    list_display = ('title', 'slug', 'created_on', )
    list_filter = ("slug",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = [send_notification]
    # https://www.py4u.net/discuss/18397
    # def get_employees(self, obj):
    #     return "\n".join([p.employees for p in obj.employees.all()])  

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

class StatusAdmin(admin.ModelAdmin):
    list_display = ('employee', 'name','reviews')
    list_filter = ('name', 'employee',)
    search_fields = ['name', 'employee']

admin.site.register(Status, StatusAdmin)

# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
# PushMessage(to=None, data=None, title=None, body='DRUG AND ALCOHOL POLICY', sound=None, ttl=None, expiration=None, priority=None, badge=None, category=None, display_in_foreground=None, channel_id=None, subtitle=None, mutable_content=None)
def send_push_message(token, title, message, extra=None):
    try:
        response = PushClient().publish(
            PushMessage(to=token,
                        title=title,
                        sound='default',
                        body=message,
                        data=extra))
    except PushServerError as exc:
        # Encountered some likely formatting/validation error.
        rollbar.report_exc_info(
            extra_data={
                'token': token,
                'message': message,
                'extra': extra,
                'errors': exc.errors,
                'response_data': exc.response_data,
            })
        raise
    except (ConnectionError, HTTPError) as exc:
        # Encountered some Connection or HTTP error - retry a few times in
        # case it is transient.
        rollbar.report_exc_info(
            extra_data={'token': token, 'message': message, 'extra': extra})
        raise self.retry(exc=exc)

    try:
        # We got a response back, but we don't know whether it's an error yet.
        # This call raises errors so we can handle them with normal exception
        # flows.
        response.validate_response()
    except DeviceNotRegisteredError:
        # Mark the push token as inactive
        from notifications.models import PushToken
        PushToken.objects.filter(token=token).update(active=False)
    except PushTicketError as exc:
        # Encountered some other per-notification error.
        rollbar.report_exc_info(
            extra_data={
                'token': token,
                'message': message,
                'extra': extra,
                'push_response': exc.push_response._asdict(),
            })
        raise self.retry(exc=exc)
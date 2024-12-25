from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bugtracker.models import BugHunter, Ticket

# Register your models here.
# class BugHunterAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         (
#             None,
#             {
#                 "fields": (
#                     "first_name",
#                     "last_name",
#                     "email",
#                 )
#             },
#         ),
#     )


admin.site.register(BugHunter, UserAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ["status", "title", "filed_by", "assigned_to", "completed_by"]


admin.site.register(Ticket, TicketAdmin)
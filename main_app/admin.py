from django.contrib import admin

from main_app.models import User, Property, Review, Message, Appointment, Payment

# Register your models here.
admin.site.site_header = "Dwell Hub System"
admin.site.index_title = "Dwell Hub"


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'user_type')


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'landlord', 'price', 'availability')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'property', 'rating', 'timestamp')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'timestamp')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'property', 'appointment_date', 'appointment_time', 'status')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'property', 'amount', 'payment_date', 'payment_method', 'status')


admin.site.register(User, UserAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Payment, PaymentAdmin)

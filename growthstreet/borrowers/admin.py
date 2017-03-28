from django.contrib import admin

from .models import Borrower, Business, Loan

admin.site.register(Borrower)
admin.site.register(Business)
admin.site.register(Loan)

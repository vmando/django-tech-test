from django.db import models
from django.core.validators import RegexValidator
from .choices import SECTOR_CHOICES


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="""Phone number
    must be entered in the format: '+999999999'. Up to 15 digits allowed.""")
company_regex = RegexValidator(regex=r'^\d{8}$', message="""The registered
    company number is a 8 digits number.""")


class Borrower(models.Model):
    """It's used to store the information about the borrowers """
    name = models.CharField(max_length=200, help_text="Please enter your name")
    email = models.CharField(max_length=200,
                             help_text="Please enter your email")
    phone_number = models.CharField(max_length=100, help_text="""Please enter
                                        your telephone number""",
                                    validators=[phone_regex])

    def __str__(self):
        return self.name


class Business(models.Model):
    """It's used to store the information about the borrowers' business """
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200, help_text="""Please enter
                                            your company name""")
    address = models.CharField(max_length=400,
                               help_text="Please enter your company address")
    company_number = models.CharField(max_length=50,
                                      validators=[company_regex],
                                      help_text="""Please enter your registered
                                      company number (8 digits)""")
    business_sector = models.CharField(max_length=100,
                                       choices=SECTOR_CHOICES,
                                       help_text="""Please select your
                                                    business sector""")

    def __str__(self):
        return self.business_name


class Loan(models.Model):
    """It's used to store the information about the loan """
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    amount = models.IntegerField(help_text="""Please enter the amount
                                            you wish to borrow in GBP""")
    days = models.IntegerField(help_text="""Please enter the duration
                                            of the loan (in days)""")
    reason = models.TextField(help_text="Please enter the reason of the loan")

    def __str__(self):
        return str(self.amount)

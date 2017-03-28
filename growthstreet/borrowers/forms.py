from django import forms
from django.core.validators import RegexValidator
from .models import Borrower, Business, Loan


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="""Phone number must be entered in the
                                        format: '+999999999'. Up to 15 digits
                                        allowed.""")
company_regex = RegexValidator(regex=r'^\d{8}$',
                               message="""The registered company number is a
                                          8 digits number.""")


class BorrowerForm(forms.ModelForm):
    """ Form validating the basic information about the borrower """
    class Meta:
        model = Borrower
        fields = '__all__'

    def save(self, commit=True):
        borrower = super(BorrowerForm, self).save(commit=False)

        if commit:
            borrower.save()

        return borrower


class BusinessForm(forms.ModelForm):
    """
    Form validating the additional information about the business
    of the borrower
    """
    class Meta:
        model = Business
        fields = '__all__'

    def save(self, commit=True):
        business = super(BusinessForm, self).save(commit=False)

        if commit:
            business.save()

        return business


class LoanForm(forms.ModelForm):
    """ Form validating the loan request """
    class Meta:
        model = Loan
        fields = '__all__'

    def save(self, commit=True):
        loan = super(LoanForm, self).save(commit=False)

        if commit:
            loan.save()

        return loan

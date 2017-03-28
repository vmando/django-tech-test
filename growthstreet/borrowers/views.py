from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls.base import reverse_lazy

from .forms import BorrowerForm, BusinessForm, LoanForm


class BorrowerSignUpView(FormView):
    """ View for registering by entering name, email and phon number """
    form_class = BorrowerForm
    template_name = 'borrowers/borrower_signup.html'
    success_url = reverse_lazy('borrowers:registered')

    def post(self, request, *args, **kwargs):
        """ Overriding post method for saving the data to the database"""
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return super(BorrowerSignUpView, self).form_valid(form)

        return render(request, self.template_name, {'form': form})


class BusinessView(FormView):
    """ View for entering the information about the business """
    form_class = BusinessForm
    template_name = 'borrowers/business_details.html'
    success_url = reverse_lazy('borrowers:loan')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return super(BusinessView, self).form_valid(form)

        return render(request, self.template_name, {'form': form})


# class BorrowerLoanView(LoginRequiredMixin, FormView):
class BorrowerLoanView(FormView):
    """ View for requesting a loan """
    form_class = LoanForm
    template_name = 'borrowers/requestloan.html'
    success_url = reverse_lazy('borrowers:thanks')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return super(BorrowerLoanView, self).form_valid(form)

        return render(request, self.template_name, {'form': form})


# class RegisteredView(LoginRequiredMixin, TemplateView):
class RegisteredView(TemplateView):
    """
    View after a successful registration. It allows to choose between adding
    further information about the business and directly requesting a loan
    """
    form_class = LoanForm
    template_name = 'borrowers/success.html'


# class ThanksView(LoginRequiredMixin, TemplateView):
class ThanksView(TemplateView):
    """
    View after submitting a loan request.
    It contains a link to a new loan request
    """
    template_name = 'borrowers/thanks.html'

from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from .views import BorrowerSignUpView, BusinessView, BorrowerLoanView
from .forms import BorrowerForm


class TestBorrowerSignUpView(TestCase):

    def test_get_success_url(self):
        """"
        should redirect to the page with the choice between adding further
        information on the business and requesting a loan
        """
        self.assertEqual(
            BorrowerSignUpView().get_success_url(),
            reverse_lazy('borrowers:registered')
            )


class TestBusinessView(TestCase):

    def test_get_success_url(self):
        """" should redirect to the page to request a loan """
        self.assertEqual(
            BusinessView().get_success_url(),
            reverse_lazy('borrowers:loan')
            )


class TestBorrowerLoanView(TestCase):

    def test_get_success_url(self):
        """" should redirect to the page to requesting a new loan """
        self.assertEqual(
            BorrowerLoanView().get_success_url(),
            reverse_lazy('borrowers:thanks')
            )

class TestBorrowerForm(TestCase):
    """ Test Case for the Borrower Creation Form """
    def setUp(self):
        self.valid_data = {
            'phone_number': '+447123456789',
            'name': 'john',
            'email': 'john@email.com',
        }

    def test_all_valid(self):
        """ self.valid_data should yield a valid form """
        form = BorrowerForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_phone_number(self):
        """ check that phone numbers are correctly validated """
        data=self.valid_data
        data["phone_number"]="+123456"
        form = BorrowerForm(data=data)
        self.assertFalse(form.is_valid())

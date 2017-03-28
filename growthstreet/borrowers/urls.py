from django.conf.urls import url
from . import views


app_name = 'borrowers'

urlpatterns = [
    url(r'^register/',
        view=views.BorrowerSignUpView.as_view(),
        name="register"),
    url(r'^registered/',
        view=views.RegisteredView.as_view(),
        name="registered"),
    url(r'^business/', view=views.BusinessView.as_view(), name="business"),
    url(r'^loan/', view=views.BorrowerLoanView.as_view(), name="loan"),
    url(r'^thanks/', view=views.ThanksView.as_view(), name="thanks"),
]

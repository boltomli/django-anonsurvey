from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.SurveysView.as_view(), name='surveys'),
    url(r'^survey_thanks/$',
        
TemplateView.as_view(template_name='anonsurvey3/survey_thanks.html'),
        name='survey_thanks'),
    url(r'^(?P<slug>[\w-]+)/form/$', views.SurveyView.as_view(),
        name='survey'),
    url(r'^(?P<pk>\d+)/complete/$', views.complete_survey,
        name="survey_complete"),
]

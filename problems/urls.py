__author__ = 'matt'

from django.conf.urls import patterns, url

urlpatterns = patterns('problems.views',
    url(r'^list', 'list.view', name='listProblems')
)

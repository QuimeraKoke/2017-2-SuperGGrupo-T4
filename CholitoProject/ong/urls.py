from django.conf.urls import url

from ong.views import ONGNaturalView, ONGIndexView, ONGAdoptedView, \
    ONGStatisticsView, ONGEditView, ONGAddAnimalView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ONGNaturalView.as_view(), name='see-natural-ong'),
    url(r'^$', ONGIndexView.as_view(), name='ong-index'),
    url(r'^adopted/$', ONGAdoptedView.as_view(), name='ong-adopted'),
    url(r'^statistics/$', ONGStatisticsView.as_view(), name='ong-statistics'),
    url(r'^edit/$', ONGEditView.as_view(), name='ong-edit'),
    url(r'^add/$', ONGAddAnimalView.as_view(), name='add-animal'),
]

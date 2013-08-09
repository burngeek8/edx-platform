from django.conf.urls import url, patterns

urlpatterns = patterns('pipeline_js.views',  # nopep8
    url(r'^$', 'xmodule_js_files', name='xmodule_js_files'),
)

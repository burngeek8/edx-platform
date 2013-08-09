import json
from django.conf import settings
from django.http import HttpResponse
from staticfiles.storage import staticfiles_storage


def xmodule_js_files(request):
    # if settings.MITX_FEATURES['USE_DJANGO_PIPELINE']:
    if False:
        paths = [settings.PIPELINE_JS['module-js']['output_filename']]
    else:
        paths = [path.replace(".coffee", ".js") for path in
                 settings.PIPELINE_JS['module-js']['source_filenames']]
    urls = [staticfiles_storage.url(path) for path in paths]
    return HttpResponse(json.dumps(urls), content_type="application/json")

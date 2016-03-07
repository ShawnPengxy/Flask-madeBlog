import os, sys
app_root=os.path.dirname(__file__)
sys.path.insert(0,os.path.join(app_root,'site-packages'))

import sae
from manage import app
from sae.ext.shell import ShellMiddleware

application=sae.create_wsgi_app(ShellMiddleware(app))

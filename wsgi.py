import os
from BasicDemo import create_app

_basepath = os.path.dirname(os.path.abspath(__file__))
app = create_app()
app.run()

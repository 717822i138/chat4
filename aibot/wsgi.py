import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aibot.settings')

application = get_wsgi_application()

# வெர்சல் சர்வருக்காக இந்த வரியை கண்டிப்பா கடைசியில் சேர்க்கணும் தம்பி!
app = application
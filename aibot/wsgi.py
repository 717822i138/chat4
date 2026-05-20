import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aibot.settings')

application = get_wsgi_application()
app = application  # இந்த வரி தான் வெர்சலுக்கு ரொம்ப முக்கியம் தம்பி!

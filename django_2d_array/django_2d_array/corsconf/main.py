
CORS_URLS_REGEX          = r'^/.*$' # CORS HEADERS ENBALED importante gamizu
CORS_ORIGIN_WHITELIST    = (
    'http://localhost:4200',
    'http://localhost:4201',
)

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + (
    'X-CSRFToken',
)
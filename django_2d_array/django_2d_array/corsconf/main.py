
CORS_URLS_REGEX          = r'^/.*$' # CORS HEADERS ENBALED importante gamizu
CORS_ORIGIN_WHITELIST    = (
    'http://69.16.201.27:4200',
    'http://69.16.201.27:4201',
)

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + (
    'X-CSRFToken',
)
# URLs Directories

BRAND_IMAGES_URL = '/var/www/images/'


# User Sign in / sign up constants
MAX_NAME_LENGTH = 200
MIN_NAME_LENGTH = 3
MAX_EMAIL_LENGTH = 100
MAX_PASSWORD_LENGTH = 200
UID_LENGTH = 64
MAX_PASSWORD_LENGTH = 200
MIN_PASSWORD_LENGTH = 3
SALT_LENGTH = 16
SOCIAL_ID_LENGTH = 30
TOKEN_LENGTH = 40
MAX_URL_LENGTH = 1000
MAX_DES_LENGTH = 10000

KEY_CUSTOMER_REF = 'customer_ref'
KEY_USER_ID = 'user_id'
KEY_EMAIL_ID = 'email'
KEY_FACEBOOK_ID = 'facebook_id'
KEY_GOOGLE_ID = 'google_id'
KEY_GOOGLE_AUTH = 'google_auth'
KEY_FB_AUTH = 'facebook_auth'
KEY_USER_NAME = 'name'
KEY_PHONE_NO = 'phoneno'
KEY_PASSWORD_HASH = 'password_hash'
KEY_SALT = 'salt'
KEY_FIELDS_GET = 'fields'
KEY_TOKEN = 'HTTP_TOKEN'
KEY_ADMIN = 'HTTP_ADMIN'

HTTP_METHOD_POST        = 'POST'
HTTP_METHOD_GET         = 'GET'
HTTP_METHOD_OPTION      = 'OPTION'
HTTP_METHOD_PUT         = 'PUT'
HTTP_METHOD_HEAD        = 'HEAD'
HTTP_METHOD_DELETE      = 'DELETE'

HASH_METHOD_USER_ADD = 'SHA512'
URL_SEPRATOR = '&'

KEY_BRAND_ID            = 'brand_id'
KEY_BRAND_NAME          = 'brand_name'
KEY_BRAND_IMAGE         = 'brand_image'
KEY_BRAND_URL           = 'brand_url'
KEY_BRAND_DES           = 'brand_des'
KEY_ADEEDON             = 'addedon'




SIGNUP_FIELDS = [
    KEY_EMAIL_ID,
    KEY_USER_NAME,
    KEY_PASSWORD_HASH
    ]

SIGNIN_FIELDS = [
    KEY_EMAIL_ID,
    KEY_PASSWORD_HASH
    ]






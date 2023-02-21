import os
import json
from google.oauth2 import service_account

scope = [
  'https://spreadsheets.google.com/feeds',
  'https://www.googleapis.com/auth/drive'
]


def load_user_secrets_from_local():
  creds_json = json.loads(os.environ['GOOGLE_API_JSON'])
  credentials = service_account.Credentials.from_service_account_info(
    creds_json, scopes=scope)
  return credentials

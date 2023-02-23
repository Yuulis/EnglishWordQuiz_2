import os
import gspread
from google_api import get_secrets

credentials = get_secrets.load_user_secrets_from_local()
gc = gspread.authorize(credentials)

# log用スプレッドシートの取得
book_log = gc.open_by_key(os.getenv('SHEET_KEY_LOG'))
sheet_log = book_log.sheet1


# logに記録する
def add_log(contents, line):
  sheet_log.insert_row(contents, line)
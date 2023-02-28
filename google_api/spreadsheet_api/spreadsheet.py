import os
import gspread
from google_api import get_secrets

credentials = get_secrets.load_user_secrets_from_local()
gc = gspread.authorize(credentials)

# log用スプレッドシートの取得
book_log = gc.open_by_key(os.getenv('SHEET_KEY_LOG'))
sheet_log = book_log.sheet1

# userList用のスプレッドシートの取得
book_userList = gc.open_by_key(os.getenv('SHEET_KEY_USERLIST'))
sheet_userList = book_userList.sheet1


# logに記録する
def add_log(contents):
  sheet_log.insert_row(contents, 2)


# userListの取得
def get_userList():
  return sheet_userList.col_values(1)


# userListに追加
def add_userList(id):
  return sheet_userList.insert_row([str(id)], 2)

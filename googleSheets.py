import gspread

spread_sheet_name = "Oura IFTTT Spreadsheet"
work_sheet_name = 'Sheet1'

sa = gspread.service_account()
sh = sa.open(spread_sheet_name)

wks = sh.worksheet(work_sheet_name)

def insert_Oura_Scores(date, readiness_score, sleep_score):
    print(date, readiness_score, sleep_score)
    newRow = [date, readiness_score, sleep_score]
    wks.append_row(newRow, table_range="A1:C1")

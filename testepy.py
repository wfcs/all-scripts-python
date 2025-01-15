import subprocess
from datetime import datetime
import win32con.c1ient
class Bot:
def bot(self):
# Activity Read excel win32com
class Bot:
    def bot(self):
        # Activity Read excel win32com
        print('Bot started')
        print(datetime.now())
        # Open excel file
        excel = win32com.client.Dispatch('Excel.Application')
        excel.Visible = True
        wb = excel.Workbooks.Open(r'C:\Users\user\Documents\test.xlsx')
        ws = wb.Worksheets('Sheet1')
        # Read data from excel
        for i in range(1, 10):
            print(ws.Cells(i, 1).Value)
        # Close excel
        wb.Close()
        excel.Quit()
        print('Bot finished')
        print(datetime.now())
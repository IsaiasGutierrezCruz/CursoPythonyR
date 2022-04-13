import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

ITEM_SHEET = 'items'
CLIENT_SHEET = 'clients'
SPREAD_SHEET = '<identificador_de_la_hoja_de_calculo'
CREDS_JSON = '<tu_direccion>/access_key.json'

class gsheet_helper: 
    def __init__(self):
        scope = ["https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_JSON,scope)

        # autoriza una conexion hacia la google sheet 
        self.client = gspread.authorize(creds)
        self.gsheet = self.client.open_by_key(SPREAD_SHEET)

    def get_items(self):
        items = self.get_sheet(ITEM_SHEET)
        return items


    def get_sheet(self, sheet_name):
        sheet = self.gsheet.worksheet(sheet_name)
        items = pd.DataFrame(sheet.get_all_records())
        return items 

    def store_user(self, user_dic):
        sheet = self.gsheet.worksheet(CLIENT_SHEET)
        clients = pd.DataFrame(self.get_sheet(CLIENT_SHEET))

        if len(clients.index != 0):
            cond = clients[clients["id"] == user_dic["id"]].empty

            # si no existe guardarlo en el registro
            if cond:
                sheet.add_rows(1)
                sheet.append_row([element for element in user_dic.values()])
            else:
                print("Este usuario ya esta registrado en nuestra hoja de calculo")
        else:
            sheet.add_rows(1)
            sheet.append_row([element for element in user_dic.values()])



if __name__ == "__main__":
    print(gsheet_helper().get_items())


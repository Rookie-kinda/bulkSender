# links[i] = f"https://wa.me/+20{numbers[i]}"

import pywhatkit as pwk # to send whatsapp msgs
from datetime import datetime # to determine current time
from time import sleep # to pause between moves since internet is...shitty at best
import pyautogui as pag # to control keyboard
import pandas as pd # ...pandas
import keyboard as kb


class dataHandler:
    def __init__(self, path_to_data, type_of_file):
        self.path = path_to_data
        
        if type_of_file == "excel":
            self.data = pd.read_excel(self.path)
        elif type_of_file == "csv":
            self.data = pd.read_csv(self.path)
        else:
            raise ValueError(f"'type_of_file' should be either 'excel' or 'csv', not {type(type_of_file)}")
        self.data.dropna(inplace=True)
        self.data.set_index("Parent's WA", inplace=True)

    def check_siblings(self) -> None:
        counts = self.data.value_counts(subset="Parent's WA")
        counts = counts[counts > 1]
        
        for i in counts.index:
            x = self.data.loc[i].drop_duplicates()["Name"]
            self.data["Name"].loc[i] = " و".join(x)
        
        self.data.drop_duplicates(inplace=True)
        return self.data
        # self.data.to_excel("E:\مسجد العادل(دورة القران الكريم)\dummy.xlsx")

class whatsend:
    def __init__(self, wait_time) -> None:
        self.wait_time = wait_time
    def sendmsg(self, phone: str, msg: str) -> None:
        if phone[0] == "0":
            pwk.sendwhatmsg_instantly(f'+2{phone}', msg, wait_time=self.wait_time, tab_close=True)
        else:
            pwk.sendwhatmsg_instantly(f'+20{phone}', msg, wait_time=self.wait_time, tab_close=True)
    # sleep(15)
    # kb.press_and_release("enter")
    # sleep(3)
    # with pag.hold("ctrl"):
    #     pag.press("w")

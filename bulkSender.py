# links[i] = f"https://wa.me/+20{numbers[i]}"

import pywhatkit as pwk # to send whatsapp msgs
from time import sleep # to pause between moves since internet is...shitty at best
import pyautogui as pag # to control keyboard
import pandas as pd # ...pandas
import keyboard as kb

# To handle incoming data that contains whatsapp numbers and owner's name
def read_data(path, type_of_file):
    if type_of_file == "excel":
        data = pd.read_excel(path)
    elif type_of_file == "csv":
        data = pd.read_csv(path)
    else:
        raise ValueError(f"'type_of_file' should be either 'excel' or 'csv', not {type(type_of_file)}")
    self.data.dropna(inplace=True, subset="phone_num) #To drop rows with no phone number


def sendmsg(phone: str, msg: str) -> None:
    """
    Adjust wait_time properly, if the internet connection is slow then increase it (although 30 seconds should be good anyways)
    And if the connection is good then decrease it (10-15 seconds should be good, unless you have some exceptionally good connection, lol, but either way 10 to 15 seccs should be good)
    Anways, adjust how you see fit!

    Also, change tab_close if you want to

    One last thing is, adjust the country code where to the proper country code, this code is Egypt's code and the condition is to check if the number starts with a 0 or not, because Egypt's is +20
    but we always start our phones with "01" anways, so it's just to avoid an error, that's all, you can change it with a try except block though...idk why but that's an option
    """
        if phone[0] == "0":
            pwk.sendwhatmsg_instantly(f'+2{phone}', msg, wait_time=30, tab_close=True)
        else:
            pwk.sendwhatmsg_instantly(f'+20{phone}', msg, wait_time=30, tab_close=True)
    kb.press_and_release("enter") # because sometimes the function doesn't actually send the message, just types it in the box
    # The next block is in case your internet is slow and you want to close the tab, should not be necessary if you adjust wait_time properly though, so you can delete it
    # sleep(5)
    # with pag.hold("ctrl"):
    #     pag.press("w")

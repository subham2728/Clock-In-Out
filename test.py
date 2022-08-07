import pyautogui
from datetime import datetime
import time
from dhooks import Webhook
import datetime

print("***************Script Started*******************")

while True:
    hook = Webhook("https://discord.com/api/webhooks/1005687335779848262/dt-VZux2Hva7c9oEOvF_ElFc7SIKMCEihg5xFemDwg3rzxCe-CTDfX8Ao9InlCEXufso")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    day_name = str(datetime.datetime.now().strftime('%A'))
    date_today = datetime.datetime.now().date()
    try:
        if current_time == "10:30" and day_name == "Monday" or day_name=="Tuesday" or day_name=="Wednesday" or day_name=="Thursday" or day_name=="Friday":
            print("It is time to clock in")
            if pyautogui.locateOnScreen("C:\\Users\\Administrator\\Desktop\\in.png",confidence=0.8) != None:
                pyautogui.leftClick(1715,152)
                content=("**Good Morning Subham!** \nToday's date is **{}** \nI have clocked in successfully at **{}**\n**Have a nice day :)**".format(date_today,current_time))
                hook.send(content)
                print("Clocked in at",day_name,date_today,current_time)
                time.sleep(60)
        elif current_time == "20:02" and day_name == "Monday" or day_name=="Tuesday" or day_name=="Wednesday" or day_name=="Thursday" or day_name=="Friday":
            if pyautogui.locateOnScreen("C:\\Users\\Administrator\\Desktop\\in.png",confidence=0.8) != None:
                print("It is time to clock out")
                pyautogui.leftClick(1715,152)
                content=("**Hey Subham!**\nI have clocked out successfully at **{}**\n**Good Night :)**".format(current_time))
                hook.send(content)
                print("Clocked out at",day_name,date_today,current_time)
                time.sleep(60)
        else:
            pass
    except:
        if current_time!= "10:30" and current_time!= "20:02":
            content=("**Hey Subham!** \nI ran into an error at **{} {}**".format(date_today,current_time))
            hook.send(content)
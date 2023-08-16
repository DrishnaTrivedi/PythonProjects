from plyer import notification
import time
import pandas as pd
from playsound import playsound
print("Add the task name to the excel file along with time to get notified about it".center(150))
df = pd.read_excel('Book1.xlsx')
while True:

    for i in range (len(df)):
        t1 = int(time.strftime("%H"))
        t2 = int(time.strftime("%M"))
        # print("current time= ",t1 ,t2)
        if(t1==int(str(df.iloc[i,2]).split(":")[0]) and t2==int(str(df.iloc[i,2]).split(":")[1] ) ):#0,1 ...1,1
            print("Found a remainder!")

            notification.notify(title = df.iloc[i,0],
                                message = df.iloc[i,1],
                                timeout = 3,
                                app_icon = "C:/Users/drish/PycharmProjects/pythonProject/icons8-app-50.ico"
                                                        )
            playsound("C:/Users/drish/PycharmProjects/pythonProject/notiSound.mp3")

    time.sleep(60)
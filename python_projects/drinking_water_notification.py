import time
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(
            title = "Drink Water Now!",
            message = "You can drink 3.17 liter water daily.",
            app_icon=r"C:\Users\Jigu\Documents\meet\project_clg\python_projects\icon.ico",
            timeout = 10
        )
        time.sleep(60*60)
import requests
import tkinter as tk
from tkinter import font
from PIL import ImageTk

def test_function(entry):
    print("button clicked : ",entry)

def get_weather(city):
    weather_key = 'b5111187392755947720b8870cd9f49b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key,'q':city,'units':'metric','lang':'kr'}
    res= requests.get(url,params=params)
    weather = res.json()
    label['text'] = format_response(weather)
    print(weather)

def format_response(weather):
    try:
        name = weather['name']
        print("name=",name)
        dec = weather['weather'][0]['description']
        print("dec=",dec)
        temp = weather['main']['temp']
        print("temp=",temp)
        temp_min = weather['main']['temp_min']
        print("temp_min=",temp_min)
        temp_max = weather['main']['temp_max']
        print("temp_max=",temp_max)
        humi = weather['main']['humidity']
        print("humi=",humi)
        wind_speed = weather['wind']['speed']
        print("wind_speed=",wind_speed)

        final_str ="도시 : %s\n날씨 : %s\n온도 : %s\n최저온도 : %s\n최고온도 : %s\n습도 : %s\n풍속 : %s"%(name,dec,temp,temp_min,temp_max,humi,wind_speed)
    except:
        final_str = "오류 있음. 확인필요"
    return final_str

root=tk.Tk()
canvas = tk.Canvas(root,height=500,width=700)
canvas.pack()

background_image=ImageTk.PhotoImage(file="IMG_4389.JPEG")
background_label=tk.Label(root,image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

frame = tk.Frame(root, background='blue', bd=5)
frame.place(relx=0.5, rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

button = tk.Button(frame, text='Search', font=40, command=lambda:get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)

entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

lower_frame =tk.Frame(root,bg='blue',bd=10)
lower_frame.place(relx=0.5, rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(lower_frame,font=("휴먼매직체",18))
label.place(relwidth=1,relheight=1)

root.mainloop()

"""

def message(event) :
    lbl['text'] = entry.get()

entry = Entry(win)
entry.bind("<Return>", message)
entry.pack()

lbl = Label(win.text="")
lbls.pack()
win.mainloop()

city = input('도시 입력 : ')
weather_url = f'https://api.openweathermap.org/data/2.5/weather?q=' \
+ city + '&APPID=b5111187392755947720b8870cd9f49b&units=metric&lang=kr'

res = requests.get(weather_url)
data = res.json()
print(data)

temp = data['main']['temp']
weather = data['weather'][0]['main']
print(temp, " ", weather)
"""
"""
도시 입력 : Seoul
{'coord': {'lon': 126.9778, 'lat': 37.5683}, 
'weather': [{'id': 500, 'main': 'Rain', 'description': '실 비', 'icon': '10d'}], 
'base': 'stations', 
'main': {'temp': 13.96, 'feels_like': 13.71, 'temp_min': 13.69, 'temp_max': 14.66, 'pressure': 1009, 'humidity': 88}, 
'visibilih0, 
'wind': {'speed': 5.14, 'deg': 70}, 
'clouds': {'all': 100}, 
'dt': 1713597322, 
'sys': {'type': 1, 'id': 8105, 'country': 'KR', 'sunrise': 1713559818, 'sunset': 1713607878}, 
'timezone': 32400, 
'id': 1835848, 
'name': 'Seoul', 
'cod': 200}
"""
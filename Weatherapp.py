from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the Tk root window
x = (screen_width - 900) // 2
y = (screen_height - 500) // 2

# Set the geometry of the root window
root.geometry(f"900x500+{x}+{y}")

root.resizable(False, False)
root.attributes("-alpha", 1)		# transparency range 0-1

def getweather():
    try:
        city=textfield.get()
        if city == "":
            messagebox.showerror("Warning!", "Please enter a city name.")
            return
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

        name.config(text=result)
        long_lat.config(text=f"{round(location.latitude,4)}°N / {round(location.longitude,4)}°E")
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
                
        #WeatherApi
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a03a9654056957bfe21c192876194a6f"
        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = (json_data['main']['pressure'])
        humidity = (json_data['main']['humidity'])
        wind = (json_data['wind']['speed'])
        sunrise = datetime.fromtimestamp(json_data['sys']['sunrise']).strftime("%I:%M %p")
        sunset = datetime.fromtimestamp(json_data['sys']['sunset']).strftime("%I:%M %p")
                
        t.config(text=f"{temp}°C")
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°C"))
        
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description)
        p.config(text=f"{pressure} hPa")
        sr.config(text=sunrise)
        ss.config(text=sunset)
        
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")

def reset_data():
    t.config(text="...")
    c.config(text="...")
    w.config(text="...")
    h.config(text="...")
    d.config(text="...")
    p.config(text="...")
    sr.config(text="...")
    ss.config(text="...")

#Search Box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()	#sets the focus on the text field itself
textfield.bind("<Return>", lambda event: getweather()) #binds the Enter key event to a specific function
textfield.bind("<BackSpace>", lambda event: reset_data())

Search_icon=PhotoImage(file="searchicon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",activebackground='#404040',command=getweather)
myimage_icon.place(x=400,y=34)

#Logo
logo_image=PhotoImage(file="im.png")
logoimage=Label(image=logo_image)
logoimage.place(x=150,y=100) 

#sunrise/sunset icon
sr_image=PhotoImage(file="sunrise.png")
srimage=Label(image=sr_image)
srimage.place(x=90,y=355)

ss_image=PhotoImage(file="sunset.png")
ssimage=Label(image=ss_image)
ssimage.place(x=590,y=355)


#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#Timezone
name=Label(root,font=("arial",12,'bold'))
name.place(x=690,y=20)
long_lat=Label(root,font=("arial",12,'bold'))
long_lat.place(x=690,y=50)

clock=Label(root,font=("Helvetica",20,'bold'))
clock.place(x=30,y=100)

# Label
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=420, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

label5 = Label(root, text="SUNRISE", font=("Helvetica", 14, 'bold'),fg="#1ab5ef")
label5.place(x=125, y=356)

label6 = Label(root, text="SUNSET", font=("Helvetica", 14, 'bold'),fg="#1ab5ef")
label6.place(x=630, y=356)


t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"), fg="#ee666d")
c.place(x=400, y=250)

w = Label(text="...", font=("arial",15, "bold"), bg="#1ab5ef")
w.place(x=125, y=430)
h = Label(text="...", font=("arial",15,"bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial",15, "bold"), bg="#1ab5ef")
d.place(x=420, y=430)
p = Label(text="...", font=("arial",15, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)
sr = Label(text="...", font=("arial", 14, "bold"))
sr.place(x=220, y=356)
ss = Label(text="...", font=("arial", 14, "bold"))
ss.place(x=715, y=356)

root.mainloop()



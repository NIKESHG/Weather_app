from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Create the root window
root = Tk()
root.title("WEATHER APP")
root.geometry("1365x697+0+0")
root.resizable(False, False)

# Set the background image
image_path = "blur.jpg"  # Replace with the actual path to your image
background_image = Image.open(image_path)
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
background_image = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position for the frame window
frame_width = 900
frame_height = 500
frame_x = (screen_width - frame_width) // 2
frame_y = (screen_height - frame_height) // 2

frame = Toplevel(root)
frame.title("Weather App")
frame.geometry(f"{frame_width}x{frame_height}+{frame_x}+{frame_y}")
frame.attributes("-alpha", 0.7)
#frame.focus()

# Set the frame window to be always on top
frame.wm_attributes("-topmost", 1)

def getweather(event=None):
    try:
        city=textfield.get()
        if city == "":
            messagebox.showerror("Warning !! ", "Please enter a city name. ", parent=frame)
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
        messagebox.showerror(" Warning !! "," Invalid Entry!! ", parent=frame)

def reset_data():
    t.config(text="...")
    c.config(text="...")
    w.config(text="...")
    h.config(text="...")
    d.config(text="...")
    p.config(text="...")
    sr.config(text="...")
    ss.config(text="...")


# Create the search box
search_image = PhotoImage(file="search.png")
myimage = Label(frame, image=search_image, bd=0, highlightthickness=0)
myimage.place(x=20, y=20)

textfield=tk.Entry(frame,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()	#sets the focus on the text field itself
textfield.bind("<Return>", getweather) #binds the Enter key event to a specific function
textfield.bind("<BackSpace>", lambda event: reset_data())

Search_icon=PhotoImage(file="searchicon.png")
myimage_icon=Button(frame,image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",activebackground='#404040',command=getweather)
myimage_icon.place(x=400,y=31)

#Logo
logo_image=PhotoImage(file="im.png")
logoimage=Label(frame,image=logo_image)
logoimage.place(x=150,y=100)

#sunrise/sunset icon
sr_image=PhotoImage(file="sunrise.png")
srimage=Label(frame,image=sr_image)
srimage.place(x=90,y=355)

ss_image=PhotoImage(file="sunset.png")
ssimage=Label(frame,image=ss_image)
ssimage.place(x=590,y=355)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(frame,image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#Timezone
name=Label(frame,font=("arial",12,'bold'))
name.place(x=690,y=20)
long_lat=Label(frame,font=("arial",12,'bold'))
long_lat.place(x=690,y=50)

clock=Label(frame,font=("Helvetica",20,'bold'))
clock.place(x=30,y=100)

# Label
label1 = Label(frame, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(frame, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(frame, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=420, y=400)

label4 = Label(frame, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

label5 = Label(frame, text="SUNRISE", font=("Helvetica", 14, 'bold'),fg="#1ab5ef")
label5.place(x=125, y=356)

label6 = Label(frame, text="SUNSET", font=("Helvetica", 14, 'bold'),fg="#1ab5ef")
label6.place(x=630, y=356)

t = Label(frame,font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(frame,font=("arial", 15, "bold"), fg="#ee666d")
c.place(x=400, y=250)

w = Label(frame,text="...", font=("arial",15, "bold"), bg="#1ab5ef")
w.place(x=125, y=430)
h = Label(frame,text="...", font=("arial",15,"bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(frame,text="...", font=("arial",15, "bold"), bg="#1ab5ef")
d.place(x=420, y=430)
p = Label(frame,text="...", font=("arial",15, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)
sr = Label(frame,text="...", font=("arial", 14, "bold"))
sr.place(x=220, y=356)
ss = Label(frame,text="...", font=("arial", 14, "bold"))
ss.place(x=715, y=356)


def on_frame_close():
    root.destroy()
# Register the on_frame_close() function to be called when the frame window is closed.
frame.protocol("WM_DELETE_WINDOW", on_frame_close)

root.mainloop()

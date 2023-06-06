from tkinter import *
import requests
import json
import customtkinter
from datetime import date,datetime,timedelta
import config

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
root = customtkinter.CTk()
root.title("Weather Application")
root.geometry("500x500")

def input_city():
    cty = inp1.get()
    global city
    city = cty
    current.pack_forget()
    current.pack()
    forcast.pack_forget()
    forcast.pack()
    '''today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    Label(root,text="today's date:"+str(d1)).pack()
    tomorrow = today + timedelta(days=1)
    d2 = tomorrow.strftime("%d/%m/%Y")
    Label(root, text="today's date:" + str(d2)).pack()'''




def current_weather():
    current_weather_window = customtkinter.CTkToplevel()
    current_weather_window.title("Current Weather Conditions")
    current_weather_window.geometry("400x400")
    global city
    city = inp1.get()
    api_link = 'http://api.weatherapi.com/v1/forecast.json?key='+config.API_KEY+'&q='+city+'&days=10&aqi=yes&alerts=yes'
    try:
        api_request = requests.get(api_link)
        x = json.loads(api_request.content)
        cty_name = customtkinter.CTkLabel(current_weather_window, text="City Name:" + str((x['location']['name'])))
        cty_name.pack()
        time = customtkinter.CTkLabel(current_weather_window, text="Time:" + str((x['location']['localtime'])))
        time.pack()
        temp_in_c = customtkinter.CTkLabel(current_weather_window, text="Temperature in celsius:" + str(x['current']['temp_c']))
        temp_in_c.pack()
        curr_condt = customtkinter.CTkLabel(current_weather_window, text="Current condition:" + str(x['current']['condition']['text']))
        curr_condt.pack()
        wind_speed = customtkinter.CTkLabel(current_weather_window, text="Wind speed in mph:" + str(x['current']["wind_mph"]))
        wind_speed.pack()
        humidity = customtkinter.CTkLabel(current_weather_window, text="humidity:" + str(x['current']["humidity"]))
        humidity.pack()
        uv = customtkinter.CTkLabel(current_weather_window, text="UV:" + str(x['current']['uv']))
        uv.pack()
        air_quality = customtkinter.CTkLabel(current_weather_window, text="Air Quality")
        air_quality.pack()
        co = customtkinter.CTkLabel(current_weather_window, text="CO:" + str(x['current']['air_quality']['co']))
        co.pack()
        no2 = customtkinter.CTkLabel(current_weather_window, text="NO2:" + str(x['current']['air_quality']['no2']))
        no2.pack()
        o3 = customtkinter.CTkLabel(current_weather_window, text="O3:" + str(x['current']['air_quality']['o3']))
        o3.pack()
        so2 = customtkinter.CTkLabel(current_weather_window, text="SO2:" + str(x['current']['air_quality']['so2']))
        so2.pack()
    except Exception as e:
        customtkinter.CTkLabel(root,text="error").pack()



def forecast():
    forecast_window = customtkinter.CTkToplevel()
    forecast_window.title("Forecast")
    forecast_window.geometry("400x400")
    clicked = StringVar()
    global opt
    global lb

    lst = [str(1),str(2),str(3)]
    clicked.set(str(1))
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    lb2 =customtkinter.CTkLabel(forecast_window, text="today's date:" + str(d1))
    lb2.pack()
    lb1 = customtkinter.CTkLabel(forecast_window, text="Select which day after today forecast to be shown:")
    lb1.pack()
    drop = customtkinter.CTkOptionMenu(forecast_window,values=lst,variable=clicked)
    drop.pack()



    btn = customtkinter.CTkButton(forecast_window,text="Submit",command=fore)

    btn.pack()

    global clk
    clk = clicked

    global fr_window
    fr_window = forecast_window
    global btn1
    btn1 = btn
    opt = drop
    lb = lb1






inp1 = customtkinter.CTkEntry(root)
inp1.pack()
current = customtkinter.CTkButton(root, text="Display current weather conditions", command=current_weather)
forcast = customtkinter.CTkButton(root,text="Display daily forecast",command=forecast)
submit1 = customtkinter.CTkButton(root,text="Submit",command=input_city)
submit1.pack()
def fore():
    global fr_window
    global clk
    global btn1
    global opt
    global lb
    btn1.pack_forget()
    opt.pack_forget()
    lb.pack_forget()
    btn2 = customtkinter.CTkButton(fr_window,text="see hourly forecast",command=hourly_forecast)
    btn2.pack()
    h = Scrollbar(fr_window,orient='horizontal')

    h.pack(side=BOTTOM,fill=X)
    v = Scrollbar(fr_window)

    v.pack(side=RIGHT,fill=Y)
    t = Text(fr_window,width=150,height=150,wrap=NONE,xscrollcommand=h.set,yscrollcommand=v.set)
    global butn2
    butn2 = btn2






    cty = inp1.get()

    api_link = 'http://api.weatherapi.com/v1/forecast.json?key='+config.API_KEY+'&q='+city+'&days=10&aqi=yes&alerts=yes'
    try:
        api_request = requests.get(api_link)
        x = json.loads(api_request.content)
        i = int(clk.get())-1
        if i<len(x['forecast']['forecastday']):
            dte = str(x['forecast']['forecastday'][i]['date'])
            t.insert(END, "date:" + dte + "\n")
            max_tmp = str(x['forecast']['forecastday'][i]['day']['maxtemp_c'])
            t.insert(END, "maximum temperature:" + max_tmp + "\n")
            min_tmp = str(x['forecast']['forecastday'][i]['day']['mintemp_c'])
            t.insert(END, "minimum temperature:" + min_tmp + "\n")

            avg_tmp = str(x['forecast']['forecastday'][i]['day']['avgtemp_c'])
            max_wind = str(x['forecast']['forecastday'][i]['day']['maxwind_mph'])
            precipitation = str(x['forecast']['forecastday'][i]['day']['totalprecip_mm'])
            sunset = str(x['forecast']['forecastday'][i]['astro']['sunset'])
            avg_humidity = str(x['forecast']['forecastday'][i]['day']['avghumidity'])
            moonrise = str(x['forecast']['forecastday'][i]['astro']['moonrise'])
            moonset = str(x['forecast']['forecastday'][i]['astro']['moonset'])
            moon_phase = str(x['forecast']['forecastday'][i]['astro']['moon_phase'])
            sunrise = str(x['forecast']['forecastday'][i]['astro']['sunrise'])

            t.insert(END, "average temperature:" + avg_tmp + "\n")
            t.insert(END, "maximum wind speed:" + max_wind + "\n")
            t.insert(END, "precipitation:" + precipitation + "\n")
            t.insert(END, "sunset:" + sunset + "\n")
            t.insert(END, "average humidity:" + avg_humidity + "\n")
            t.insert(END, "moonrise:" + moonrise + "\n")
            t.insert(END, "moonset:" + moonset + "\n")
            t.insert(END, "moon phase:" + moon_phase + "\n")
            t.insert(END, "sunrise:" + sunrise + "\n")
        else:
            t.insert(END,"out of index")








    except Exception as e:
        customtkinter.CTkLabel(fr_window,text=e).pack()

    t.pack(side=TOP,fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)


def hourly_forecast():
    global clk
    global clkde
    global butn2
    global h_window
    global bt
    global opt1
    hourly_window = customtkinter.CTkToplevel()
    hourly_window.title("hourly forecast")
    hourly_window.geometry("400x400")
    butn2.pack_forget()
    clkd = StringVar()
    lst1 = list()
    for i in range(0,24):
        lst1.append(str(i))
    clkd.set(lst1[0])
    drop = customtkinter.CTkOptionMenu(hourly_window,values=lst1,command=hour,variable=clkd)
    drop.pack()
    btn3 = customtkinter.CTkButton(hourly_window,text="submit",command=lambda selected_hour: hour(selected_hour))
    btn3.pack()

    h_window = hourly_window
    clkde = clkd
    bt = btn3
    opt1 = drop
def hour(selected_hour):
    global h_window
    global clkde
    global bt
    global opt1
    bt.pack_forget()
    opt1.pack_forget()
    h1 = Scrollbar(h_window, orient='horizontal')

    h1.pack(side=BOTTOM, fill=X)
    v1 = Scrollbar(h_window)

    v1.pack(side=RIGHT, fill=Y)
    t1 = Text(h_window, width=150, height=150, wrap=NONE, xscrollcommand=h1.set, yscrollcommand=v1.set)
    cty = inp1.get()

    api_link = 'http://api.weatherapi.com/v1/forecast.json?key='+config.API_KEY+'&q='+city+'&days=10&aqi=yes&alerts=yes'
    try:
        api_request = requests.get(api_link)
        x = json.loads(api_request.content)
        i = int(clk.get())-1
        j = int(clkde.get())
        time = str(x['forecast']['forecastday'][i]['hour'][j]['time'])
        temp_in_c = str(x['forecast']['forecastday'][i]['hour'][j]['temp_c'])
        wind_speed = str(x['forecast']['forecastday'][i]['hour'][j]['wind_mph'])
        precipitation = str(x['forecast']['forecastday'][i]['hour'][j]['precip_mm'])
        humidity = str(x['forecast']['forecastday'][i]['hour'][j]['humidity'])
        t1.insert(END,"time:"+time+"\n")
        t1.insert(END,"temperature in celsius:"+temp_in_c+"\n")
        t1.insert(END,"wind speed in mph:"+wind_speed+"\n")
        t1.insert(END,"precipitation:"+precipitation+"\n")
        t1.insert(END,"humidity:"+humidity+"\n")
    except Exception as e:
        print(e)
    t1.pack(side=TOP,fill=X)
    h1.config(command=t1.xview)
    v1.config(command=t1.yview)
    return
#New = Button(root,text="open new window",command=new)
#New.pack()
root.mainloop()
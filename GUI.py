from tkinter import *
import tkinter.font
import tkinter.ttk as ttk
import webbrowser
import requests
import datetime
import calendar
from pytz import timezone
import config

APIKEY = config.APIKEY


# Quit button class, closes GUI.
class quitButton(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        powerImg = PhotoImage(file = "guiImages\power.png")
        self.button = Button(master, image= powerImg, text="QUIT", command=master.quit, bd=0, highlightcolor="#91C46B",activebackground="#91C46B", bg="#91C46B")
        self.button.image = powerImg
        self.button.place(x=13,y=550)
# Settings button class, opens setting window when changing location.
class settingButton(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        powerImg = PhotoImage(file = "guiImages\settings.png")
        
        
        self.button = Button(master, image= powerImg, text="SETTINGS", command=settingWindow, bd=0, highlightcolor="#91C46B",activebackground="#91C46B", bg="#91C46B")
        self.button.image = powerImg
        self.button.place(x=13,y=500)
# Refresh button class, refreshes all the weather data and time intervals.
class refreshButton(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        powerImg =  PhotoImage(file = "guiImages\erefresh.png")
        self.button = Button(master, image= powerImg, text="REFRESH", command=displayCurrentConditions, bd=0,highlightcolor="#000000",activebackground="#1E2226", bg="#1E2226", relief = SUNKEN)
        self.button.image = powerImg
        self.button.place(x=977,y=14)

# Class to create the border design for the GUI.
class Border():
    def __init__(self, master=None):
        self.master = master
        bg = Canvas(self.master, width=1024, height=600, bd=0, highlightthickness=0, relief='ridge', background="#FFFFFF")
        bg.create_rectangle(60, 0, 1024, 59, fill="#34383C", outline="#393E42")
        bg.create_rectangle(0, 0, 60, 60, fill="#1E2226", outline="#23272C")
        bg.create_rectangle(0, 60, 60, 600, fill="#91C46B", outline="#97C774")
        bg.create_rectangle(213,528 , 337,529 , fill="#1E2226", outline="#1E2226")

        bg.create_rectangle(346,528 , 470,529 , fill="#1E2226", outline="#1E2226")
        bg.create_rectangle(479,528 , 603,529 , fill="#1E2226", outline="#1E2226")
        bg.create_rectangle(612,528 , 736,529 , fill="#1E2226", outline="#1E2226")
        bg.create_rectangle(745,528 , 869,529 , fill="#1E2226", outline="#1E2226")

        bg.create_rectangle(835, 0, 1024, 59, fill="#1E2226", outline="#23272C")
        bg.create_rectangle(500, 200, 900,201, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(500, 250, 900,251, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(500, 300, 900,301, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(75, 280, 76,315, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(873, 350, 874,585, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(208, 350, 874,351, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(208, 585, 874,584, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(208, 350, 209,585, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(341, 350, 342,585, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(474, 350, 475,585, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(607, 350, 608,585, fill="#A8A8A8", outline="#C9C9C9")
        bg.create_rectangle(740, 350, 741,585, fill="#A8A8A8", outline="#C9C9C9")
       
  
        bg.pack()
# Class for Logo design in GUI.
class Logo():
    def __init__(self, master=None):
        self.master = master
        logo = PhotoImage(file = "guiImages\cloud.png")
        cloudImage = Label(master, image=logo, bg="#1E2226")
        cloudImage.image = logo
        cloudImage.place(x=13,y=13)

# Class for new setting window to change location for weather.
class settingWindow():
    def __init__(self, master=None):
        self.master = master
        # Generates a top level window.
        self.settings_window = Toplevel(window, bg = "#7E848B", height= 500, width = 500)
        self.changeWindow()
        
        self.settings_window.transient(window)
        self.settings_window.grab_set()
        window.wait_window(self.settings_window)
        
    # Sets up the settings window for location data transported through the rest api
    def changeWindow(self):
        self.settings_window.resizable(0,0)
        self.bg = Canvas(self.settings_window, width=500, height=500, bd=0, highlightthickness=0, relief='ridge', background="#FFFFFF")
        self.bg.pack()
        map_image = PhotoImage(file = "guiImages\mapimage.png")
        self.mapLink = Label(self.settings_window, text="map", cursor="hand2", image=map_image, relief= RAISED)
        self.mapLink.image = map_image
        self.variable = StringVar(self.settings_window)
        self.mapLink.place(x=150, y=75)
        self.mapLink.bind("<Button-1>", lambda e: webbrowser.open_new("http://192.168.0.3/Web%20App%20Code/index.html"))
        
        self.save_button = Button(self.settings_window, text="Save", bd=0, command=self.get_Location, bg="#FFFFFF", fg="#4CA73E", font=("Impact", 25), relief =FLAT, activebackground="#4CA73E", activeforeground="#FFFFFF",height = 0, width = 7)
        self.save_button.place(x= 192, y= 400)
        self.settingsLabel = Label(self.settings_window, text="Settings", bg="#FFFFFF", fg="#000000", font=("Calibri", 30), bd = 0)
        self.settingsLabelfont = tkinter.font.Font(self.settingsLabel, self.settingsLabel.cget("font"))
        self.settingsLabelfont.configure(underline = True)
        self.settingsLabel.configure(font=self.settingsLabelfont)
        self.settingsLabel.place(x= 185, y= 10)
        self.city_names, self.data, self.ids = getLocationData()
        self.city_names = self.city_names
        setcity_names = list(set(self.city_names))
        self.variable = StringVar()
        self.w = ttk.Combobox(self.settings_window,textvariable = self.variable, state= "readonly", values= [*setcity_names])
        self.w.bind("<<ComboboxSelected>>",lambda e: self.settings_window.focus())
        self.w.configure(width = 20)
        self.w.configure(font = ("Calibri", 20 ))
        self.w.place(x= 100, y=310)
        self.chooseLable = Label(self.settings_window, text="Choose a city...", bg="#FFFFFF", fg="#878787", font=("Calibri", 12), bd = 0)
        self.chooseLable.place(x= 100, y=285)
        tooltip_image = PhotoImage(file = "guiImages\qmark.png")
        toolTipIcon = Label(self.settings_window, text="button 1", image=tooltip_image, bg="#FFFFFF")
        toolTipIcon.image = tooltip_image
        toolTipIcon.place(x=355, y=80)
        toolTipIcon_ttp = createToolTip(toolTipIcon, "Click on the map to choose\nthe city location within the web\nbrowser, then the city results will\nbe avaliable to choose from the\ndrop-down box.")
    # Gets the city location name from the settings window.
    def get_Location(self):
        city = self.variable.get()
        index = 0
        for i in self.city_names:
            
            if i == city:
                index = index
                saveDataTxt(index, self.data)
                break
            else:
                index += 1
        displayCurrentConditions()
# Tooltip class.
class createToolTip():
    
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
    # Mouse over event displays the text box with tooltip
    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # Creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background='white', relief='solid', borderwidth=1,
                       font=("times", "8", "normal"))
        label.pack(ipadx=1)
    # Mouse leave event destroys the text box on the tooltip
    def close(self, event=None):
        if self.tw:
            self.tw.destroy()
# Writes data of the city id location. IDs provided by openweathermap.org
def overwriteData(data1, data2, id):
    savedLatLngDataW = open("savedLatLngData.txt", "w")
    savedLatLngDataW.write(id)
    savedLatLngDataW.close()
    getConditions()
# Gets from API.
def saveDataTxt(index, data):
    city_id = data['list'][index]["id"]
    lat = data['list'][index]["coord"]["lat"]
    long = data['list'][index]["coord"]["lon"]
    overwriteData(lat, long, str(city_id))


# Gets all location data from API         
def getLocationData():
    # Rest API Address
    url2 = "http://127.0.0.1:5000/"
    res2 = requests.get(url2)
    data2 = res2.json()
    try:  
        lat = data2["coords"]["lat"]
        long = data2["coords"]["long"]
        lat = float(lat)
        long = float(long)
    except:
        print("Click on the map...")
    citynames = []
    ids = []
    # Weather data API address for specific location
    url3 = "http://api.openweathermap.org/data/2.5/find?lat={}&lon={}&cnt=10&appid={}".format(lat, long, APIKEY)
    res3 = requests.get(url3)
    data3 = res3.json()
    name = data3['list']
    for i in range(len(name)):
        cityname = data3['list'][i]["name"]
        citynames.append(cityname)
    for j in range(len(name)):
        id = data3['list'][i]["id"]
        ids.append(id)
  
    return citynames, data3, ids
# Gets current day and also the following to display on the GUI
def listOfWeekdays():
    list_of_weekdays = []
    # Timmezone set to this so the days line up with the 3/hr weather data blocks
    tz1 = timezone("Etc/GMT-3")
    for i in range(8):
        NextDay_Date = datetime.datetime.now(tz=tz1) + datetime.timedelta(days=i)
        NextDay_Date = NextDay_Date.weekday()
        Day = calendar.day_abbr[NextDay_Date]
        
        list_of_weekdays.append(Day)
    return list_of_weekdays
# Changes data and images for all respective times for 5 days.
def ChangeIcon(day_index, day_list):
    createDailyRadioButton.getButtonTimes
    cityi = cityid.get()
    firstIndexLength = (len(day_list[0]) - 1)
    # Day 1 Section
    if day_index == "1":
        if button1.get() == "0":
            acessDailyAPIData(0, cityi,day_index)
        if button1.get() == "1":
            acessDailyAPIData(1, cityi,day_index)
        if button1.get() == "2":
            acessDailyAPIData(2, cityi,day_index)
        file_directorystring1 = ("WeatherPics\{}.png").format(day_10_icon.get())
        icon_image1 = PhotoImage(file = file_directorystring1)
        WIcon_1image = Label(window, text="icon", image=icon_image1, bd=0)
        WIcon_1image.image = icon_image1
        daymaxt = Label(textvariable=day_10_maxt, bg="#FFFFFF", fg="#000000", font=("Verdana", 20), bd = 0)
        daymint = Label(textvariable=day_10_mint, bg="#FFFFFF", fg="#878787", font=("Verdana", 14), bd = 0)
        daymaxt.place(x=215,y= 465)
        daymint.place(x=215,y= 500)
        WIcon_1image.place(x=224, y=370)
    # Day 2 Section
    if day_index == "2":
        if button2.get() == "0":
            acessDailyAPIData((firstIndexLength+2), cityi,day_index)
        if button2.get() == "1":
            acessDailyAPIData((firstIndexLength+5), cityi,day_index)
        if button2.get() == "2":
            acessDailyAPIData((firstIndexLength+8), cityi,day_index)

        file_directorystring2 = ("WeatherPics\{}.png").format(day_20_icon.get())
        icon_image2 = PhotoImage(file = file_directorystring2)
        WIcon_2image = Label(window, text="icon", image=icon_image2, bd=0)
        WIcon_2image.image = icon_image2
        daymaxt2 = Label(textvariable=day_20_maxt, bg="#FFFFFF", fg="#000000", font=("Verdana", 20), bd = 0)
        daymint2 = Label(textvariable=day_20_mint, bg="#FFFFFF", fg="#878787", font=("Verdana", 14), bd = 0)
        daymaxt2.place(x=348,y= 465)
        daymint2.place(x=348,y= 500)

        WIcon_2image.place(x=357, y=370)
    # Day 3 Section
    if day_index == "3":
        if button3.get() == "0":
            acessDailyAPIData((firstIndexLength+10), cityi,day_index)
        if button3.get() == "1":
            acessDailyAPIData((firstIndexLength+13), cityi,day_index)
        if button3.get() == "2":
            acessDailyAPIData((firstIndexLength+16), cityi,day_index)

        file_directorystring3 = ("WeatherPics\{}.png").format(day_30_icon.get())
        icon_image3 = PhotoImage(file = file_directorystring3)
        WIcon_3image = Label(window, text="icon", image=icon_image3, bd=0)
        WIcon_3image.image = icon_image3
        daymaxt3 = Label(textvariable=day_30_maxt, bg="#FFFFFF", fg="#000000", font=("Verdana", 20), bd = 0)
        daymint3 = Label(textvariable=day_30_mint, bg="#FFFFFF", fg="#878787", font=("Verdana", 14), bd = 0)
        daymaxt3.place(x=481,y= 465)
        daymint3.place(x=481,y= 500)
        WIcon_3image.place(x=490, y=370)
    # Day 4 Section
    if day_index == "4":
        if button4.get() == "0":
            acessDailyAPIData(firstIndexLength+18, cityi,day_index)
        if button4.get() == "1":
            acessDailyAPIData(firstIndexLength+21, cityi,day_index)
        if button4.get() == "2":
            acessDailyAPIData(firstIndexLength+24, cityi,day_index)

        file_directorystring4 = ("WeatherPics\{}.png").format(day_40_icon.get())
        icon_image4 = PhotoImage(file = file_directorystring4)
        WIcon_4image = Label(window, text="icon", image=icon_image4, bd=0)
        WIcon_4image.image = icon_image4
        daymaxt4 = Label(textvariable=day_40_maxt, bg="#FFFFFF", fg="#000000", font=("Verdana", 20), bd = 0)
        daymint4 = Label(textvariable=day_40_mint, bg="#FFFFFF", fg="#878787", font=("Verdana", 14), bd = 0)
        daymaxt4.place(x=614,y= 465)
        daymint4.place(x=614,y= 500)
        WIcon_4image.place(x=623, y=370)
    # Day 5 Section
    if day_index == "5":
        if button5.get() == "0":
            acessDailyAPIData(firstIndexLength+26, cityi,day_index)
        if button5.get() == "1":
            acessDailyAPIData(firstIndexLength+29, cityi,day_index)
        if button5.get() == "2":
            acessDailyAPIData(firstIndexLength+31, cityi,day_index)

        file_directorystring5 = ("WeatherPics\{}.png").format(day_50_icon.get())
        icon_image5 = PhotoImage(file = file_directorystring5)
        WIcon_5image = Label(window, text="icon", image=icon_image5, bd=0)
        WIcon_5image.image = icon_image5
        daymaxt5 = Label(textvariable=day_50_maxt, bg="#FFFFFF", fg="#000000", font=("Verdana", 20), bd = 0)
        daymint5 = Label(textvariable=day_50_mint, bg="#FFFFFF", fg="#878787", font=("Verdana", 14), bd = 0)
        daymaxt5.place(x=747,y= 465)
        daymint5.place(x=747,y= 500)
        WIcon_5image.place(x=756, y=370)

# Creates the radio buttons for each day
class createDailyRadioButton():
    def __init__(self, xcoord, var, day_index, timeVariable1,timeVariable2,timeVariable3 ):
        buttonValue = [0, 1, 2]
        self.radiobuttonList = []
        self.day_index = day_index
        self.dayList = self.makeTimeSeperations()
        self.r1 = Radiobutton(window, variable = var,textvariable=timeVariable1, value = buttonValue[0], indicatoron= 0, background="#91C46B",activebackground ="#CCCCCC", command=lambda: ChangeIcon(self.day_index,self.dayList), height=3, width=5, bd=0, relief=FLAT)
        self.r1.place(x = xcoord+42, y =530)
        self.r2 = Radiobutton(window, variable = var,textvariable=timeVariable2, value = buttonValue[1], indicatoron= 0, background="#91C46B",activebackground ="#CCCCCC", command=lambda: ChangeIcon(self.day_index,self.dayList), height=3, width=5, bd=0, relief=FLAT)
        self.r2.place(x = xcoord+84, y =530)
        self.r3 = Radiobutton(window, variable = var,textvariable=timeVariable3, value = buttonValue[2], indicatoron= 0, background="#91C46B",activebackground ="#CCCCCC", command=lambda: ChangeIcon(self.day_index,self.dayList), height=3, width=5, bd=0, relief=FLAT)
        self.r3.place(x = xcoord+126, y =530)
        self.radiobuttonList.append(self.r1)
        self.getButtonTimes()
        self.radiobuttonList.append(self.r2)

        self.radiobuttonList.append(self.r3)
        
        xcoord = int(xcoord)
        xcoord += 42
       
    def updateRadioButtons(self):
        ChangeIcon(self.day_index, self.dayList)

    # Gets the times for each individual button to display on GUI.
    def getButtonTimes(self):
        url4 = "http://api.openweathermap.org/data/2.5/forecast?id={}&appid={}&units=metric".format(cityid.get(), APIKEY)
        res4 = requests.get(url4)
        self.day_data = res4.json()
        self.dayList = self.makeTimeSeperations()
        if self.day_index == "1":
            day_10_time.set(self.dayList[0][0])
            try:
                day_11_time.set(self.dayList[0][1])
            except:
                # Checks to see if there is no other time apart from one on that day. Other buttons are disabled because there are no other times.
                if day_10_time.get() == "21:00":
                    day_11_time.set("")      
                    self.r2.config(state ="disabled")
                    day_12_time.set("")
                    self.r3.config(state ="disabled")
            try:        
                day_12_time.set(self.dayList[0][2])
            except:
                if day_11_time.get() == "21:00":
                    day_12_time.set("")
                    self.r3.config(state = "disabled")
        # Sets times of all respective days.
        if self.day_index == "2":
            day_20_time.set(self.dayList[1][1])
            
            day_21_time.set(self.dayList[1][4])
                        
            day_22_time.set(self.dayList[1][7])
        if self.day_index == "3":
            day_30_time.set(self.dayList[2][1])
            
            day_31_time.set(self.dayList[2][4])
                        
            day_32_time.set(self.dayList[2][7])
        if self.day_index == "4":
            day_40_time.set(self.dayList[3][1])
            
            day_41_time.set(self.dayList[3][4])
                        
            day_42_time.set(self.dayList[3][7])
        if self.day_index == "5":
            day_50_time.set(self.dayList[4][1])
            
            day_51_time.set(self.dayList[4][4])
                        
            day_52_time.set(self.dayList[4][6])
    # Checks the time comapred to the data.
    def checkTimes(self,indexstart,indexend):

        for i in range(indexstart,indexend):
            data = self.day_data["list"][i]["dt_txt"]
            data = data[11:16]
            if data == "00:00":
                return i
    # Seperateds times into 3 hour segments.
    def makeTimeSeperations(self):
        tempurl4 = "http://api.openweathermap.org/data/2.5/forecast?id={}&appid={}&units=metric".format(cityid.get(), APIKEY)
        tempres4 = requests.get(tempurl4)
        self.day_data = tempres4.json()
        daysList = [[],[],[],[],[]]
        dayindex = 0
        for i in range(0,39):
            dataJSON = self.day_data["list"][i]["dt_txt"]
            if i != 0:
                prevDataJSON = self.day_data["list"][(i-1)]["dt_txt"]
                currentdata = dataJSON[0:11]
                prevdata = prevDataJSON[0:11]
                if currentdata == prevdata:
                    if dayindex != 5:
                        daysList[dayindex].append(dataJSON[11:16])
                else:
                    dayindex += 1
                    if dayindex != 5:
                        daysList[dayindex].append(dataJSON[11:16])
            else:
                daysList[dayindex].append(dataJSON[11:16])

        return daysList
# Gets the weather data from the API and sets the dynamic variables with that data
def acessDailyAPIData(index, city_id, day_index):
    # Weather data API address
    url4 = "http://api.openweathermap.org/data/2.5/forecast?id={}&appid={}&units=metric".format(city_id, APIKEY)
    res4 = requests.get(url4)
    day_data = res4.json()

    day10_max = day_data["list"][index]["main"]["temp_max"]
    
    day10_min = day_data["list"][index]["main"]["temp_min"]
    day10_icon = day_data["list"][index]["weather"][0]["icon"]

    if day_index == "1":
        day_10_mint.set(str(int(day10_min))+"°")
        day_10_maxt.set(str(int(day10_max))+"°")
        day_10_icon.set(day10_icon)
    elif day_index == "2":
        day_20_mint.set(str(int(day10_min))+"°")
        day_20_maxt.set(str(int(day10_max))+"°")
        day_20_icon.set(day10_icon)
    elif day_index == "3":
        day_30_mint.set(str(int(day10_min))+"°")
        day_30_maxt.set(str(int(day10_max))+"°")
        day_30_icon.set(day10_icon)
    elif day_index == "4":
        day_40_mint.set(str(int(day10_min))+"°")
        day_40_maxt.set(str(int(day10_max))+"°")
        day_40_icon.set(day10_icon)
    elif day_index == "5":
        day_50_mint.set(str(int(day10_min))+"°")
        day_50_maxt.set(str(int(day10_max))+"°")
        day_50_icon.set(day10_icon)
    else:
        print("Error Getting Data")

# Displays the data on the GUI and sets other dynamic variables
def displayCurrentConditions():
    # Gets the current date.
    now = datetime.datetime.now()
    daytime_string = now.strftime("%d/%m/%Y - %H:%M:%S")
    weekday_list = listOfWeekdays()

    savedLatLngData = open("savedLatLngData.txt", "r")
    city_id = savedLatLngData.read()
    url3 = "http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric".format(city_id,APIKEY)
    res3 = requests.get(url3)
    data = res3.json()
    cityid.set(city_id)

    temp_data = data["main"]["temp"]
    fltemp_data = data["main"]["feels_like"]
    humidity_data = data["main"]["humidity"]
    pressure_data = data["main"]["pressure"]
    windspeed_data = data["wind"]["speed"]
    main_data = data["weather"][0]["main"]
    description_data = data["weather"][0]["description"]
    icon_data = data["weather"][0]["icon"]
    name_data = data["name"]
    day_1.set(weekday_list[0])
    day_2.set(weekday_list[1])
    day_3.set(weekday_list[2])
    day_4.set(weekday_list[3])
    day_5.set(weekday_list[4])

    city_name.set(name_data)
    city_temp.set(str(int(temp_data))+"℃")
    city_fltemp.set("Feels like "+str(int(fltemp_data))+"℃")
    city_humidity.set(str(humidity_data)+"%")
    msTomph = int(windspeed_data*2.23694)
   
    city_windspeed.set(str(msTomph)+"mph")
    city_main.set(main_data)
    city_pressure.set(str(pressure_data)+"hPa")
    city_description.set(description_data)

    city_icon.set(str(icon_data))
    last_refreshed.set("Last Updated: "+str(daytime_string))
    file_directorystring = ("WeatherPics\{}.png").format(icon_data)

    icon_image = PhotoImage(file = file_directorystring)
    WIcon_image = Label(window, text="icon", image=icon_image, bd=0)
    WIcon_image.image = icon_image
    WIcon_image.place(x=100, y=170)

    # Creates radio buttons for respective days
    day1 = createDailyRadioButton(171, button1,"1",day_10_time,day_11_time,day_12_time)
    day2 = createDailyRadioButton(304, button2,"2",day_20_time,day_21_time,day_22_time)
    day3 = createDailyRadioButton(437, button3,"3",day_30_time,day_31_time,day_32_time)
    day4 = createDailyRadioButton(570, button4,"4",day_40_time,day_41_time,day_42_time)
    day5 = createDailyRadioButton(703, button5,"5",day_50_time,day_51_time,day_52_time)
    # Calls update function for all radio buttons
    day1.updateRadioButtons()
    day2.updateRadioButtons()
    day3.updateRadioButtons()
    day4.updateRadioButtons()
    day5.updateRadioButtons()
# Places aspects on GUI.
def getConditions():
    displayCurrentConditions()

    day1tag = Label(textvariable=day_1, bg="#FFFFFF", fg="#000000", font=("Verdana", 10), bd = 0)
    day2tag = Label(textvariable=day_2, bg="#FFFFFF", fg="#000000", font=("Verdana", 10), bd = 0)
    day3tag = Label(textvariable=day_3, bg="#FFFFFF", fg="#000000", font=("Verdana", 10), bd = 0)
    day4tag = Label(textvariable=day_4, bg="#FFFFFF", fg="#000000", font=("Verdana", 10), bd = 0)
    day5tag = Label(textvariable=day_5, bg="#FFFFFF", fg="#000000", font=("Verdana", 10), bd = 0)
    showcasedTemp = Label(textvariable=city_temp, bg="#FFFFFF", fg="#000000", font=("Verdana", 30), bd = 0)
    showcasedRefreshed = Label(textvariable=last_refreshed, bg="#FFFFFF", fg="#878787", font=("Verdana", 9), bd = 0)
    showcasedMain = Label(textvariable=city_main, bg="#FFFFFF", fg="#000000", font=("Calibri", 20), bd = 0)
    showcasedFLTemp = Label(textvariable=city_fltemp, bg="#FFFFFF", fg="#878787", font=("Verdana", 10), bd = 0)
    showcasedName = Label(textvariable=city_name, bg="#FFFFFF", fg="#000000", font=("Calibri", 44, ), bd = 0)
    showcasedHum = Label(textvariable=city_humidity, bg="#FFFFFF", fg="#878787", font=("Calibri", 16), bd = 0)
    showcasedWS = Label(textvariable=city_windspeed, bg="#FFFFFF", fg="#878787", font=("Calibri", 16), bd = 0)
    showcasedPress = Label(textvariable=city_pressure, bg="#FFFFFF", fg="#878787", font=("Calibri", 16), bd = 0)
    hum_tag = Label(text="Humidity", bg="#FFFFFF", fg="#878787", font=("Calibri", 16), bd = 0)
    ws_tag = Label(text="Wind speed", bg="#FFFFFF", fg="#878787", font=("Calibri", 16), bd = 0)
    press_tag = Label(text="Pressure", bg="#FFFFFF", fg="#878787", font=("Calibri", 16), bd = 0)
    now_tag = Label(text="NOW", bg="#FFFFFF", fg="#000000", font=("Calibri", 12), bd = 0)
    underlinedFont = tkinter.font.Font(now_tag, now_tag.cget("font"))
    underlinedFont.configure(underline=True)
    drop_image = PhotoImage(file = "guiImages\drop.png")
    hum_image = Label(window, text="drop", image=drop_image, bd=0)
    hum_image.image = drop_image

    wind_image = PhotoImage(file = "guiImages\wind.png")
    WS_image = Label(window, text="WS", image=wind_image, bd=0)
    WS_image.image = wind_image
    pressure_image = PhotoImage(file = "guiImages\pressure.png")
    Press_image = Label(window, text="Pressure", image=pressure_image, bd=0)
    Press_image.image = pressure_image

    tooltip_image = PhotoImage(file = "guiImages\qmark.png")
    toolTipIcon = Label(window, text="button 1", image=tooltip_image, bg="#FFFFFF")
    toolTipIcon.image = tooltip_image
    toolTipIcon.place(x=880, y=355)
    toolTipIcon_ttp = createToolTip(toolTipIcon, "All times are based off\nthe UTC timezone.")

    now_tag.configure(font=underlinedFont)
    now_tag.place(x=80, y=70)
    hum_tag.place(x=505, y= 165)
    showcasedRefreshed.place(x=760,y=60)
    ws_tag.place(x=505, y= 215)
    press_tag.place(x=505,y=265)
    showcasedName.place(x=80,y=80)
    showcasedTemp.place(x=250,y=190)
    showcasedPress.place(x=820, y=265 )
    showcasedHum.place(x=860, y=165)
    showcasedMain.place(x=80,y=280)
    hum_image.place(x=473,y=170)
    showcasedWS.place(x=840, y=215)
    Press_image.place(x=473,y=265)
    WS_image.place(x=473,y=215)
    showcasedFLTemp.place(x=255,y=240)
    day1tag.place(x=213, y=355)
    day2tag.place(x=346, y=355)

    day3tag.place(x=479, y=355)
    day4tag.place(x=612, y=355)
    day5tag.place(x=745, y=355)
 

# Creates master window (GUI)    
window = Tk()

# Initilises GUI aspects.
border = Border(master=window)
quit_button = quitButton(master=window)
cloud_logo = Logo(master=window)
settings_button = settingButton(master=window)
refresh_button = refreshButton(master=window)

window.title("Weather App")
window.resizable(0,0)
savedLatLngData = open("savedLatLngData.txt", "r")
data = savedLatLngData.read()

# Current Dynamic Variables
cityid = StringVar()
city_name = StringVar()
city_temp = StringVar()
city_fltemp = StringVar()
city_humidity = StringVar()
city_windspeed = StringVar()
city_main = StringVar()
city_description = StringVar()
city_icon = StringVar()
city_pressure = StringVar()
last_refreshed = StringVar()


# Day 1 Variables
day_1 = StringVar()

day_10_mint = StringVar()
day_10_maxt = StringVar()
day_10_icon = StringVar()

day_10_time = StringVar()
day_11_time = StringVar() 
day_12_time = StringVar() 


# Day 2 Variables
day_2 = StringVar()

day_20_mint = StringVar()
day_20_maxt = StringVar()
day_20_icon = StringVar()

day_20_time = StringVar()
day_21_time = StringVar()
day_22_time = StringVar()


# Day 3 Variables
day_3 = StringVar()

day_30_mint = StringVar()
day_30_maxt = StringVar()
day_30_icon = StringVar()

day_30_time = StringVar()
day_31_time = StringVar()
day_32_time = StringVar()

# Day 4 Variables
day_4 = StringVar()

day_40_mint = StringVar()
day_40_maxt = StringVar()
day_40_icon = StringVar()

day_40_time = StringVar()
day_41_time = StringVar()
day_42_time = StringVar()

# Day 5 Variables
day_5 = StringVar()

day_50_mint = StringVar()
day_50_maxt = StringVar()
day_50_icon = StringVar()

day_50_time = StringVar()
day_51_time = StringVar()
day_52_time = StringVar()



button1 = StringVar(window, 0)
button2 = StringVar(window, 1)
button3 = StringVar(window, 1)
button4 = StringVar(window, 1)
button5 = StringVar(window, 1)


if len(data) == 0:
    
    print("No Data INSIDE")
else:
  
    getConditions()
    print("Data INSIDE")

window.mainloop()

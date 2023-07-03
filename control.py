from tkinter import *
import tkinter as tk
import customtkinter as ctk
import random
import os
import location
import main
country="india"
temperature=39.0090
temperature=str(temperature)
maximum_temperature=42.890
maximum_temperature=str(maximum_temperature)
minimum_temparature=20.1404
feels_like=0.100
feels_like=str(feels_like)
minimum_temparature=str(minimum_temparature)
humidity=70.89
humidity=str(humidity)
air_pressure=10.00
air_pressure=str(air_pressure)
air_speed=11.00
air_speed=str(air_speed)

town="kolkata"
window=Tk()
window.geometry('520x650+725+0')
window.title('weather app')
icon=os.path.join('assests','icon','darkpheonix.png')
window.resizable(False,False)
icon=PhotoImage(file=icon)
window.iconphoto(False,icon)
window.config(bg="#FAF2DF",pady=5)
def clear_widgets():
    for widgets in window.winfo_children():
        widgets.destroy()
class firstpage:
    def __init__(self):
        clear_widgets()
        first_frame=ctk.CTkFrame(window,fg_color='#32CC32',corner_radius=15)
        first_frame.pack(side=TOP,pady=5)
        second_frame=ctk.CTkFrame(window,fg_color='#808000',corner_radius=15)
        second_frame.pack(side=TOP,pady=5)
        third_frame=ctk.CTkFrame(window,fg_color="black",corner_radius=15)
        third_frame.pack(side=TOP,pady=5)

        def first_frame_widgets(first_frame):

            title_label=ctk.CTkLabel(first_frame,text='Weather App',text_color='black',font=("poppins",30,"bold"),height=50,width=250,corner_radius=20,fg_color='#55CEFF',bg_color='transparent')
            title_label.pack(side=TOP,pady=5)
            box=os.path.join('assests','search','searchbox.png')
            search_box=PhotoImage(file=box)
            search_box_label=ctk.CTkLabel(first_frame,image=search_box,width=500,text=None)
            search_box_label.pack(side=TOP,pady=5)
            engine=os.path.join('assests','search','searchengine.png')
            search_icon=PhotoImage(file=engine)
            def get_details():
                global town
                town=city_name_entry_label.get()
                print(town)
                secondpage()
            search_icon_label=ctk.CTkButton(first_frame,image=search_icon,text=None,width=0,height=0,fg_color='#C5E1EC',bg_color="#C5E1EC",hover=False,cursor="hand2",command=get_details)
            search_icon_label.place(x=341,y=160)
            city_name_label=ctk.CTkLabel(first_frame,text="Enter City Name",font=('ubuntu',17),width=10,text_color='black',bg_color="#C5E1EC")
            city_name_label.place(x=140,y=75)
            city_name_entry_label=ctk.CTkEntry(first_frame,font=("poppins",25),text_color="black",height=15,fg_color="transparent",bg_color="#8FBEDC",width=200,border_width=0)
            city_name_entry_label.place(x=130,y=130)
            disclaimer_label=ctk.CTkLabel(first_frame,text="DISCLAIMER: Enter the city name and press the search button",text_color='black',font=('ubuntu',13),fg_color="transparent",bg_color="transparent")
            disclaimer_label.pack(side=TOP,pady=5)
        def second_frame_widgets(second_frame):
            city_folder=os.path.join('assests','citys')
            citys=os.listdir(city_folder)
            random.shuffle(citys)
            button_dir={}
            img={}
            label_dir={}
            frame_dir={}
            random_name_label=ctk.CTkLabel(second_frame,text="Random City",font=('poppins',30,'bold'),height=50,width=250,text_color='black',fg_color="#FADA5F",corner_radius=20)
            random_name_label.pack(side=TOP,pady=5)
            button_frame=ctk.CTkFrame(second_frame,bg_color="transparent",fg_color="transparent")
            button_frame.pack(side=TOP)
            def get_city(city):
                global town
                town=city
                print(city)
                secondpage()
            for city in citys[:4]:
                frame_dir[city]=ctk.CTkFrame(button_frame,fg_color="transparent",bg_color="transparent")
                frame_dir[city].pack(side=LEFT)
                img[city]=PhotoImage(file=os.path.join(city_folder,city))
                button_dir[city]=ctk.CTkButton(frame_dir[city],image=img[city],text=None,height=0,width=0,hover=True,hover_color='gray75',cursor='hand2',fg_color="transparent",bg_color="transparent",command=lambda:get_city(city=city[:-4]))
                button_dir[city].pack(side=TOP)
                label_dir[city]=ctk.CTkLabel(frame_dir[city],text=city[:-4].capitalize(),font=('ubuntu',15,'bold'),fg_color="transparent",bg_color="transparent",text_color="white",width=125)
                label_dir[city].pack(side=TOP,pady=3)
            disclaimer_label=ctk.CTkLabel(second_frame,text="DISCLAIMER: Press any of the city for the instant search",text_color='black',font=('ubuntu',13),fg_color="transparent",bg_color="transparent")
            disclaimer_label.pack(side=TOP,pady=5)
        def third_frame_widgets(third_frame):
            city,country=location.location_extraction.current_location()
            information=main.get_information(city=city)
            description=ctk.CTkLabel(third_frame,text="Current Location",font=("poppins",20),width=490)
            description.pack(side=TOP,pady=5,padx=5)
            location_frame=ctk.CTkFrame(third_frame,bg_color="transparent",fg_color="transparent")
            location_frame.pack(side=LEFT,padx=5,pady=5)
            information_frame=ctk.CTkFrame(third_frame,bg_color="transparent",fg_color="transparent")
            information_frame.pack(side=RIGHT,padx=5,pady=5)
            temperature="--"
            if information[0]==True:
                temperature=information[1][0]
            else:
                temperature="--"
            location_city=ctk.CTkLabel(location_frame,text=city.upper(),font=("Impact",50),width=0,height=0,text_color="red",bg_color="transparent",fg_color="transparent")
            location_city.place(x=10,y=0)
            temperature_city=ctk.CTkLabel(information_frame,text=temperature,width=0,height=0,text_color="white",font=("Impact",50),bg_color="transparent",fg_color="transparent")
            temperature_city.place(x=100,y=0)
            degree_label=ctk.CTkLabel(information_frame,text=chr(176),width=0,height=0,text_color="white",font=("Impact",40),bg_color="transparent",fg_color="transparent")
            degree_label.place(x=153,y=0)
            celcius_label=ctk.CTkLabel(information_frame,text="C",width=0,height=0,text_color="white",font=("Impact",30),bg_color="transparent",fg_color="transparent")
            celcius_label.place(x=153,y=20)
        first_frame_widgets(first_frame=first_frame)
        second_frame_widgets(second_frame=second_frame)
        third_frame_widgets(third_frame=third_frame)
class secondpage:

    def __init__(self):  
        clear_widgets()
        def update():
            global country
            global temperature
            global maximum_temperature
            global minimum_temparature
            global feels_like
            global humidity
            global air_pressure
            global air_speed
            information=main.get_information(town)
            if information[0]==True:
                country=information[1][10]
                temperature=information[1][0]
                maximum_temperature=information[1][1]
                minimum_temparature=information[1][2]
                feels_like=information[1][3]
                humidity=information[1][4]
                air_pressure=information[1][8]
                air_speed=information[1][9]
            else:
                country="--"
                temperature="--"
                maximum_temperature="--"
                minimum_temparature="--"
                feels_like="--"
                humidity="--"
                air_pressure="--"
                air_speed="--"
        update()
        first_frame=ctk.CTkFrame(window,fg_color='red',corner_radius=15)
        first_frame.pack(side=TOP,pady=5)
        second_frame=ctk.CTkFrame(window,fg_color='black',corner_radius=15)
        second_frame.pack(side=TOP,pady=5)
        third_frame=ctk.CTkFrame(window,fg_color='red',corner_radius=15)
        third_frame.pack(side=TOP)
        def first_frame_widgets(first_frame):
            title_label=ctk.CTkLabel(first_frame,text='Weather App',text_color='green',font=("poppins",30,"bold"),height=50,width=25,corner_radius=20,fg_color='black',bg_color='transparent')
            title_label.pack(side=TOP,pady=5,padx=100)
            searchbar_frame=ctk.CTkFrame(first_frame,bg_color="transparent",fg_color="pink",width=450)
            searchbar_frame.pack(side=TOP,padx=5,pady=5)
            search=PhotoImage(file=os.path.join('assests','search','searchnew.png'))
            searchbar=ctk.CTkLabel(searchbar_frame,image=search,text=None)
            searchbar.place(x=50,y=-50)
            def get_details():
                global town
                town=entry_label.get()
                print(town)
                secondpage()
            entry_label=ctk.CTkEntry(searchbar_frame,text_color="red",width=230,height=15,font=("poppins",25),bg_color="transparent",fg_color="transparent",border_width=0)
            entry_label.place(x=100,y=23)
            search_icon=PhotoImage(file=os.path.join('assests','search','searchicon.png'))
            search_button=ctk.CTkButton(searchbar_frame,image=search_icon,text=None,width=0,height=30,bg_color="transparent",border_width=0,fg_color="transparent",cursor="hand2",hover=False,command=get_details)
            search_button.place(x=325,y=23)
            city_name=ctk.CTkLabel(searchbar_frame,text=town.upper(),font=("Impact",30),text_color="black",bg_color="transparent",fg_color="transparent")
            city_name.place(x=10,y=90)
            country_name=ctk.CTkLabel(searchbar_frame,text=country.upper(),font=("Impact",20),text_color="black",bg_color="transparent",fg_color="transparent")
            country_name.place(x=10,y=125)
            temperature_city=ctk.CTkLabel(searchbar_frame,text=temperature,width=0,height=0,text_color="black",font=("Impact",50),bg_color="transparent",fg_color="transparent")
            temperature_city.place(x=350,y=90)
            degree_label=ctk.CTkLabel(searchbar_frame,text=chr(176),width=0,height=0,text_color="black",font=("Impact",40),bg_color="transparent",fg_color="transparent")
            degree_label.place(x=403,y=90)
            celcius_label=ctk.CTkLabel(searchbar_frame,text="C",width=0,height=0,text_color="black",font=("Impact",30),bg_color="transparent",fg_color="transparent")
            celcius_label.place(x=403,y=110)
        def second_frame_widgets(second_frame):
            left_widget=ctk.CTkFrame(second_frame,width=455,bg_color="transparent",fg_color="transparent")
            left_widget.pack(side=TOP,padx=5,pady=5)
            maximum_temperature_label=ctk.CTkLabel(left_widget,text="Today Maximum temerature of {} : {}{}C".format(town,maximum_temperature,chr(176)),font=("poppins",17),text_color="white",bg_color="transparent",fg_color="transparent")
            maximum_temperature_label.place(x=10,y=10)
            minimum_temperature_label=ctk.CTkLabel(left_widget,text="Today Minimum temerature of {} : {}{}C".format(town,minimum_temparature,chr(176)),font=("poppins",17),text_color="white",bg_color="transparent",fg_color="transparent")
            minimum_temperature_label.place(x=10,y=40)
            feels_like_label=ctk.CTkLabel(left_widget,text="The Current temperature of {} feels like : {}{}C".format(town,feels_like,chr(176)),font=("poppins",17),text_color="white",bg_color="transparent",fg_color="transparent")
            feels_like_label.place(x=10,y=70)
            humidity_label=ctk.CTkLabel(left_widget,text="The current humidity level of {} : {}%".format(town,humidity),font=("poppins",17),text_color="white",bg_color="transparent",fg_color="transparent")
            humidity_label.place(x=10,y=100)
            air_pressure_label=ctk.CTkLabel(left_widget,text="Current air pressure of {} : {}hpa".format(town,air_pressure),font=("poppins",17),text_color="white",bg_color="transparent",fg_color="transparent")
            air_pressure_label.place(x=10,y=130)
            air_speed_label=ctk.CTkLabel(left_widget,text="Current air speed of {} : {}m/s".format(town,air_speed),font=("poppins",17),text_color="white",bg_color="transparent",fg_color="transparent")
            air_speed_label.place(x=10,y=160)
        def third_frame_widgets(third_frame):
            home=PhotoImage(file=os.path.join('assests','search','homebutton.png'))
            home_button=ctk.CTkButton(third_frame,image=home,text=None,bg_color='transparent',fg_color='transparent',hover=False,cursor='hand2',command=firstpage)
            home_button.pack(padx=10,pady=10)
        first_frame_widgets(first_frame=first_frame)
        second_frame_widgets(second_frame=second_frame)
        third_frame_widgets(third_frame=third_frame)
if __name__=="__main__":
    firstpage()
window.mainloop()
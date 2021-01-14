from tkinter import *

from bs4 import BeautifulSoup #html veri arama

import requests

#Ankara
request=requests.get("https://www.hurriyet.com.tr/hava-durumu/ankara/")
text=request.text
b = BeautifulSoup(text, 'html.parser')
classDerece="weather-detail-hightemp" # html deki class i "weather-detail-hightemp" olan veriyi aramak icin bu stringi degiskene attım
derece1=b.find(class_=classDerece).get_text() #html veri > ( <p class="weather-detail-hightemp">0<sup class="degree">°</sup><sup class="celcius">C</sup></p> )

#istanbul
request=requests.get("https://www.hurriyet.com.tr/hava-durumu/istanbul/")
text=request.text
b = BeautifulSoup(text, 'html.parser')
classDerece="weather-detail-hightemp"
derece2=b.find(class_=classDerece).get_text()

#zonguldak
request=requests.get("https://www.hurriyet.com.tr/hava-durumu/zonguldak/")
text=request.text
b = BeautifulSoup(text, 'html.parser')
classDerece="weather-detail-hightemp"
derece3=b.find(class_=classDerece).get_text()

pencere = Tk()
pencere.title("Hava Durumu")

lankara=Label(pencere,text="Ankara",bg="white",highlightcolor="blue",borderwidth=2, relief="groove")
lankara.config(font=("Courier", 20))
lankara.place(relx=0.20, rely=0.3, anchor=CENTER);

listanbul=Label(pencere,text="Istanbul",bg="white",highlightcolor="blue",borderwidth=2, relief="groove")
listanbul.config(font=("Courier", 20))
listanbul.place(relx=0.46, rely=0.3, anchor=CENTER);

lzonguldak=Label(pencere,text="Zonguldak",bg="white",highlightcolor="blue",borderwidth=2, relief="groove")
lzonguldak.config(font=("Courier", 20))                                                                                  
lzonguldak.place(relx=0.74, rely=0.3, anchor=CENTER);

lderece1=Label(pencere,text=derece1,bg="white") # texti htmlden elde ettimiz derece
lderece1.config(font=("Courier", 20))
lderece1.place(relx=0.20, rely=0.5, anchor=CENTER);
lderece2=Label(pencere,text=derece2,bg="white")
lderece2.config(font=("Courier", 20))
lderece2.place(relx=0.46, rely=0.5, anchor=CENTER);
lderece3=Label(pencere,text=derece3,bg="white")
lderece3.config(font=("Courier", 20))
lderece3.place(relx=0.74, rely=0.5, anchor=CENTER);
pencere.geometry("600x300");
pencere.mainloop()
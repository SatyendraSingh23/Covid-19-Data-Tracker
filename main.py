import tkinter as tk
import bs4 
import plyer
import requests
import threading
import time
import datetime
from bs4 import BeautifulSoup


city_information=[]
corona_url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
headers = {
	'x-rapidapi-key': "5da47e4009msh038c747a3a2a74fp17f53ajsn43de3c1d19f3",
	'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
	}
response = requests.request("GET", corona_url, headers=headers).json()

def getDataFromURL(url) :
    data=requests.get(url)
    return data

	
def getInternetLocation() :
	htmlData=getDataFromURL("https://www.google.com/search?q=show+my+location")
	soup=BeautifulSoup(htmlData.text,"html.parser")
	data=soup.find('span',id="xxxXMc")
	return data.text
	

def defaultCityInformation(state_name,city_name) :
	city_information.clear()
	city_info=response['state_wise'][state_name]['district'][city_name]
	city_information.append(str(city_info['active']))
	city_information.append(str(city_info['confirmed']))
	city_information.append(str(city_info['deceased']))
	city_information.append(str(city_info['recovered']))
	city_information.append(str(city_info['delta']['confirmed']))
	city_information.append(str(city_info['delta']['deceased']))
	city_information.append(str(city_info['delta']['recovered']))
def search_by_city():	
	ct=city.get().strip()
	city_information.clear()
	city_info=[]
	flag=0
	try:
		for each in response['state_wise'] :
			if int(response['state_wise'][each]['active'])!=0 :
				for city_name in response['state_wise'][each]['district'] :
					if ct.lower()==city_name.lower():
						flag=1
						city_info=response['state_wise'][each]['district'][city_name]
						city_information.append(str(city_info['active']))
						city_information.append(str(city_info['confirmed']))
						city_information.append(str(city_info['deceased']))
						city_information.append(str(city_info['recovered']))
						city_information.append(str(city_info['delta']['confirmed']))
						city_information.append(str(city_info['delta']['deceased']))
						city_information.append(str(city_info['delta']['recovered']))
						current_city_name_label.config(text="                                  ")
						city_name_label.config(text=ct.title())
						city_active_label.config(text="Active\n"+city_information[0])
						city_confirmed_label.config(text="Confirmed\n"+city_information[1])
						city_death_label.config(text="Deaths\n"+city_information[2])
						city_recovered_label.config(text="Recovered\n"+city_information[3])
						city_deltaconfirmed_label.config(text="Confirmed today\n"+city_information[4])
						city_deltadeath_label.config(text="Deaths today\n"+city_information[5])
						city_deltarecovered_label.config(text="Recovered today\n"+city_information[6])
						
		if flag==0 :
			current_city_name_label.config(text="Incorrect city.                   ",foreground='red',background='black')	
	except KeyError :
		pass

def search_by_state() :
	st=state.get().strip()
	s=""
	try:
		for all in response['state_wise'] :
			if st.lower()==all.lower() :
				s=all
				break
		resp=response['state_wise'][s]
		lastUpdatedTime=resp['lastupdatedtime']
		active=resp['active']
		confirmed=resp['confirmed']
		deaths=resp['deaths']
		recovered=resp['recovered']
		confirmed_today=resp['deltaconfirmed']
		death_today=resp['deltadeaths']
		recovered_today=resp['deltarecovered']
		state_name_label.config(text=st.title())
		current_state_name_label.config(text="                                  ")
		lastUpdatedTime_label.config(text="Last update on : "+lastUpdatedTime)
		state_active_label.config(text="Active\n"+active)
		state_confirmed_label.config(text="Confirmed\n"+confirmed)
		state_death_label.config(text="Deaths\n"+deaths)
		state_recovered_label.config(text="Recovered\n"+recovered)
		state_deltaconfirmed_label.config(text="Confirmed today\n"+confirmed_today)
		state_deltadeath_label.config(text="Deaths today\n"+death_today)
		state_deltarecovered_label.config(text="Recovered today\n"+recovered_today)
	except KeyError :
		current_state_name_label.config(text="Incorrect state.                   ",foreground="red")
		pass

def getDetails() :
	lst=[]
	url="https://www.mohfw.gov.in/"
	htmlData=getDataFromURL(url)
	bs=bs4.BeautifulSoup(htmlData.text,'html.parser')
	infoRow = bs.find("div", class_= "col-xs-8 site-stats-count")
	active=infoRow.find("li","bg-blue").get_text()
	ActiveArray=active.split()
	Active=ActiveArray[0]
	ActiveTotal=ActiveArray[1]
	ActiveRaised=ActiveArray[2]
	lst.append(ActiveTotal)
	lst.append(ActiveRaised)
	discharged=infoRow.find("li","bg-green").get_text()
	dischargeArray=discharged.split()
	Discharged=dischargeArray[0]
	DischargedTotal=dischargeArray[1]
	DischargedRaised=dischargeArray[2]
	lst.append(DischargedTotal)
	lst.append(DischargedRaised)
	death = infoRow.find("li", "bg-red").get_text()
	deathArray = death.split()
	Death = deathArray[0]
	DeathTotal = deathArray[1]
	DeathRaised = deathArray[2]
	lst.append(DeathTotal)
	lst.append(DeathRaised)
	totalVaccinationArray=bs.find("div","fullbol").get_text().split()
	totalVaccination=totalVaccinationArray[0]+(" "+totalVaccinationArray[1])
	covidData=totalVaccinationArray[3]
	vaccinedToday=totalVaccinationArray[4]
	lst.append(covidData)
	lst.append(vaccinedToday)
	full_details=Active + " = " + ActiveTotal+", Raised = "+ActiveRaised+"\n"+Discharged + " = "+DischargedTotal+", Raised = "+DischargedRaised+"\n"+Death + " = " + DeathTotal + ", Raised = " + DeathRaised+"\n"+totalVaccination+" = "+covidData+" applied today = "+vaccinedToday+")\n"
	return lst

#  -------------------------FRONTEND----------------------------------------------
def refresh() :
	print("Refreshing..")
	state.set(default_state)
	city.set(default_city)
	newData=getDetails()
	search_by_state()
	search_by_city()
	current_city_name_label.config(text="Current internet location (city).",foreground='Rosybrown1')
	current_state_name_label.config(text="Current internet location (state).",foreground='white')
# Notification STARTS
def notify_me() :
	while True :
		c=city.get()
		plyer.notification.notify(title="Today's COVID 19 cases in "+c,message="Confirmed : "+str(city_information[4])+", Deaths :"+str(city_information[5])+", Recovered : "+str(city_information[6]),timeout=10,app_icon='covid.ico')
		time.sleep(10800)

#Notification ENDS

# window starts

root=tk.Tk()
root.geometry("700x700")
root.iconbitmap("covid.ico")
root.title("COVID19 TRACKER")
root.configure(background="black")

# Title Frame starts
titleFrame=tk.Frame(root,background="black")
covid_19=tk.Label(titleFrame,text="COVID-19",background="black",foreground="red",font=("comicsansms",20,"bold")).grid(row=0,column=0)
data_tracker=tk.Label(titleFrame,text=" Data tracker",background="black",foreground="white",font=("comicsansms",20,"bold")).grid(row=0,column=1)
titleFrame.pack(fill="x",padx="190",pady="10")
#Title frame ends


# Main image label starts
mainImage=tk.PhotoImage(file="covid-19.png")
mainImageLabel=tk.Label(root,image=mainImage)
mainImageLabel.pack()
# Main image label ends


# India's Frame starts
india_details_frame=tk.Frame(root,background="black")
# India's Frame ends

# India_detail Font works starts
lst=getDetails()

India=tk.Label(india_details_frame,text="India",background="black",foreground="peach puff",font=("Ariel", 22,"bold")).grid(row=0,column=0)
Active_Label=tk.Label(india_details_frame,text="Active",background="black",foreground="blue2",font="poppins 15 bold").grid(row=1,column=0)
Active_Details=tk.Label(india_details_frame,text="Total : "+lst[0]+"\nraised : "+lst[1],background="black",foreground="sky blue",font="poppins 10 italic").grid(row=2,column=0)

Discharged_Label=tk.Label(india_details_frame,text="Discharged",background="black",foreground="lime green",font="poppins 15 bold").grid(row=1,column=1)
Discharged_Details=tk.Label(india_details_frame,text="Total : "+lst[2]+"\nraised : "+lst[3],background="black",foreground="lawn green",font="poppins 10 italic").grid(row=2,column=1)

Death_Label=tk.Label(india_details_frame,text="Deaths",background="black",foreground="red3",font="poppins 15 bold").grid(row=1,column=2)
Discharged_Details=tk.Label(india_details_frame,text="Total : "+lst[4]+"\nraised : "+lst[5],background="black",foreground="firebrick1",font="poppins 10 italic").grid(row=2,column=2)

total_vacc_label=tk.Label(india_details_frame,text="Total Vaccination",background="black",foreground="dodger blue",font="poppins 15 bold").grid(row=1,column=3)
vacc_details=tk.Label(india_details_frame,text="Total : "+lst[6]+"\ntoday : "+lst[7],background="black",foreground="sky blue",font="poppins 10 italic").grid(row=2,column=3)

india_details_frame.pack()
# India_detail Font works ends

# current location starts
city=tk.StringVar()
state=tk.StringVar()
internet_location=getInternetLocation().split(',')
default_city=internet_location[0].strip().title()
default_state=internet_location[1].strip().title()
defaultCityInformation(default_state,default_city)
# current location ends

pic=tk.PhotoImage(file="locBtn.png")
# State frame starts 
state_frame = tk.Frame(root,background="black")
state_entry_frame=tk.Frame(state_frame,background='black')
state_entry_label=tk.Label(state_entry_frame,background="black")
state_entry_label.place(relx='0.0',rely='0.0')

# state entry box starts
state_entry_box = tk.Entry(state_entry_label,textvariable=state,background="gray10",foreground="white",font=("poppins",15,"italic"))
state_entry_box.insert(0,default_state)
state_entry_box.pack(pady='10',side='left')
# state entry box ends

# state enter button starts
pic=tk.PhotoImage(file="locBtn.png")
state_enter_button=tk.Button(state_entry_label,background='black',image=pic,height=22,width=22,command=search_by_state)
state_enter_button.pack(padx=5,side='left')
state_entry_label.pack(side='left')
# state enter button ends
state_entry_frame.pack()
current_state_name_label=tk.Label(state_entry_label,text="Current internet location (state).",background="black",foreground="Rosybrown1",font=("Lucida Console",10,'italic'))
current_state_name_label.pack(side='left')

#state information starts
state_name_frame=tk.Frame(state_frame,background="black")
state_info_frame=tk.Frame(state_frame,background="black")
state_name_label = tk.Label(state_name_frame,text=default_state,background="black",foreground="salmon1",font=("poppins",18,"italic"))
lastUpdatedTime_label=tk.Label(state_name_frame,text="last updated on : "+response['state_wise'][default_state]['lastupdatedtime'],background="black",foreground="cyan",font="poppins 10 italic")
state_active_label=tk.Label(state_info_frame,text="Active\n"+response['state_wise'][default_state]['active'],background="black",height=2,width=10,foreground="blue",font="poppins 10 bold")
state_confirmed_label=tk.Label(state_info_frame,text="Confirmed\n"+response['state_wise'][default_state]['confirmed'],background="black",height=2,width=10,foreground="gold",font="poppins 10 bold")
state_death_label=tk.Label(state_info_frame,text="Death\n"+response['state_wise'][default_state]['deaths'],background="black",height=2,width=10,foreground="orange red",font="poppins 10 bold")
state_recovered_label=tk.Label(state_info_frame,text="Recovered\n"+response['state_wise'][default_state]['recovered'],background="black",height=2,width=10,foreground="Lime green",font="poppins 10 bold")
state_deltaconfirmed_label=tk.Label(state_info_frame,text="Confirmed Today\n"+response['state_wise'][default_state]['deltaconfirmed'],background="black",height=2,width=14,foreground="blue",font="poppins 10 bold")
state_deltadeath_label=tk.Label(state_info_frame,text="Death today\n"+response['state_wise'][default_state]['deltadeaths'],background="black",height=2,width=10,foreground="red",font="poppins 10 bold")
state_deltarecovered_label=tk.Label(state_info_frame,text="Recovered today\n"+response['state_wise'][default_state]['deltarecovered'],background="black",height=2,width=15,foreground="green yellow",font="poppins 10 bold")


state_name_label.pack(side='left')
lastUpdatedTime_label.pack(side='left',padx='5')
state_active_label.pack(side='left')
state_confirmed_label.pack(side='left')
state_death_label.pack(side='left')
state_recovered_label.pack(side='left')
state_death_label.pack(side='left')
state_deltadeath_label.pack(side='left')
state_deltaconfirmed_label.pack(side='left')
state_deltarecovered_label.pack(padx='2',side='left')
state_name_frame.pack(anchor='nw')
state_info_frame.pack(side='left')
#state information ends

state_frame.pack()
# State frame ends 

# City frame start
city_frame = tk.Frame(root,background="black")
city_entry_frame=tk.Frame(city_frame,background='black')
city_entry_label=tk.Label(city_entry_frame,background="black")

# city entry box starts
city_entry_box = tk.Entry(city_entry_label,textvariable=city,background="gray10",foreground="white",font=("poppins",15,"italic"))
city_entry_box.insert(0,default_city)
city_entry_label.place(relx='0.0',rely='0.1',anchor='nw')
city_entry_box.pack(pady='10',side='left')
# city entry box ends

# city enter button starts
city_enter_button=tk.Button(city_entry_label,background='black',image=pic,height=22,width=22,command=search_by_city)
city_enter_button.pack(padx=5,side='left')
city_entry_label.pack(side='left')
# city enter button ends

city_entry_frame.pack()
current_city_name_label=tk.Label(city_entry_label,text="Current internet location (city).",background="black",foreground="Rosybrown1",font=("Lucida Console",10,'italic'))
current_city_name_label.pack(side='left')

#city information starts
city_name_frame=tk.Frame(city_frame,background="black")
city_info_frame=tk.Frame(city_frame,background="black")
city_name_label = tk.Label(city_name_frame,text=default_city,background="black",foreground="salmon1",font=("poppins",18,"italic"))
city_active_label=tk.Label(city_info_frame,text="Active\n"+city_information[0],background="black",height=2,width=10,foreground="blue",font="poppins 10 bold")
city_confirmed_label=tk.Label(city_info_frame,text="Confirmed\n"+city_information[1],background="black",height=2,width=10,foreground="gold",font="poppins 10 bold")
city_death_label=tk.Label(city_info_frame,text="Death\n"+city_information[2],background="black",height=2,width=10,foreground="orange red",font="poppins 10 bold")
city_recovered_label=tk.Label(city_info_frame,text="Recovered\n"+city_information[3],background="black",height=2,width=10,foreground="Lime green",font="poppins 10 bold")
city_deltaconfirmed_label=tk.Label(city_info_frame,text="Confirmed Today\n"+city_information[4],background="black",height=2,width=14,foreground="blue",font="poppins 10 bold")
city_deltadeath_label=tk.Label(city_info_frame,text="Death today\n"+city_information[5],background="black",height=2,width=10,foreground="red",font="poppins 10 bold")
city_deltarecovered_label=tk.Label(city_info_frame,text="Recovered today\n"+city_information[6],background="black",height=2,width=15,foreground="green yellow",font="poppins 10 bold")


city_name_label.pack(side='left')
lastUpdatedTime_label.pack(side='left',padx='5')
city_active_label.pack(side='left')
city_confirmed_label.pack(side='left')
city_death_label.pack(side='left')
city_recovered_label.pack(side='left')
city_death_label.pack(side='left')
city_deltadeath_label.pack(side='left')
city_deltaconfirmed_label.pack(side='left')
city_deltarecovered_label.pack(padx='2',side='left')
city_name_frame.pack(anchor='nw')
city_info_frame.pack(side='left')
#city information ends
city_frame.pack()
# City frame ends


# copy right frame starts
copyright_frame=tk.Frame(root,background="black")
copyright_label=tk.Label(copyright_frame,text=u"\u00A9"+" created by Satyendra Singh (2021)",background="black",foreground="white")
copyright_label.pack()
copyright_frame.pack(side='bottom',anchor='s')
# copy right frame ends


f=("poppins",12,"bold")
refreshButton=tk.Button(root,text="REFRESH",font=f,relief='solid',command=refresh)
refreshButton.pack(pady='20')
# Threading starts
t=threading.Thread(target=notify_me)
t.setDaemon(True)
t.start()
# Threading ends
root.maxsize(700,700)
root.minsize(700,700)

root.mainloop()
# Window Ends

#    ------------------------------------- FRONTEND ENDS ---------------------------------------------------------
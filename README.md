# Covid-19-Data-Tracker
A live covid-19 data tracker of India including state and city along with notifications.
This app sends notification in every 3 hours.
Project Title: Live COVID-19 data tracker

# Problem : 
Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus. 
In this project, we dived deep into ‘What does data say about Covid-19 situation in India?’. In addition, with available data, we came up with some observations and conclusions. 
This analysis mainly focuses on: 
✔What is the current COVID-19 situation in India.
✔State-wise comparison.

# Why is this particular topic chosen?
As COVID-19 continues to take human lives and jolt the global economy, governments are urgently seeking innovative new tools to inform policy and tackle the crisis. Digital solutions based on geolocation data are emerging to help authorities monitor and contain the spread of the virus. Mobile call data records (CDRs), i.e. data produced by telecommunication service providers on telephone calls or other telecommunications transactions, which provide valuable insights into population movements, feed some. As network operators serve substantial portions of the population across entire nations, the movements of millions of people at fine spatial and temporal scales can be measured in near real-time. The resulting information and trends are invaluable for governments seeking to track the COVID-19 outbreak, warn vulnerable communities, and understand the impact of policies such as social distancing and confinement.
									
# Objective and scope of the project:
The Covid-19 Tracker app can provide full statistics about the default place where they are living with a notification, which is used to pop-up after every 3 hours. Not only for the default location, the data can be shown for any state and any district of the state so that the user can be alert before visiting any place.
The scope of this app is only within India and its territories and to use this application, Internet is must.

# Methodology Used:
1)	First, a request is sent to the google as “show my current location”; the current location is fetched from the response.
2)	The fetched location is used as a response for an API of COVID-19 reports.
3)	The full report is fetched for the current state and the city. 
4)	The current state and city can be changed manually by the user to see the report for that location.
5)	Notification is send after every 3 hours showing the confirmed cases, deaths and recovered in parallel.
6)	Every attribute of the report is show with different color codes.
# Hardware and software to be used:
1)	Python 3.8.
2)	Tkinter package for GUI.
3)	Request and beautifoulSoup4 package for posting and getting response.
4)	COVID-19 API to fetch the report.
5)	Currently this application is only developed for the windows desktop. It can be developed for android and linux further.
6)	For the desktop requirements:  minimum 512 mb ram, Internet connection upto 100kbps minimum.

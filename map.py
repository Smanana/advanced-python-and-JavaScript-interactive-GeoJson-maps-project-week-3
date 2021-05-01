#import libraries
import folium
from folium import IFrame
import pandas
import os
import base64

#create a variable
map = folium.Map(location=[-26.20227,28.04363],zoom_start=7)

#variables that holds images and setting the width and height 
logoIcon = folium.features.CustomIcon("download.png",icon_size=(40,40))
logoIcon1 = folium.features.CustomIcon("images.png",icon_size=(40,40))
logoIcon2 = folium.features.CustomIcon("markerpen.jpg",icon_size=(40,40))
logoIcon3 = folium.features.CustomIcon("images (1).png",icon_size=(40,40))

#geojson data
coordinate= os.path.join('data','coordinate.json')

#tooltip variable
tooltip= "Click for more"

#html variable to hold and convert image
html = '<img src="data:image/png;base64,{}">'.format

#variable image1
image1 = base64.b64encode(open('./images/kimberly.png','rb').read()).decode()
Iframe1 = IFrame(html(image1), width=200+ 20, height=200+20)
popup1 =folium.Popup(Iframe1,max_width=750)
icon1 = folium.Icon(color="red")

#variable image2
image2 = base64.b64encode(open('./images/images.jpg','rb').read()).decode()
Iframe2 = IFrame(html(image2), width=200+ 20, height=200+20)
popup2 =folium.Popup(Iframe2,max_width=750)
icon2 = folium.Icon(color="black")

#variable image3
image3 = base64.b64encode(open('./images/kimberly.png','rb').read()).decode()
Iframe3 = IFrame(html(image3), width=200+ 20, height=200+20)
popup3 =folium.Popup(Iframe3,max_width=750)
icon3 = folium.Icon(color="orange")

#variable image4
image4 = base64.b64encode(open('./images/klerksdorp.png','rb').read()).decode()
Iframe4 = IFrame(html(image4), width=200+ 20, height=200+20)
popup4 =folium.Popup(Iframe4,max_width=750)
icon4 = folium.Icon(color="purple")


#variable image5
image5 = base64.b64encode(open(".\images\download.jpg",'rb').read()).decode()
Iframe5 = IFrame(html(image5), width=200+ 20, height=200+20)
popup5 =folium.Popup(Iframe5,max_width=750)
icon5 = folium.Icon(color="white")

#variable image6
image6 = base64.b64encode(open('./images/bloemfontein.png','rb').read()).decode()
Iframe6 = IFrame(html(image6), width=200+ 20, height=200+20)
popup6 =folium.Popup(Iframe6,max_width=750)
icon6 = folium.Icon(color="pink")

#variables wher the images will show
marker1 = folium.Marker([-25.37380917154398, 27.103271484375],
              popup=popup1,
                  tooltip=tooltip,
                      icon=icon1).add_to(map),
marker2 = folium.Marker([-25.492868271257112, 31.014404296875],
              popup=popup2,
                  tooltip=tooltip,
                      icon=icon2).add_to(map),

marker3 = folium.Marker([-28.73876397137028, 24.719238281249996],
              popup=popup3,
                  tooltip=tooltip,
                      icon=icon3).add_to(map),
marker4 = folium.Marker([-26.843677401113002, 26.663818359375],
              popup=popup4,
                  tooltip=tooltip,
                      icon=icon4).add_to(map),

marker5 = folium.Marker([-28.052590823339845, 26.806640624999996],
              popup=popup5,
                  tooltip=tooltip,
                      icon=icon5).add_to(map),
marker6 = folium.Marker([-29.161755515328824, 26.2353515625],
              popup=popup6,
                  tooltip=tooltip,
                      icon=icon6).add_to(map),




#create markers
folium.Marker([-25.654448,27.255854],
              popup='<strong>Location Rustenburg</strong>').add_to(map),
folium.Marker([-25.872782,29.255323],
              popup='<strong>Location Emalahleni</strong>').add_to(map)
folium.Marker([-28.741943,24.771944],
              popup='<strong>Location Kimberly</strong>').add_to(map)

#marker with a different color
folium.Marker([-29.100000, 26.216700],
              popup='<strong> Location Bloemfontein</strong>' ,
              icon=folium.Icon(color='green')).add_to(map),
folium.Marker([-33.958252, 25.619022],
              popup='<strong> Location Port Elizabeth</strong>' ,
              icon=folium.Icon(color='black')).add_to(map),
folium.Marker([-26.29999,27.9999],
              popup='<strong> Location Johannesburg</strong>' ,
              icon=folium.Icon(color='red')).add_to(map),
folium.Marker([-33.977074, 22.457581],
              popup='<strong> Location Cape Town</strong>' ,
              icon=folium.Icon(color='purple')).add_to(map),

#marker with a different image
folium.Marker([-26.859823,26.631750],
              popup='<strong>Location Klerksdorp</strong>',
              icon=logoIcon).add_to(map),
folium.Marker([-30.845867,30.372374],
              popup='<strong>Location Margate</strong>',
              icon=logoIcon1).add_to(map),
folium.Marker([-33.844166,18.698610],
              popup='<strong>Location Cape Town</strong>',
              icon=logoIcon2).add_to(map),
folium.Marker([-25.853161,25.640181],
              popup='<strong>Location Mahikeng</strong>',
              icon=logoIcon3).add_to(map)

#creating circular marker
folium.CircleMarker(location=[-25.4610,30.9290],
                    radius=30,
                    color='#B0E0E6',
                    fill=True,
                    fill_color='#B0E0E6').add_to(map)
              
folium.CircleMarker(location=[-29.883333,31.049999],
                    radius=30,
                    color='#FF69B4',
                    fill=True,
                    fill_color='#FF69B4').add_to(map)
folium.CircleMarker(location=[-28.0045655,26.7732162],
                    radius=30,
                    color='#EE82EE',
                    fill=True,
                    fill_color='#EE82EE').add_to(map)

folium.GeoJson(coordinate, name='area').add_to(map)
#saving the file as an HTML file
map.save('map.html')

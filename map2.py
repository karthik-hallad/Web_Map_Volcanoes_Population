import folium
import pandas

#reading the csv file
data=pandas.read_csv("PYTHON\Web Map\Volcanoes.txt")

#converting the lat and long series structure into a list
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])

def colorproducer(el):
    if el <1000:
        return 'green'
    elif 1000 <= el <2000:
        return 'darkgreen'
    elif 2000<=el <3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el) +" m",icon=folium.Icon(color=colorproducer(el))))
#for large strings with ' use folium.Popup(str(el),parse_html=True)

map.add_child(fg)
map.save('Map2.html')
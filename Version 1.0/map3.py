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
fgv=folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el) +" m",
    fill_color=colorproducer(el),color='grey',fill_opacity=.7))
#color refers to cg color and fill_color refers to the color to be filled inside
#for large strings with ' use folium.Popup(str(el),parse_html=True)


fgp=folium.FeatureGroup(name="Population")
#here x already is a elemnt inside  the data so no need to say features
fgp.add_child(folium.GeoJson(data=open("PYTHON\Web Map\world.json",'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 
else 'blue' if 10000000<=x['properties']['POP2005'] <20000000 
else 'violet' if 20000000<=x['properties']['POP2005'] <35000000
else 'orange' if 35000000<=x['properties']['POP2005']<50000000 
else 'red'  }))


map.add_child(fgv)
map.add_child(fgp)
#add layer acontrol afeter adding feature group
map.add_child(folium.LayerControl())
map.save('Map3.html')
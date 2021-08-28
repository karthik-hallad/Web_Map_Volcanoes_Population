import folium

#intitializing the map
map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
#feature group is a grp like list which can be used to add mul child at once
fg=folium.FeatureGroup(name='My Map')

# fg.add_child(folium.Marker(location=[37.2,-99.1],popup="Hi I am a Marker",icon=folium.Icon(color='green')))
# map.add_child(fg)
#instead using for loop for adding child

#adding the coordinates to the feature group
for coordinates in [ [38.58,-99.09] ,[38.2,-99.1]]:
    fg.add_child(folium.Marker(location=coordinates,popup="Hi I am a Marker",icon=folium.Icon(color='green')))

#adding the collection of child to map and then saving
map.add_child(fg)
map.save("Map1.html")
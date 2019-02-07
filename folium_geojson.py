import folium,json

def embed_map(m):
	'''This is a workaround for a bug that happens in Chrome/jupyter with complex geojsons'''
	from IPython.display import IFrame
	m.save('removeIT.html')
	return IFrame('removeIT.html', width='100%', height='750px')

f = 'FILENAME.geojson'
m = folium.Map( location=[6,12], tiles='Mapbox Bright', zoom_start=5)
folium.GeoJson( json.load(open(f,'r'))).add_to(m)
folium.LayerControl().add_to(m)
embed_map(m)

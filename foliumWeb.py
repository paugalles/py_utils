import folium
import pandas

#https://pythonhow.com/web-mapping-with-python-and-folium/
#python -m http.server 7788

df=pandas.read_csv("Volcanoes_USA.txt")

map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Mapbox bright')

def color(elev):
    minimum=int(min(df['ELEV']))
    step=int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elev in range(minimum,minimum+step):
        col='green'
    elif elev in range(minimum+step,minimum+step*2):
        col='orange'
    else:
        col='red'
    return col

fg=folium.FeatureGroup(name="Volcano Locations")

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
        fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(name)),icon=folium.Icon(color=color(elev),icon_color='green')))

map.add_child(fg)
map.add_child(folium.GeoJson(data=open('world_geojson_from_ogr.json'),name="Population",style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(folium.GeoJson(data=open("MERGED.json", 'r', encoding='utf-8-sig').read(),name="MERGEDfinal",style_function=lambda x:{'fillColor': 'blue'}))
map.add_child(folium.LayerControl())
map.save(outfile='map.html')


myencodings = ['ascii','big5','big5hkscs','cp037','cp424','cp437','cp500','cp737','cp775','cp850','cp852','cp855','cp856','cp857','cp860','cp861','cp862','cp863','cp864','cp865','cp866','cp869','cp874','cp875','cp932','cp949','cp950','cp1006','cp1026','cp1140','cp1250','cp1251','cp1252','cp1253','cp1254','cp1255','cp1256','cp1257','cp1258','euc_jp','euc_jis_2004','euc_jisx0213','euc_kr','gb2312','gbk','gb18030','hz','iso2022_jp','iso2022_jp_1','iso2022_jp_2','iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext','iso2022_kr','latin_1','iso8859_2','iso8859_3','iso8859_4','iso8859_5','iso8859_6','iso8859_7','iso8859_8','iso8859_9','iso8859_10','iso8859_13','iso8859_14','iso8859_15','johab','koi8_r','koi8_u','mac_cyrillic','mac_greek','mac_iceland','mac_latin2','mac_roman','mac_turkish','ptcp154','shift_jis','shift_jis_2004','shift_jisx0213','utf_16','utf_16_be','utf_16_le','utf_7','utf_8']

for enco in myencodings:
    try:
        map.add_child(folium.GeoJson(data=open('MERGED.json',encoding=enco),name="MERGEDfinal",style_function=lambda x:{'fillColor': 'blue'}))
        print(enco+r' >> GOOOD')
    except:
        print(enco+r' >> FAILED')

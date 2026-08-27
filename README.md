V eksperimentu-projektu sem se odločil, da bom skušal izboljšati svojo vizualizacijo LiDAR posnetka za arheološke interpretacije. Vsi rezultati in metode bodo objavljeni tu, v tem GitHubovem reprozitoriju. 
LiDAR podatke sem pridobil iz dveh platform: 

              - Atlas LiDAR (https://gis.arso.gov.si/evode/profile.aspx?id=atlas_voda_Lidar@Arso ) 
              - CLSS (https://clss.si/).

Pri obdelavi teh podatkov sem primarno uporabljal Python, pri čemer je bilo uporabljenih več knjižnic:

              - PDAL
              - JSON
              - Rasterio
              - Numpy
              - scipy.ndimage

Kodo programa prav tako lahko vidite na temu reprozitoriju, in sicer:

              - PDAL (začetek za obdelovanje točk, zbiranje klasifikacij...)
              - Kernel in mediana filter (izboljšanje vizualizacij)

Da bi bil poskus primerljiv in ponovljiv, sem se odločil, da bom sproti opazoval od PDAL (brez uporabe kernel-a in mediane filter) vse do kernel_size 10 in pri tem spremljal vpliv vizualizacije posnetka.
Nato sem .tif datoteko, ki se mi je naložila v datotekah, odprl v QGIS okolju, kjer sem nato uporabil slednja orodja:

              - GDAL - Fill NoData (če je potrebno)
              - Relief Visualization Toolbox (RVT)

Za samo vizualizacijo sem se odločil uporabiti Sky View Factor iz orodja RVT. 

### Natančnejši postopek uporabe Sky View Factor

## 1. korak

        Vertical exaggeration factor: 1.000
        Search radius: 10
        Number of search directions: 16
        Level noise removal: No remove
        
## 2. korak
   
        Properties
        Min/Max Values settings → cumulative count na 2.00–98.00

# Raziskovalno vprašanje: 

    Kako velikost kernel_size pri uporabi medianega filtra vpliva na interpretabilnost LiDAR rastra za arheološko vizualizacijo reliefa?

# Hipoteza

    Učinek median filtra na interpretabilnost LiDAR rastra je odvisen od velikosti uporabljenega kernel_size in prostorske velikosti rastra. Pri večjih vrednostih kernel_size se pričakuje večja stopnja glajenja rastra, zaradi česar se lahko manjše reliefne strukture izgubijo ali popačijo (onemogočeno arheološko interpretiranje).

V eksperimentu-projektu sem se odločil, da bom skušal izboljšati svojo vizualizacijo LiDAR posnetka za arheološke interpretacije. Vsi rezultati in metode bodo objavljeni tu, na temu GitHubu reprozitoriju. 
LiDAR podatke sem pridobil iz dve platformi: 

              - Atlas LiDAR (https://gis.arso.gov.si/evode/profile.aspx?id=atlas_voda_Lidar@Arso ) 
              - CLSS (https://clss.si/).

Pri obdelavi teh podatkov sem primarno uporabljal Python, pri čemer je bilo uporabljenih več knjižic:

              - PDAL
              - JSON
              - Rasterio
              - Numpy
              - scipy.ndimage

Kodo programa prav tako lahko vidite na temu reprozitoriju, in sicer:

              - PDAL (začetek za obdelovanje točk, zbiranje klasifikacij...)
              - Kernel in mediana filter (izboljšanje vizualizacij)

Da bi bil poskus primerljiv in ponovljiv, sem se odločil, da bom sproti opazoval od PDAL (brez uporabe kernel-a in mediane filter) vse do 10 in pri tem spremljal vpliv vizualizacije posnetka.
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

Raziskovalno vprašanje: Ali je kombinacija velikosti kernela in filtra mediane, res odvisna od velikost LiDAR posnetka?
Stransko vprašanje: Kateri vir je najboljši za uporabo interpretacije za arheologije in nasploh?

### REZULTAT UPORABE METODE - 1 
Datoteka (GK_399_75) je bila prenesena s spletne strani LiDAR Atlas. Na tej datoteki je prikazano arheološko najdišče Zagrajec – Gradišče Brith, ki je bilo naseljeno od pozne bronaste dobe vse do železne dobe (vir: https://geohub.gov.si/ghapp/giskd/).

Original brez uporabe kernel-a in mediane filter (direktno iz PDAL-a)
<figure>
  <img width="898" height="896" alt="image" src="https://github.com/user-attachments/assets/0d11d5e4-fb85-41b2-8f27-ad23f04cc2a1" />
</figure>

Kernel size - 1 
<figure>
  <img width="982" height="986" alt="image" src="https://github.com/user-attachments/assets/e61f394e-0005-4fc3-a949-f772bd9157aa" />
</figure>

Kernel size - 2
<figure>
  <img width="984" height="988" alt="image" src="https://github.com/user-attachments/assets/1667c221-7a78-475d-adb8-d0e19ea321fb" />
</figure>

Kernel size - 3
<figure>
  <img width="953" height="953" alt="image" src="https://github.com/user-attachments/assets/e53f6761-3300-47e1-a92a-9c56bb489778" />
</figure>

Kernel size - 4
<figure>
  <img width="953" height="953" alt="image" src="https://github.com/user-attachments/assets/5b929465-5f65-4cc5-a182-01a08496bfb7" />
</figure>

Kernel size - 5
<figure>
  <img width="916" height="928" alt="image" src="https://github.com/user-attachments/assets/8213241e-4715-44da-bc8a-3ed01e80e981" />
</figure>

Kernel size - 6
<figure>
  <img width="898" height="906" alt="image" src="https://github.com/user-attachments/assets/b5ba404e-e9cc-4aca-abaa-8d6fd4a28219" />
</figure>

Kernel size - 7 
<figure>
  <img width="949" height="947" alt="image" src="https://github.com/user-attachments/assets/96d6e35e-af88-4464-a9da-e10f71b28129" />
</figure>

Kernel size - 8
<figure>
  <img width="928" height="932" alt="image" src="https://github.com/user-attachments/assets/cb25383e-6b14-4101-9ca2-b5bc1c9fa3d6" />
</figure>

Kernel size - 9 
<figure>
  <img width="952" height="960" alt="image" src="https://github.com/user-attachments/assets/ca142f24-73dc-4e13-96bd-4f58c5032c91" />
</figure>

Kernel size - 10
<figure>
  <img width="955" height="979" alt="image" src="https://github.com/user-attachments/assets/02f5a323-88ec-4c98-ac4a-a7b1360f3b64" />
</figure>

import rasterio as rio
import numpy as np 
from scipy.ndimage import median_filter
import os 

"""
Kernel oziroma jedro je v kontekstu obdelave rastrskih in slikovnih podatkov
lokalno območje celic, ki ga algoritem uporablja za izračun vrednosti posameznih celic.
Velikost kernela določa, kako široko okolico posamezne celice algoritem upošteva.

Primer 3 × 3 kernela:

                [ 1 ][ 2 ][ 3 ]  ┐
                [ 4 ][ X ][ 6 ]  ┤ d
                [ 7 ][ 8 ][ 9 ]  ┘

V tem primeru imamo 3 × 3 matriko, ki vsebuje devet celic. Kernel zajema
osrednjo celico X in njenih osem sosednjih celic. Pri različnih postopkih
obdelave se vrednosti znotraj tega lokalnega območja uporabijo za izračun
oziroma določitev nove vrednosti osrednje celice.

Na desni strani matrike je s puščicami prikazana prostorska ločljivost mreže (d), ki predstavlja razdaljo med sosednjimi celicami.

Pri medianem filtru, ki ga uporabljam v tem algoritmu, se osredotočam na parameter kernel_size, ki določa velikost lokalnega okna. 
Ker se pri tem eksperimentu dela z 2D rastrskimi podatki, je kernel prav tako dvodimenzionalen.

Primeri velikosti kernela:

                          3 × 3
                          5 × 5
                          7 × 7

Vpliv velikosti kernela

- Majhni kerneli (npr. 3 × 3) obravnavajo manjše lokalno območje. Njihova
  prednost je, da bolje ohranjajo drobne strukture, vendar lahko pri tem
  odstranijo manj šuma.

- Srednje veliki kerneli (npr. 5 × 5 do 9 × 9) zajamejo širšo okolico
  posamezne celice. Zaradi tega lahko učinkoviteje zmanjšajo šum, hkrati
  pa še vedno omogočajo ohranjanje pomembnejših reliefnih struktur.

- Veliki kerneli (npr. 21 × 21 ali več) zajamejo precej širše prostorsko
  območje. Pri filtriranju lahko zato močneje zmanjšajo šum, vendar lahko
  hkrati povzročijo izgubo mikrostruktur in nekaterih reliefnih struktur.

Pri izbiri velikosti kernela je zato treba upoštevati predvsem:

    - prostorsko ločljivost rastra,
    - velikost oziroma merilo ciljnih struktur,
    - namen analize,
    - količino šuma v podatkih,
    - računsko zahtevnost.

Pomembno je, da velikost kernela vedno obravnavamo v povezavi z ločljivostjo
rastra, saj ista velikost kernela pri različnih ločljivostih pokriva različno
veliko fizično območje.

Na primer, kernel velikosti 3 × 3 pri rastru z ločljivostjo 0,5 m pokriva
območje približno 1,5 × 1,5 m oziroma 2,25 m². Pri rastru z ločljivostjo
2 m pa isti kernel pokriva območje 6 × 6 m oziroma 36 m².

Mediana filter

Mediana filter je nelinearna tehnika filtriranja, ki se pogosto uporablja
za zmanjševanje šuma v slikah in rastrskih podatkih.

Filter se pomika po rastru in za vsako osrednjo celico določi vrednosti celic
znotraj izbranega lokalnega okna. Te vrednosti razvrsti po velikosti, nato
pa vrednost osrednje celice nadomesti z njihovo mediano.

Primer delovanja medianega filtra:

1. Izbira velikosti okna

   V tem primeru uporabimo okno velikosti 3 × 3, ki je razporejeno okoli
   osrednje celice.

2. Zbiranje vrednosti celic

            [ 1 ][ 2 ][ 3 ]
            [ 4 ][ 8 ][ 6 ]
            [ 7 ][ 5 ][ 9 ]

   Osrednja celica ima vrednost 8.

3. Razvrščanje vrednosti

   Vrednosti znotraj okna razvrstimo po naraščajočem vrstnem redu:

            [1, 2, 3, 4, 5, 6, 7, 8, 9]

4. Določitev mediane

   Ker je v naboru devet vrednosti, je srednja oziroma mediana vrednost 5.

5. Zamenjava osrednje vrednosti

   Vrednost osrednje celice se spremeni iz 8 v 5.

6. Ponovitev postopka

   Postopek se ponovi za vse ostale celice rastra.

Prednost medianega filtra je, da lahko učinkovito zmanjša določene vrste
šuma, pri tem pa običajno bolje ohranja robove in izrazitejše strukture
kot nekateri linearni filtri.

V tem eksperimentu se zato preverja, kako različne vrednosti parametra
kernel_size vplivajo na kakovost končne LiDAR vizualizacije in na možnost
interpretacije arheoloških oziroma geomorfoloških struktur.
"""
#vhod datoteke (pred uporabo kernel_size)
input_path = r"\xxxx\xx.tif"

#izhod datoteke (po uporabi kernel_size)
output_path = r"C:\xxxx\xxx.tif"

#kernel_size, kjer lahko kontorlirano dodajš številko. Učinek kernel_size bo odvisno od velikosti matrike. Zato je potrebno, da sta matrika in kernel_size čim bolj skladna, saj na tak način bo tudi vizaulizacija terena omogočala boljšo interpretacijo 
#za priporočilo je najbolje uporabiti zgolj lihe velikosti
kernel_size = 5

#kratek izpis, ki pove, ali obstaja vhodna datoteka
if os.path.exists(input_path):
    print("Super je")
else:
    print("Here we go again!")


#s pomočjo knjižnice rasaterio (rio) in numpy (np) z vhodom datoteke, da v pregled celotno matriko in pretvori v array (arr)
with rio.open(input_path) as src: 
    profile = src.profile 
    arr = src.read(1).astype(np.float32)
    nodata = src.nodata
  
profile.update(dtype=rio.float32)
#Če je v array (arr) priostna [vrednost], se nato pretovri v nodata, kjer nato sprememni v matriko TRUE/FALSE (prikaz spodaj). Pri tem nodata označi TRUE povsod tam, kjer je prisotna ta vrednost.
"""
[[False, False,  True],
 [False,  True, False],
 [False, False, False]]
""" 
#Če pa nodata nima nobenih vrednost, izpiše FALSE 
"""
[[False, False,  False],
 [False,  False, False],
 [False, False, False]]
""" 
mask_nodata = (arr == nodata) if nodata is not None else np.zeros_like(arr, dtype=bool)

#filitriranje
arr_filtered = median_filter(arr, size=kernel_size)

#Podoben pristop kot prej, samo, da gre že za filtrirano območje s pomočjo kernel_size in median filter
arr_filtered[mask_nodata]= nodata if nodata is not None else arr_filtered[mask_nodata]

#izpis izhodne datoteke urejene celotne matrike s pomočjo kernel_size.
with rio.open(output_path, "w", **profile) as dst:  
    dst.write(arr_filtered, 1)

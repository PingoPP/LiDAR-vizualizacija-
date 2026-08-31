# Zaključek

Po pregledu vizualizacij in primerjav sem pri svojem raziskovalnem vprašanju prišel do začasnega sklepa.

Vizualizacija, izdelana neposredno iz surove datoteke PDAL, brez uporabljenega kernel_size in mediana filtra, je bila polna šuma, kar je močno oteževalo interpretacijo. Pri tem sem preizkusil vrednosti kernel_size med 1 in 10, nato pa še večje vrednosti (13, 15, 17 in 21), da bi ocenil njihov vpliv na celotno datoteko.

Glede na dosedanje rezultate ocenjujem, da v povprečju najboljše rezultate dosežem pri kernel_size 4 ali 5. Ta ugotovitev pa ni univerzalna, saj je optimalna vrednost odvisna od več dejavnikov, med drugim od:

    načina snemanja z LiDAR senzor,
    postopka filtriranja,
    klasifikacije,
    modeliranja,
    rasterizacije,
    izbire filtrov v PDAL-u.

Moje ugotovitve se skladajo tudi z opažanji drugih avtorjev. Hesse pojasnjuje, da kernel_size vpliva predvsem na prostorsko merilo, znotraj katerega orodje izračuna lokalno površino (raster v .tif formatu); večji kernel_size tako pomeni širše območje izračuna, kar posledično spreminja merilo reliefnih struktur, ki jih vizualizacija poudari [1]. Podobno tudi članek o srednjeveškem naselju v južni Italiji izpostavlja, da so nekateri filtri – na primer Local Relief Model (LRM) – odvisni od kernel_size, saj se statistični parametri izračunajo znotraj izbranega kernela; posledično izbira velikosti kernela pomembno vpliva na končni rezultat [2] [3].

Rezultati so pokazali, da so bile pri uporabi medianega filtra v obravnavanem primeru lihe vrednosti kernel_size nekoliko primernejše za ohranjanje oziroma izboljšanje interpretabilnosti. Pri medianem filtru se za vsako celico rastra obravnava njeno lokalno sosedstvo znotraj določenega okna. Pri večjih vrednostih kernel_size se v obdelavo vključi večje število okoliških celic, zaradi česar je učinek glajenja izrazitejši. To lahko povzroči izgubo oziroma popačenje manjših reliefnih struktur. Vendar rezultatov ni mogoče posplošiti na vse LiDAR podatke, saj je optimalna velikost kernela odvisna tudi od značilnosti vhodnega rastra in namena vizualizacije.

Median filter je znan filter, ki lahko ohrani ostrino izrazitih sprememb naklona, hkrati pa zmanjša šum oziroma zgladi DEM. Avtorji omenjajo, da ta filter nima samo pozitivnih lastnosti, saj lahko glede na velikost parametra kernel_size močno zgladi površino, kar lahko oteži oziroma privede do napačne interpretacije [3].


## Rezultat 1 
<fig>
    <img width="1642" height="1636" alt="image" src="https://github.com/user-attachments/assets/8ade887f-9c1d-4a92-9f3c-58d7101860aa" />
    <figcaption>A) Original iz PDAL (brez mediane in kernel_size); B) kernel_size = 5; C) kernel_size = 13; D) kernel_size =  21
</fig>
<br><br>
<fig>
    <img width="1300" height="1720" alt="image" src="https://github.com/user-attachments/assets/55597e50-d9d7-48f2-8cd6-482cc0f3ca68" />
    <figcaption>A) Original iz PDAL (brez mediane in kernel_size); B) kernel_size = 5; C) kernel_size = 13; D) kernel_size =  21
</fig>
<br><br>
Vključil sem tudi subjektivno oceno glede vizualizacije. Ocenjeval sem na podlagi treh kriterijev, in sicer: berljivost, vidne strukture in čistota, ter nato skupaj seštel in naredil povprečje. Na podlagi subjektivnega ocenjevanja se je izkazalo, da je bila vrednost kernel_size = 5 med testiranimi vrednostmi najbolj uspešna, medtem ko so bile pri drugih vrednostih ocene nekoliko nižje.
<br><br>
Na začetku projekta sem si zastavil raziskovalno vprašanje in sicer: Kako velikost kernel_size pri uporabi medianega filtra vpliva na interpretabilnost LiDAR rastra za arheološko vizualizacijo reliefa?
Na to vprašanje sem z vztrajnim raziskovanjem in stalnim eksperimentiranjem prišel do odgovora. Rezultati so pokazali, da je vprašanje kompleksnejše, kot je bilo sprva predvideno, saj na optimalno izbiro velikosti kernela vpliva več različnih dejavnikov.
Prav tako sem si zadal svojo hipotezo, ki pa je omogočila zgolj delni odgovor in jo je seveda potrebno preoblikovati v nekoliko bolj natančno obliko. 
<br><br>

        Predvideva se, da velikost kernel_size pri uporabi medianega filtra pomembno vpliva na interpretabilnost LiDAR rastra. Srednje velike vrednosti kernel_size naj bi zagotavljale najboljše razmerje med zmanjšanjem šuma in ohranjanjem drobnih arheološko pomembnih reliefnih struktur. Z naraščanjem velikosti kernel_size se pričakuje izrazitejše glajenje rastra, zaradi česar lahko pride do zmanjšanja, izgube ali popačenja manjših reliefnih struktur. 
        Neustrezna izbira velikosti kernel_size lahko zato vodi do napačne arheološke interpretacije.
        
<br><br>
Ob tem bi bilo zanimivo, da bi namesto medianega filtra zamenjal v Lee filter, ki ga omenjajo avtorji v članku [2], ter med njima naredil primerjavo. 
Namreč Lee filter zmanjša šum, hkrati pa poskuša ohraniti robove in lokalne strukture. Ta eksperiment nameravam izvesti v prihodnje.  

Prav tako bi bilo smisleno preveriti tudi, ali je optimalna velikost kernel_size povezana s prostorsko velikostjo vhodnega LiDAR območja.
<br><br>
# Literatura
[1] Hesse, R. 2010 LiDAR - derived LRM - a new tool for archaeological prospection. - vol. 17, issue 2, Archaeological prospection.<br><br>
[2] Massini et al. 2018 Medieval Archaeology Under the Canopy with LiDAR. The (Re)Discovery of a Medieval Forified Settlement in Southern Italy. - 10, 1598, MDPI Remote Sensing.  
[3] Lindsay, B. J. et al. 2019 LiDAR DEM Smoothing and the Preservation of Drainage Features. - 11, 1926, MDPI Remote Sensing. 

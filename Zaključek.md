Začasni zaključek

Po pregledu vizualizacij in primerjav sem pri svojem raziskovalnem vprašanju prišel do začasnega sklepa.

Vizualizacija, izdelana neposredno iz surove datoteke PDAL, brez uporabljenega kernel_size in mediana filtra, je bila polna šuma, kar je močno oteževalo interpretacijo. Po vključitvi kernel_size in mediana filtra se je čitljivost reliefnih struktur bistveno izboljšala. Pri tem sem preizkusil vrednosti kernel_size med 1 in 10; zanimivo bi bilo v nadaljevanju preveriti tudi večje vrednosti (15, 20, 25) in oceniti, kako te vplivajo na celotno datoteko.

Glede na dosedanje rezultate ocenjujem, da v povprečju najboljše rezultate dosežem pri kernel_size 4 ali 5. Ta ugotovitev pa ni univerzalna, saj je optimalna vrednost odvisna od več dejavnikov, med drugim od:

    načina snemanja z LiDAR kamero,
    postopka filtriranja,
    klasifikacije,
    modeliranja,
    rasterizacije,
    izbire filtrov v PDAL-u.

Moje ugotovitve se skladajo tudi z opažanji drugih avtorjev. Hesse pojasnjuje, da kernel_size vpliva predvsem na prostorsko merilo, znotraj katerega orodje izračuna lokalno površino (raster v .tif formatu); večji kernel_size tako pomeni širše območje izračuna, kar posledično spreminja merilo reliefnih struktur, ki jih vizualizacija poudari [1]. Podobno tudi članek o srednjeveškem naselju v južni Italiji izpostavlja, da so nekateri filtri – na primer Local Relief Model (LRM) – odvisni od kernel_size, saj se statistični parametri izračunajo znotraj izbranega kernela; posledično izbira velikosti kernela pomembno vpliva na končni rezultat [2].


Te ugotovitve nakazujejo, da manjši kernel_size bolje ohranja podrobnosti drobnejših arheoloških struktur, medtem ko bi večje vrednosti verjetno poudarile širše, obsežnejše reliefne oblike, ki pa lahko delno ali povsem zabrišejo arheoloških sledi. 
Prav tako je bilo na podlagi rezultatov ugotovljeno, da je učinek median filtra izrazitejši pri uporabi lihe vrednosti parametra kernel_size. To je mogoče pojasniti z načinom delovanja median filtra, pri katerem se za vsako celico rastra obravnava njeno lokalno sosedstvo znotraj določenega okna. Pri lihem kernel_size ima tako okno jasno določeno osrednjo celico, kar omogoča določitev mediane iz lihega števila vrednosti. Pri večjih vrednostih kernel_size se v obdelavo vključi večje število okoliških celic, zaradi česar je učinek glajenja izrazitejši in lahko pride do izgube oziroma popačenja manjših reliefnih struktur.





Ob tem bi bilo zanimivo, da bi namesto mediana filtra zamenjal v Lee filter, ki ga omenjajo avtorji v članku [2], ter med njima naredil primerjavo. 
Namreč Lee filter zmanjša šum, hkrati pa poskuša ohraniti robove in lokalne strukture. Eksperiment bom izvedel v bodoče in naredil primerjavo med mediano filter ter Lee filter. 


# Literatura
[1] Hesse, R. 2010 LiDAR - derived LRM - a new tool for archaeological prospection. - vol. 17, issue 2, Archaeological prospection.<br><br>
[2] Massini et al. 2018 Medieval Archaeology Under the Canopy with LiDAR. The (Re)Discovery of a Medieval Forified Settlement in Southern Italy. - 10, 1598, MDPI Remote Sensing.  

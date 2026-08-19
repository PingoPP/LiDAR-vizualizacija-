import pdal 
import json as json_module
"""
PDAL je kratica za besedno zvezo Point Data Abstraction Library, kar gre za odprtokodno knjižnico. Knjižnica je namenjena filtriranju, manipuliranju in procesiranju 3D oblakov točk (point cloud) in LiDAR podatkov.
Uporablja se lahko na več načinov in sicer: command-line orodje ali preko programskih okolij (python).
Sam PDAL deluje v osnovi na principu PIPELINE-a, ki predstavlja zaporedje korakov, skozi katere gredo podatki od input-a (vhoda) vse do output-a (izhoda).

                    "READERS"
                    načeloma se bere vhoda v .laz datoteki
                    "FILTER(S)"
                    obdelujejo, čisitijo, klasificirajo oblakovne točke
                    "WRITERS"
                    izpis rezultata obdelave v laz. datoteki ali tiff.datoteki
"""


pipeline_json = {
    "pipeline": [
        #ker sem naložil iz CLSS 10 laz ploščic, ki jih je potrebno združiti uporabil filters.merge.
        #Za vsako združitev sem še prej dal programu dati funkcijo vhod datoteke, ki so pa označene pod tagX 
        {
            "type": "readers.las",
            "filename": r"C:\Users\jakad\Downloads\GKOT_463_91.laz",
            "tag": "file1"
        },
        {
            "type": "readers.las",
            "filename": r"C:\Users\jakad\Downloads\GKOT_462_91.laz",
            "tag": "file2"     
        },
        {
            "type": "readers.las",
            "filename": r"C:\Users\jakad\Downloads\GKOT_462_90.laz",
            "tag": "file3"
        },
        {
            "type": "readers.las",
            "filename": r"C:\Users\jakad\Downloads\GKOT_463_90.laz",
            "tag": "file4"        
        },
        {
             "type": "readers.las",
             "filename": r"C:\Users\jakad\Downloads\GKOT_463_88.laz",
             "tag": "file5"
        },  
        {
            "type": "readers.las",
            "filename": r"C:\Users\jakad\Downloads\GKOT_464_88.laz",
            "tag": "file6"
        },
        {
            "type": "readers.las",
            "filename": r"C:\Users\jakad\Downloads\GKOT_462_88.laz",
            "tag": "file7"
        },
        {
            "type": "readers.las",
            "filename": r"C:\Users\jakad\Downloads\GKOT_462_89.laz",
            "tag": "file8"
        },
        {
            "type": "readers.las",
            "filename": r"C:\Users\jakad\Downloads\GKOT_463_89.laz",
            "tag": "file9"
        },
        {
            "type": "readers.las",
            "filename": r"C:\Users\jakad\Downloads\GKOT_464_89.laz",
            "tag": "file10"
        },
        {
            "type": "filters.merge",
            "inputs": ["file1","file2","file3","file4","file5","file6","file7","file8","file9","file10"],
            "tag":"merged"
        },
        # funkcija filters.elm je, da poskuša odstraniti low noise (nizke šume), ki so prisotni v LAZ datoteki.
        {
            "type": "filters.elm", 
            "cell": 10.0,       # "cell" določa velikost celice, v kateri filter išče lokalne minimume.
            "threshold": 0.5    # "threshold" določa toleranco za prepoznavanje nizkih odstopajočih točk.

        }, 
        # filters.outlier pri metodi "radius" preverja, koliko sosednjih točk se nahaja
        # znotraj določenega radija. "min_k" določa minimalno število sosednjih točk,
        # ki jih mora imeti točka znotraj tega radija, da se ne obravnava kot outlier.
        """
        primer:         
         •
       
       
                    X
       
        •   •
        """
        # Če ima točka X znotraj radija 1 m samo 3 sosede, pri min_k = 4 ne izpolnjuje
        # pogoja in se odstrani kot outlier. Če ima 4 ali več sosednjih točk, se ohrani.
        {
            "type": "filters.outlier",
            "method": "radius",
            "radius": 1,
            "min_k": 4,
        },
        #SMRF (Simple Morphological Filter) je namenjen predvsem ločevanju ground in non-ground točk
        {
            "window": 12,      # velikost morfološkega okna, ki ga filter uporablja pri analizi lokalne površine
            "slope": 0.2,      # dovoljena lokalna strmina terena - višja vrednost omogoča večje spremembe reliefa
            "scalar": 0.3,     # faktor, ki vpliva na določanje dovoljenega višinskega odklona glede na velikost okna
            "returns": "last", # upoštevajo se samo zadnji odboji laserskega impulza; ti so pogosto povezani s tlemi,
                               # vendar sami po sebi še niso nujno klasificirani kot ground
            "cell": 0.5,       # velikost celice za rasterizacijo
            "threshold": 0.3,  # višinski prag 
        },
        # funkcija tega filtra je ohraniti samo izbrane klasifikacije.
        # V tem primeru se ohranita ground [2:2] in building [6:6],
        # vse ostale klasifikacije pa se odstranijo.        
        { 
            "type": "filters.range", 
            "limits": "Classification[2:2], Classification[6:6]"
        },
        #output oz. shranjevanje filtriran in združen laz datoteka.
        {
            "type": "writers.las",
            "filename": r"C:\Users\jakad\Downloads\radius_merged.laz",
            "forward": "all",
            "minor_version": "4",
            "dataformat_id": "8"
        },
        {
            "type": "writers.gdal",
            "filename": r"C:\Users\jakad\Downloads\radius_merged.tif",
            "resolution": 0.5,
            "output_type": "idw",
            "gdaldriver": "GTiff",
            "nodata": -9999,
            "window_size": 6
        }
    ]
}

#run
pipeline = pdal.Pipeline(json_module.dumps(pipeline_json))

#število točk
try:
    count = pipeline.execute()
    print(f"{count} število točk ")
except Exception as e:
    print(f"ERROR: {e}")

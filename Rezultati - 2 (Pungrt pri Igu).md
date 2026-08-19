### REZULTATI UPORABE METODE - 2
V naslednji fazi sem se odločil, da bom isto tehniko uporabil na večji datoteki (10 ploščic iz vira: https://clss.si/) GKOT_463_91, GKOT_462_91, GKOT_462_90, GKOT_463_90, GKOT_464_89, GKOT_464_88, GKOT_462_89, GKOT_463_89, GKOT_463_88, GKOT_462_88 (vse skupaj: 2,45 GB). Izbrano območje je Pungrt pri Igu, kjer so vidne sledi arheoloških ostankov.

Najbolj izstopajoče obdobje je v času starejše železne dobe (8.–4. st. pr. n. št.), kjer so bili odkriti sledi prvo starejšoželeznodobno urbano gradišče v Sloveniji (Vojaković et al. 2024, 17–19).

Po izvajanju algoritmov PDAL–a in kernel ter mediane filter je skupna datoteka zmanjšala na

        •	LAZ: 995 MB
        •	TIF: 366 MB
        
Glede števila točk, ki jih je bilo posnetih je bila precejšna številka in sicer;
Vse točke (vključno vegetacijo…): 
        
        215.475.538 (prib. 24.3 pt/m na kvadrat)
Samo ground in building: 
        
        105.182.285, kjer 94% od celotnih točk predstavlja ground (prib. 11.8 pt/m na kvadrat).

Časa delovanja PDAL-a je znašal 139 minut in 59 sekund. 

Original brez uporabe kernel-a in mediane filter (direktno iz PDAL-a)
<fig>
<img width="999" height="1329" alt="image" src="https://github.com/user-attachments/assets/b8e60843-3484-498d-96b7-33c4b121e2da" />
</fig>
<fig>
<img width="983" height="968" alt="image" src="https://github.com/user-attachments/assets/0e7e78a6-ce50-407b-8301-d0558937171b" />
</fig>
<fig>
<img width="971" height="654" alt="image" src="https://github.com/user-attachments/assets/97de8861-00a9-4ffe-95a9-c64e6c859a69" />
</fig>
Kernel size - 1 
<fig>
<img width="979" height="1297" alt="image" src="https://github.com/user-attachments/assets/86f59ae0-393d-4b34-8303-bf546ca22e80" />
</fig>
<fig>
<img width="1021" height="980" alt="image" src="https://github.com/user-attachments/assets/77522211-754e-49e5-a8e9-7976faab732c" />
</fig>
<fig>
<img width="1030" height="693" alt="image" src="https://github.com/user-attachments/assets/d65d8d4d-b4a1-4fe2-b001-847f2ec08fdd" />
</fig>
Kernel size - 2
<fig>
<img width="1021" height="1354" alt="image" src="https://github.com/user-attachments/assets/b46f8dba-0b56-4862-862c-499488817b12" />
</fig>
<fig>
<img width="1015" height="993" alt="image" src="https://github.com/user-attachments/assets/4abe7ae1-912c-4948-8232-d8ae44cd4994" />
</fig>
<fig>
<img width="961" height="646" alt="image" src="https://github.com/user-attachments/assets/aefa7a5e-e9e5-42a4-b53c-215eaf36c8a0" />
</fig>
Kernel size - 3
<fig>
<img width="1015" height="1348" alt="image" src="https://github.com/user-attachments/assets/26ad0942-8362-4fed-beb1-142296a13184" />
</fig>
<fig>
<img width="1026" height="1010" alt="image" src="https://github.com/user-attachments/assets/62cdb9b4-7c60-4085-9eb8-3cd303af406c" />
</fig>
<fig>
<img width="1009" height="687" alt="image" src="https://github.com/user-attachments/assets/da1c21de-af6e-43d1-b6b6-4eae772a2a45" />
</fig>
Kernel size - 4
<fig>
<img width="1009" height="1344" alt="image" src="https://github.com/user-attachments/assets/879ca19d-3bbb-4d01-9aed-ec9898efdd8c" />
</fig>
<fig>
<img width="1008" height="999" alt="image" src="https://github.com/user-attachments/assets/c602e221-7841-42ce-a650-e5f1d755c671" />
</fig>
<fig>
<img width="945" height="635" alt="image" src="https://github.com/user-attachments/assets/5784100b-0b1b-4d54-8d03-5cf906b8d253" />
</fig>
Kernel size - 5
<fig>
<img width="1020" height="1360" alt="image" src="https://github.com/user-attachments/assets/86a3a6e7-16d6-45c1-a51f-5788e2753a7a" />
</fig>
<fig>
<img width="984" height="970" alt="image" src="https://github.com/user-attachments/assets/b6f1f711-fdfa-4380-b6aa-faf3584eba1b" />
</fig>
<fig>
<img width="1015" height="682" alt="image" src="https://github.com/user-attachments/assets/b61541fb-1d0a-4b2c-919c-3559a82a6047" />
</fig>
Kernel size - 6
<fig>
<img width="1013" height="1348" alt="image" src="https://github.com/user-attachments/assets/7b7bc0be-46eb-4408-869f-c6f90329e8ba" />
</fig>
<fig>
<img width="1009" height="996" alt="image" src="https://github.com/user-attachments/assets/3b5d2f42-5406-4270-8f03-96a575bbd2b8" />
</fig>
<fig>
<img width="980" height="658" alt="image" src="https://github.com/user-attachments/assets/5f8a9163-1167-44c3-97db-99d8eee0a2a1" />
</fig>
Kernel size 7
<fig>
<img width="988" height="1317" alt="image" src="https://github.com/user-attachments/assets/a257e1c0-7b32-4ca2-95e2-fa109c72bee5" />
</fig>
<fig>
<img width="1012" height="992" alt="image" src="https://github.com/user-attachments/assets/68359459-5f48-48f9-a95e-dce8bb8f019d" />
</fig>
<fig>
<img width="1012" height="683" alt="image" src="https://github.com/user-attachments/assets/fbeef6f0-e0d8-45b2-ada2-dc03218be512" />
</fig>
Kernelsize 8
<fig>
<img width="1014" height="1345" alt="image" src="https://github.com/user-attachments/assets/04d4dae1-eef7-4fc4-9ccb-f74ca31ff661" />
</fig>
<fig>
<img width="1004" height="991" alt="image" src="https://github.com/user-attachments/assets/536247da-b176-4868-ad56-d929a2c795fc" />
</fig>
<fig>
<img width="985" height="666" alt="image" src="https://github.com/user-attachments/assets/9ad69a17-f989-4f50-ba00-b70ac57daa6a" />
</fig>
Kernel size 9
<fig>
<img width="989" height="1303" alt="image" src="https://github.com/user-attachments/assets/475a9458-2765-47e2-aa75-47c4f42baa92" />
</fig>
<fig>
<img width="1019" height="1000" alt="image" src="https://github.com/user-attachments/assets/cd652358-693a-4920-b5ea-70a2292d013d" />
</fig>
<fig>
<img width="982" height="662" alt="image" src="https://github.com/user-attachments/assets/e4f811ba-ed38-49ed-a575-c528462be1cd" />
</fig>
Kernel size 10
<fig>
<img width="1026" height="1370" alt="image" src="https://github.com/user-attachments/assets/e9bad123-a47d-4b8f-9076-a486ccba2046" />
</fig>
<fig>
<img width="1035" height="1002" alt="image" src="https://github.com/user-attachments/assets/8b365197-9f76-4356-803d-e8d321617746" />
</fig>
<fig>
<img width="1014" height="679" alt="image" src="https://github.com/user-attachments/assets/1c9195d1-8bee-43d1-8ad9-06f5fdc98cc4" />
</fig>

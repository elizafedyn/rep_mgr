# rep_mgr
Repozytorium zawierające detektor chmur i programy FME (pobieranie zdjęć satelitarnych, przycinanie do obszaru badawczego, wyznaczanie wskaźników teledetekcyjnych)


Opis plików:

Plik "Detekcja_chmur_Cloud_detection.py" służy do detekcji chmur na zobrazowaniach satelitarnych.
Wynikiem detektora chmur jest maska chmur i plik .TIF zawierający prawdopodobieństwo wystąpienia chmury w danym pikselu.

Plik "Pobierania_zdjec_satelitarnych_USGS.fmw" to program stworzony w FME Desktop, służący do pobierania zobrazowań satelitarnych poprzez API z zasobów USGS z misji Sentinel-2, Landsat-5, Landsat-7 i Landsat-8.
Plik "Przycinanie_do_obszaru__Obliczanie_wskaznikow.fmw" to program stworzony w FME Desktop, służący do przycinania zdjęć satelitarnych do obszarów badawczych oraz do wyznaczania wartości wskaźników NDVI, NDWI, NDII, TCW, MSI i LCI.

# Zadanie 1

Sprawdź ile pamięci (szczytowo, tj. maximum resident set size) wykorzystuje program ps -eo user,pid,comm napisany w języku C, a ile Twój skrypt uruchamiany w interpreterze Pythona (można użyć GNU Time). Jak to wygląda procentowo? Zapisz swoje notatki w oddzielnym pliku tekstowym.

Uruchamiamy polecenie:

```zsh
/usr/bin/time -v ps -eo user,pid,comm > /dev/null
```

Dostajemy:

```bash
Maximum resident set size (kbytes): 3828
```

To samo dla skryptu Pythona:

```zsh
/usr/bin/time -v ./zad1.py > /dev/null
```

Dostajemy:
``` bash
Maximum resident set size (kbytes): 8436
```

Obliczamy roznice:

```
(8436 - 3828) / 3828 * 100% = 120%
```

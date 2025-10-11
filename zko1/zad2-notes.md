# Zadanie 2

Napisz skrypt w Pythonie, który:

- tworzy na nowo plik o nazwie podanej jako argument,
co sekundę dodaje do niego nową linię, która zawiera jej numer (można liczyć od zera).
- Uruchom skrypt w jednym terminalu i go nie wyłączaj. Sprawdź, czy linie są faktycznie dopisywane.

Z drugiego terminala usuń ten nowy plik. Jak bezinwazyjnie odzyskać jego zawartość? 

## Notatki

Skrypt tworzy plik i co sekunde dopisuje kolejna linie z jej numerem.

Po usunieciu pliku za pomoca komendy ```rm numery.txt``` dane dalej są dopisywane. Plik został usunięty z systemu plików ale nadal istnieje na dysku, dopóki proces działa.

Aby odzyskać zawartość:

1. Znajdujemy PID procesu ktory powstal na wskutek uruchomienia skryptu:
```bash
ps aux | grep zad2.py
```

2. Odczytujemy PID procesu ktory nas interesuje - druga kolumna:
```bash
user 5926 0.0 0.2 19316 7896 pts/0 S+ 18:17 0:00 python3 zad2.py numery.txt
```

3. Nastepnie sprawdzamy jakie otwarte pliki znajduja sie w obrebie procesu:
```bash
ls -l /proc/[pid]/fd -> ls -l /proc/5926/fd
```
Dostajemy:
```bash
l-wx------ 1 user user 64 OCT 11 18:18 3 -> 'home/user/so/numery.txt (deleted)'
```

4. Za pomocą comendy ```cat``` jestesmy wstanie wyswietlic zawartosc usunietego pliku:
```bash
cat /proc/[pid]/fd/[fd-number] -> cat /proc/5926/fd/3 
```

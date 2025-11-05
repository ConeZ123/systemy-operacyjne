# Zadania

1. Podaj polecenia, które:
- nadpisują określony tekst do pliku bez uzycia edytora
```bash
echo "tekst" > plik.txt
```
- dodaja okreslony tekst na koniec pliku bez uzycia edytora.
```bash
echo "tekst" >> plik.txt
```
2. Wymień skrót, który komentuje lub usuwa komentarz linii w nano.
```bash
ALT + 3
```
3. Wymień skróty, który dodają i odejmują wcięcie do bieżącej linii w nano.
```bash
Alt + } <- dodanie wciecia 
ALT + { <- usuniecie wciecia
```
4. Podaj nazwę pliku konfiguracyjnego nano i treść, która umożliwi, aby tabulatory były automatycznie zamieniane na spacje (za każdym uruchomieniem).
```bash
~/.nanorc <- plik konfiguracyjny
set tabstospaces <- zamiania tabulatorow na spacje
```
5. Podaj nazwę pliku konfiguracyjnego vim i treść, która umożliwi, aby tabulatory były automatycznie zamieniane na spacje (za każdym uruchomieniem).
```bash
~/.vimrc <- plik konfiguracyjnt
set expandtab
set tabstop=4
set shiftwidth=4
```
6. Uruchom ```vimtutor``` i wykonaj polecenia z tutorialu.
- Po uruchomieniu ```vimtutor``` zapisz szablon do pliku np. ```vim.txt``` (polecenie ```:w vim.txt```).
- Wyjdź z edytora i ręcznie otwórz plik przez polecenie ```vim vim.txt```.


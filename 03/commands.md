# Polecenia

1. Utwórz katalog lab w swoim katalogu domowym.

```bash
mkdir lab
```

2. Wyświetl prawa dostepu do katalogu lab.

```bash
ls -ld lab
```

3. Nadaj uprawnienia odczytu i wejścia do katalogu dla grupy i usuń uprawnienia dla pozostałych użytkowników (jednym poleceniem).

```bash
chmod g+rx,o-rwx lab 
```

4. Zapisz szczegółową zawartość katalogu /boot do pliku lab/boot.txt

```bash
ls -l /boot > lab/boot.txt
```

5. W katalogu lab utwórz jednym poleceniem strukturę katalogów dir1/dir2/dir3.

```bash
cd lab
mkdir -l dir1/dir2/dir3
```

6. Będąc w katalogu lab/dir1/dir2/ wyświetl zawartość pliku lab/boot.txt korzystając ze ścieżki relatywnej.

```bash
cat ../../boot.txt
```

7. Utwórz puste pliki tekst1.txt, tekst2.txt, tekst3.txt w katalogu lab.

```bash
touch tekst1.txt tekst2.txt tekst3.txt
```

8. Skopiuj pliki tekst1.txt, tekst2.txt, tekst3.txt do katalogu lab/dir1/dir2/dir3/ (jednym poleceniem).

```bash
cd lab
cp tekst*.txt dir1/dir2/dir3
```

9. Utwórz ukryty plik o dowolnej nazwie w katalogu lab.

```bash
cd lab
touch .ukryty_plik.txt
```

10. Zmień nazwę dowolnego pliku w katalogu lab/dir1/dir2/dir3.

```bash
mv tekst1.txt inny_tekst1.txt
```

11. Zapisz zawartość /proc/meminfo do pliku lab/tekst1.txt.

```bash
cat /proc/meminfo > lab/tekst1.txt
```

12. Dodaj zawartość /proc/cpuinfo do pliku lab/tekst1.txt.

```bash
cat /proc/meminfo >> lab/tekst1.txt
```

13. Zapisz kto jest zalogowany obecnie w systemie do pliku lab/tekst2.txt.

```bash
who > lab/tekst2.txt
```

14. Znajdź wszystkie katalogi o nazwie share, które znajdują się w /.

```bash
find /. -type d -name share 
```

15. Znajdź wszystkie pliki, które są większe niż 5 MB w katalogu /usr/bin.

```bash
find /usr/bin -type f -size +5M
```

16. Skopiuj wszystkie pliki zwykłe o rozmiarze pomiędzy 300 i 500 bajtów z katalogu /usr/bin do katalogu lab.

```bash
find /usr/bin -type f -size 300c -size 500c -exec cp {} ~/lab/\;
```

17. Utwórz dowiązanie twarde do pliku lab/tekst2.txt o nazwie lab/TEKST2.TXT.

```bash
ln lab/tekst2 lab/TEKST2.TXT
```

18. Utwórz dowiązanie symboliczne do pliku lab/tekst2.txt o nazwie lab/Tekst2.txt.

```bash
ln -s lab/tekst2.txt lab/Tekst2.txt
```

19. Wyświetl wszystkie elementy z katalogu lab wraz z ukrytymi plikami.

```bash
ls -la lab
```

20. Wyświetl pliki które mają w nazwie słowo ,,tty’’ z katalogu /dev/, korzystając z polecenia ls oraz grep.

```bash
ls /dev/ | grep tty
```

21. Korzystając z man na temat polecenia ls, znajdź sposób na wyświetlenie zawartości folderu lab wraz z podfolderami.

```bash
ls -R lab
```
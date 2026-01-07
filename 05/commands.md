# Grep - zadania

1. Wyświetl wszystkie procesy (polecenie ps axo command), które zawierają spację (tj. zostały prawdopodobnie uruchomione z jakimś parametrem).

```bash
ps axo command | grep " "
```

2. Wyswietl wszystkie linie z polecenia mount, które zawierają ścieżkę /dev/ lub /sys/ poprzedzoną znakiem spacji.

```bash
mount | grep -E "(/dev/|/sys/)"
```

3. Wyświetl wszystkie logi z polecenia journalctl -b, które zawierają słowo PCI lub USB (case-insensitive).

```bash
sudo journalctl -b | grep -iE "USB|PCI"
```

4. Wyświetl linie z pliku numery.txt, które zawierają tylko i wyłącznie męski numer PESEL (bez walidacji cyfry kontrolnej).

```bash
grep -E "^[0-9]{10}[02468]$" numery.txt
```

5. Wyświetl linie z pliku numery.txt, które zawierają tylko i wyłącznie żeński numer PESEL z urodzinami w 1999 roku (bez walidacji cyfry kontrolnej).

```bash
grep -E "^99$[0-9]{8}[13579]"
```

6. Wyświetl linie z pliku adresy.txt, które zawierają tylko i wyłącznie adres e-mail, wg następujących założeń:
- nazwa użytkownika - 1-16 liter/cyfr,
- znak oddzielający - @,
- domena - dowolna niezerowa ilość małych liter, 
- kropka,
- TLD (top level domain) - 2 lub więcej małych liter.

```bash
grep -E "^[a-zA-Z0-9]{1,16}+@[a-z]+\.[a-z]{2,}$" adresy.txt
```

7. Walidacja haseł - wyświetl linie z pliku hasla.txt, które spełniają wszystkie założenia:
- mają przynajmniej 8 znaków,
- mają przynajmniej jedną małą literę,
- mają przynajmniej jedną dużą literę,
- mają przynajmniej jedną cyfrę,
- mają przynajmniej jeden znak specjalny (!@#$%^&*()),
podpowiedź: możesz używać polecenie grep wielokrotnie.

```bash
grep -E "^.{8,}$" hasla.txt | grep "[A-Z]" | grep "[a-z]" | grep "[0-9]" | grep "[!@#$%^&*()]"
```

8. Pobierz i rozpakuj kod źródłowy programu git:

```
wget https://github.com/git/git/archive/refs/heads/master.zip
unzip master.zip
```

Wyświetl wszystkie linie w plikach z katalogu git-master rekursywnie, które zawierają słowo strlen wraz ze ścieżką do pliku i numerem linii.

```bash
grep -r "strlen" git-master/
```

9. Wyświetl linie z polecenia ip link, które zawierają heksadecymalne adresy MAC (wyrażenie regularne).

```bash
ip link | grep -E '([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}'
```

10. Wyświetl linie z polecenia ip addr, które zawierają adresy IPv4 (wyrażenie regularne) bez walidacji (każdy element w zakresie 0-999).

```bash
ip addr | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}"
```

11. Wyświetl linie z pliku ip.txt, które zawierają tylko i wyłącznie adresy IPv4 z walidacją (każdy element ma być w zakresie 0-255).

```bash
grep -E '^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$' ip.txt
```
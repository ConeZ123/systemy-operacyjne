# Zadania 

Do zadań będzie potrzebny plik: iris.csv ze zbiorem danych irysów (kwiaty). Zadania są niezależne od siebie.

Uwaga: Jeżeli w systemie są polskie ustawienia regionalne (locale), to należy poprzedzić polecenie awk zmianą zmiennej dotyczącej ustawień regionalnych liczbowych (numeric locale) ```LC_NUMERIC=C awk``` lub wszystkie ustawienia regionalne ```LC_ALL=C awk```.

1. Wypisz nagłówek (pierwszą linię) z iris.csv.
```bash
head -n 1 iris.csv
```
2. Wypisz wszystkie linie oprócz pierwszej z iris.csv (podpowiedź: skorzystaj z man tail).
```bash
tail -n +2 iris.csv
```
3. Zamień gatunki na liczby (wyświetl poprawione linie, nie zmieniaj treści pliku):
- “Setosa” na 1,
- “Versicolor” na 2,
- “Virginica” na 3.

```bash
tail -n +2 iris.csv | sed -e 's/Setosa/1/g' -e 's/Versicolor/2/g' -e 's/Virginica/3/g'
```
4. Wypisz dostępne rodzaje irysów bez powtórzeń i bez cudzysłowów.
```bash
cut -d ',' -f5 iris.csv | tail -n + 2 | tr -d '"' | sort | uniq
```
5. Oblicz sumę wartości dla każdego wiersza.
```bash
awk -F, '{print $1 + $2 + $3 + $4}' iris.csv
```
6. Oblicz średnią wartość drugiej kolumny (sepal.width).
```bash
awk -F, 'NR>1 {sum +=$2; n++} END {print sum/n}' iris.csv
```
7. Wypisz całą linię, która ma maksymalną wartość czwartej kolumny (petal.width).
```bash
awk -F, 'NR==2 {max=$4; line=$0} NR>2 && $4>max {max=$4; line=$0} END{print line}' iris.csv
```
8. Wypisz nazwę gatunku Irysa, którego pierwsza kolumna (sepal.length) jest większa niż 7.
```bash
awk -F, 'NR>1 && $1>7 { print$5 }' iris.csv
```
9. Przeformatuj plik CSV korzystając z printf w awk na pola oddzielone tabulatorami obcinając liczby do całkowitych.
```
5       4       1       0       "Setosa"
```
```bash
awk -F, 'NR>1 { printf "%d\t%d\t%d\t%d\t%s\n", $1,$2,$3,$4,$5}' iris.csv
```

10. Zmień losowo kolejność wierszy z danymi o irysach i zapisz je w nowym pliku CSV z nagłówkiem.
```bash
(head -n 1 iris.csv && tail -n +2 iris.csv | sort -R) > iris_sort.csv
```
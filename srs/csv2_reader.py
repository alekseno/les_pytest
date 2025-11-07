import csv

#если в таблице есть пустые ячейки
with open('srs/people_2.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        row = [value if value else "-" for value in row]
        print(row)
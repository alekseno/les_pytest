file = open('srs/text_ru.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
#кодировка
s = "Привет"
b = s.encode("utf-8")
print(b)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
print(list(b))  # [208, 159, 209, 128, 208, 184, 208, 178, 208, 181, 209, 130]

#декодирование
b = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
s = b.decode("utf-8")
print(s)  # Привет

#encoded = text.encode("utf-8")
#encoded = text.encode("cp1251")  # если, например, вам нужен Windows-формат
#decoded = bad_bytes.decode("utf-8", errors="replace")  # � вместо ошибки
#bad_bytes.decode("utf-8", errors="ignore")   # просто пропустит


#-------------------------------------------------------
#контекстный менеджер с with

with выражение as переменная:
    # блок кода, в котором используется ресурс
    # здесь можно читать или записывать в файл
# после выхода из блока файл автоматически закрывается

with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print("Файл прочитан:", text)

# Здесь файл уже закрыт автоматически, даже если выше случилась ошибка

try:
    with open("top_score_4.txt", "r", encoding="utf-8") as file:
        print('Файл закрыт?', file.closed)  # False
        pos = file.read().index("Python")  # вызовет ValueError
        print("Слово найдено на позиции:", pos)
except ValueError:
    print("Слово 'Python' не найдено")

# Проверим, закрыт ли файл
print('Файл закрыт?', file.closed)  # True



#try-finally -всегда закрывает файл, даже если внутри кода возникла ошибка
file = open("data.txt", "r", encoding="utf-8")
try:
    text = file.read()
    pos = text.index("Python")  # может кинуть ValueError
    print("Нашли 'Python' на позиции:", pos)
finally:
    file.close()
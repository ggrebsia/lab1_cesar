import tkinter as tk
from tkinter import messagebox

# Алфавит
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Частота символов в англ яз
chastota_simvolov = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228,
    'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025,
    'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987,
    'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
    'Y': 1.974, 'Z': 0.074
}

#функция шифрует строку по Цезарю
def cesar(stroka, step):
    new_stroka = ''
    for i in range(len(stroka)):
        k = 0
        while (stroka[i] != alphabet[k]):
            k += 1
        new_stroka += alphabet[(k + step) % len(alphabet)]
    return new_stroka

#Эта функция корректирует значение сдвига, чтобы оно было
#положительным и находилось в пределах длины алфавита
def sdvig(step):
    if step < 0:
        new_step = abs(len(alphabet) + step)
    else:
        new_step = step
    return new_step

# Функция расшифровывает строку
def decesar(stroka, step):
    new_stroka = ''
    for i in range(len(stroka)):
        k = 0
        while (stroka[i] != alphabet[k]):
            k += 1
        if (k - step < 0):
            new_stroka += alphabet[abs(len(alphabet) + k - step) % len(alphabet)]
        else:
            new_stroka += alphabet[(k - step) % len(alphabet)]
    return new_stroka

# Функция выполняет частотный анализ строки 
# и подсчитывает количество вхождений каждой буквы
def chastotnyi_analiz(stroka):
    slovar = dict()
    for simv in stroka:
        if simv in alphabet:
            if simv in slovar:
                slovar[simv] += 1
            else:
                slovar[simv] = 1
    return slovar
#функция вычисляет разницу между частотами букв в 
#заданной строке и частотами букв в англ.яз.
def raznica_chastot(slovar, chastota_simvolov):
    razlichie = 0
    for index in alphabet:
        razlichie += abs(slovar.get(index, 0) -
                                chastota_simvolov.get(index, 0))
    return razlichie

# Функция взлома
def vzlom_cesar(shifr_stroka):
    min_rzlch = float('inf')
    best_vzlom = ''

    for shift in range(len(alphabet)):
        vzlom_stroka = decesar(shifr_stroka, shift)
        dict_char = chastotnyi_analiz(vzlom_stroka)
        rzlch = raznica_chastot(dict_char, chastota_simvolov)

        if rzlch < min_rzlch:
            min_rzlch = rzlch
            best_vzlom = vzlom_stroka

    return best_vzlom


# Интерфейс
# Функция для обработки нажатия кнопки "Шифровать"
def shifr():
    input_str = input_text.get().upper()
    step = int(step_entry.get())
    new_step = sdvig(step)
    shifr_stroka = cesar(input_str, new_step)
    shifr_text.delete(0, tk.END)
    shifr_text.insert(0, shifr_stroka)

# Функция для обработки нажатия кнопки "Расшифровать"
def deshifr():
    input_str = shifr_text.get()
    step = int(step_entry.get())
    deshifr_str = decesar(input_str, step)
    deshifr_text.delete(0, tk.END)
    deshifr_text.insert(0, deshifr_str)

# Функция для обработки нажатия кнопки "Взломать"
def vzlom():
    input_str = shifr_text.get()
    best_vzlom = vzlom_cesar(input_str)
    vzlom_text.delete(0, tk.END)
    vzlom_text.insert(0, best_vzlom)




root = tk.Tk()
root.title("Шифрование и расшифрование")
# Ввод строки
tk.Label(root, text="Введите строку:").grid(row=0, column=0)
input_text = tk.Entry(root, width=50)
input_text.grid(row=0, column=1)
# Ввод сдвига
tk.Label(root, text="Введите сдвиг:").grid(row=1, column=0)
step_entry = tk.Entry(root, width=10)
step_entry.grid(row=1, column=1)
# Кнопка шифрования
encrypt_button = tk.Button(root, text="Шифровать", command=shifr)
encrypt_button.grid(row=2, column=0, columnspan=2)
# Зашифрованный текст
tk.Label(root, text="Зашифрованная строка:").grid(row=3, column=0)
shifr_text = tk.Entry(root, width=50)
shifr_text.grid(row=3, column=1)
# Кнопка расшифрования
deshifr_button = tk.Button(root, text="Расшифровать", command=deshifr)
deshifr_button.grid(row=4, column=0, columnspan=2)
# Расшифрованный текст
tk.Label(root, text="Расшифрованная строка:").grid(row=5, column=0)
deshifr_text = tk.Entry(root, width=50)
deshifr_text.grid(row=5, column=1)
# Кнопка взлома
vzlom_button = tk.Button(root, text="Взломать", command=vzlom)
vzlom_button.grid(row=6, column=0, columnspan=2)
# Взломанная строка
tk.Label(root, text="Взломанная строка:").grid(row=7, column=0)
vzlom_text = tk.Entry(root, width=50)
vzlom_text.grid(row=7, column=1)
root.mainloop()
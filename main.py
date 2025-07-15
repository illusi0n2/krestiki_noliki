import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x450")

current_player = "X"
buttons = []
score = {"X": 0, "0": 0}  # Счетчик побед


def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""


def new_game():
    global score
    score = {"X": 0, "0": 0}  # Обнуляем счетчик
    reset_game()  # Сбрасываем поле
    update_score()  # Обновляем отображение счета


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


def is_board_full():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True


def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        score[current_player] += 1
        update_score()
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!\nСчет: X - {score['X']} | 0 - {score['0']}")
        reset_game()
    elif is_board_full():
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()
    else:
        current_player = "0" if current_player == "X" else "X"


def update_score():
    score_label.config(text=f"X: {score['X']} | 0: {score['0']}")


# Создание игрового поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Кнопка новой игры (сброс всего)
new_game_btn = tk.Button(window, text="Новая игра", font=("Arial", 12), command=new_game)
new_game_btn.grid(row=3, column=0, columnspan=3, pady=10)

# Кнопка сброса только поля (можно добавить, если нужно)
reset_btn = tk.Button(window, text="Сброс поля", font=("Arial", 12), command=reset_game)
reset_btn.grid(row=4, column=0, columnspan=3, pady=5)

# Счетчик побед
score_label = tk.Label(window, text=f"X: {score['X']} | 0: {score['0']}", font=("Arial", 12))
score_label.grid(row=5, column=0, columnspan=3)

window.mainloop()
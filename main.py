import tkinter as tk
from tkinter import messagebox
from solver import calculate_function
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x**2 * np.sin(4 * np.sqrt(x))

def plot_function():
    x = np.linspace(0, 2, 400)
    y = function(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r'$y = x^2 \sin(4\sqrt{x})$', color='b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(r'График функции $y = x^2 \sin(4\sqrt{x})$')
    plt.grid(True)
    plt.legend()
    plt.show()

def open_calculator_window():
    def calculate():
        try:
            x = float(entry.get())
            y = calculate_function(x)
            result_label.config(text=f"Значение функции: {y}")
        except ValueError as e:
            messagebox.showerror("Ошибка", "Неправильное значение исходных данных")

    calc_window = tk.Toplevel(root)
    calc_window.title("Калькулятор функции")
    calc_window.geometry("250x200")

    tk.Label(calc_window, text="Введите значение x:").pack(pady=5)
    entry = tk.Entry(calc_window)
    entry.pack(pady=5)
    calculate_button = tk.Button(calc_window, text="Вычислить", command=calculate)
    calculate_button.pack(pady=5)
    result_label = tk.Label(calc_window, text="")
    result_label.pack(pady=5)

root = tk.Tk()
root.title("Главное окно")
root.geometry("250x200")

open_calc_button = tk.Button(root, text="Открыть калькулятор", command=open_calculator_window)
open_calc_button.pack(pady=10)
plot_function_button = tk.Button(root, text="Построить график", command=plot_function)
plot_function_button.pack(pady=10)

root.mainloop()

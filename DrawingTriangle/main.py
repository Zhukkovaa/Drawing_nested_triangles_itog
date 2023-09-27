import tkinter as tk
import math
from DrawingTriangle.input_validation import validate_input


class DrawingTriangle:
    """
       Класс для создания графического интерфейса приложения с использованием библиотеки Tkinter,
       которое строит и удаляет вложенные равносторонние треугольники с заданным шагом уменьшения стороны.

       Ключевые атрибуты:
           root (tk.Tk): Основное окно приложения.
           width_canvas (int): Ширина холста для рисования треугольников.
           height_canvas (int): Высота холста для рисования треугольников.
           canvas (tk.Canvas): Виджет tkinter для рисования.
           input_frame (tk.Frame): Виджет tkinter для размещения элементов управления вводом данных.
           data_label (tk.Label): Текстовая метка для вывода инструкций.
           h_label (tk.Label): Текстовая метка для ввода значения h.
           h_entry (tk.Entry): Поле ввода для значения h.
           error_label (tk.Label): Метка для вывода сообщений об ошибках.
           triangles (list): Список идентификаторов нарисованных треугольников.
           h (int): Текущее значение h (длина стороны) для рисования треугольников.
           h_increment (int): Значение шага, на которое уменьшается h при рисовании каждого нового треугольника.

       Методы:
           can_draw_triangle(h):
               Проверяет, можно ли нарисовать треугольник с заданным значением h.

           draw_triangle():
               Рисует треугольник на холсте с текущим значением h.

           delete_last_triangle():
               Удаляет последний нарисованный треугольник и восстанавливает значение h.

           on_key_press(event):
               Обработчик событий клавиатуры для реакции на клавиши Enter, D и Escape.

           run():
               Запускает главный цикл приложения.

    """
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная работа №1. Вариант №9")

        self.width_canvas = 600
        self.height_canvas = 600

        self.canvas = tk.Canvas(root, width=self.width_canvas, height=self.height_canvas)
        self.canvas.pack(side=tk.LEFT)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.data_label = tk.Label(self.input_frame, text="Введите размер шага и нажмите Enter, чтобы нарисовать")
        self.data_label.grid(row=0, columnspan=4, padx=5, pady=5)

        self.h_label = tk.Label(self.input_frame, text="Введите значение h:")
        self.h_label.grid(row=2, column=0, padx=5, pady=5)

        validate_input_cmd = root.register(lambda P: validate_input(P, self.error_label))

        self.h_entry = tk.Entry(self.input_frame, validate="key")
        self.h_entry.config(validatecommand=(validate_input_cmd, "%P"))
        self.h_entry.grid(row=2, column=1, padx=5, pady=5)

        self.error_label = tk.Label(self.input_frame, fg="red")
        self.error_label.grid(row=3, columnspan=2, padx=5, pady=5)

        self.triangles = []

        self.h = None
        self.h_increment = None

        self.root.bind("<Key>", self.on_key_press)

    def can_draw_triangle(self, h):
        """
            Проверяет, можно ли нарисовать треугольник с заданным значением h.

            Ключевые аргументы:
                h (int): Значение длины стороны h для треугольника.

            Возвращаемое значение:
                bool: True, если треугольник можно нарисовать, иначе False.

            Описание:
            Эта функция проверяет, можно ли нарисовать треугольник с заданным значением h. Для этого она сравнивает
            значение h с минимальным допустимым размером треугольника. Если h больше минимального размера, функция
            возвращает True, что означает, что треугольник можно нарисовать. В противном случае возвращается False.
        """
        min_size = 0
        if min_size < h:
            return True
        else:
            return False
    def draw_triangle(self):
        """
            Рисует треугольник на холсте с текущим значением h.

            Описание:
            Эта функция использует текущее значение h и h_increment для рисования треугольника на холсте. Если значение h равно None, то
            оно инициализируется начальным значением 500. Если значение h_increment равно None, оно берется из поля ввода h_entry.Она
            также обновляет значение h (оно очищается  для подготовки к следующему вводу) и блокирует поле ввода h_entry, чтобы предотвратить изменение `h`
            в процессе рисования треугольника. Если значение h соответствует условиям для рисования треугольника (если h больше минимального размера),
            то вычисляются координаты вершнит и треугольник рисуется на холсте. Значение h уменьшается на h_increment, чтобы готовиться
            к рисованию следующего треугольника. Идентификатор созданного треугольника добавляется в список `triangles`
            Если условие для рисования треугольника не выполняется, то на метке error_label выводится сообщение об ошибке
            "Вы не можете нарисовать треугольник меньшего размера!".
        """
        if self.h is None:
            self.h = 500
        if self.h_increment is None:
            self.h_increment = int(self.h_entry.get())
        self.h_entry.delete(0, tk.END)
        self.h_entry.config(state=tk.DISABLED)

        if self.can_draw_triangle(self.h):
            x_center = self.width_canvas / 2
            y_center = self.height_canvas / 2
            side_length = 2 * self.h / math.sqrt(3)

            x1 = x_center
            y1 = y_center - self.h / 2
            x2 = x_center - side_length / 2
            y2 = y_center + self.h / 2 - (self.h / 5)
            x3 = x_center + side_length / 2
            y3 = y_center + self.h / 2 - (self.h / 5)

            triangle = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="black")
            self.triangles.append(triangle)
            self.h -= self.h_increment
        else:
            self.error_label.config(text="Вы не можете нарисовать треугольник меньшего размера!")
    def delete_last_triangle(self):
        """
            Удаляет последний нарисованный треугольник и восстанавливает значение h.

            Описание:
            Эта функция проверяет наличие нарисованных треугольников в списке triangles и удаляет последний нарисованный треугольник с холста
            и из списка triangles и восстанавливает значение h до значения, соответствующего размеру предыдущего треугольника.
            Если значение h соответствует условиям для рисования треугольника, то метка error_label очищается от текста об ошибке.
        """
        if len(self.triangles) > 0:
            last_triangle = self.triangles.pop()

            coords = self.canvas.coords(last_triangle)
            x1, y1, x2, y2, x3, y3 = coords
            side_length = max(x1, x2, x3) - min(x1, x2, y3)
            self.h = (side_length * math.sqrt(3)) / 2

            if self.can_draw_triangle(self.h):
                self.error_label.config(text="")

            self.canvas.delete(last_triangle)
    def on_key_press(self, event):
        """
            Обработчик событий клавиатуры для реакции на клавиши Enter, D и Escape.

            Ключевые аргументы:
                event (tk.Event): Событие клавиатуры.

            Описание:
            Эта функция обрабатывает события клавиатуры. Если пользователь нажимает клавишу Enter, то вызывается
            функция draw_triangle() для отрисовеки вложенного треугольника. Если пользователь нажимает клавишу D
            (вне зависимости от регистра), то вызывается функция delete_last_triangle() для удаления последнего треугольника.
            Если пользователь нажимает клавишу Escape, то окно приложения закрывается.
        """
        if event.keysym == "Return":
            self.draw_triangle()
        elif event.keysym.lower() == "d":
            self.delete_last_triangle()
        elif event.keysym == "Escape":
            self.root.destroy()

    def run(self):
        """
            Запускает главный цикл приложения.

            Описание:
            Эта функция запускает главный цикл приложения, который обрабатывает события и отображает интерфейс на экране.
            Вызывается для запуска приложения после его инициализации.
        """
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingTriangle(root)
    app.run()

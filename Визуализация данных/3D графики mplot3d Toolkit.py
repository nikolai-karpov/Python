import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Линейный график
# Axes3D.plot(self, xs, ys, *args, zdir='z', **kwargs)
"""
Параметры функции Axes3D.plot:
• xs, ys: 1D-массивы
◦ Координаты точек по осям x и y.
• zs: число или 1D-массив
◦ z координаты. Если передано скалярное значение, то оно будет
присвоено всем точкам графика.
• zdir: {'x', 'y', 'z'}; значение по умолчанию: 'z'
◦ Ось, которая будет принята за z направление.
• **kwargs
◦ Дополнительные аргументы, аналогичные тем, что используются
в функции plot() для построения двумерных графиков.
"""
x = np.linspace(-np.pi, np.pi, 50)
y = x
z = np.cos(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')
 
 
# Точечный график (диаграмма рассеяния)
"""
Axes3D.scatter(self, xs, ys, zs=0, zdir='z', s=20, c=None,
depthshade=True, *args, **kwargs)
Параметры функции Axes3D.scatter():
• xs, ys: 1D-массив
    ◦ Координаты точек по осям x и y.
• zs: число или 1D-массив, optional; значение по умолчанию: 0
    ◦ Координаты точек по оси z. Если передано скалярное значение,то оно будет присвоено всем точкам графика.
- zdir: {'x', 'y', 'z', '-x', '-y', '-z'}, optional; значение по умолчанию 'z'
    ◦ Ось, которая будет принята за z направление.
• s: число или массив, optional; значение по умолчанию 20
    ◦ Размер маркера.
• c: цвет14, массив чисел, массив цветовых элементов, optional
    ◦ Цвет маркера. Возможные значения:
        ▪ строковое значение цвета для всех маркеров;
        ▪ массив строковых значений цвета;
        ▪ массив чисел, которые могут быть отображены в цвета через функции cmap и norm;
        ▪ 2D-массив, элементами которого являются RGB или RGBA;
• depthshade: bool, optional
    ◦ Затенение маркеров для придания эффекта глубины.
• **kwargs
    ◦ Дополнительные аргументы, аналогичные тем, что используются в функции scatter() для построения двумерных графиков.
"""

np.random.seed(123)
x = np.random.randint(-5, 5, 40)
y = np.random.randint(0, 10, 40)
z = np.random.randint(-5, 5, 40)
s = np.random.randint(10, 100, 20)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s)


# Каркасная поверхность
# используется функция plot_wireframe() из Axes3D:
# Axes3D.plot_wireframe(self, X, Y, Z, *args, **kwargs)
"""
Параметры функции Axes3D.plot_wireframe():
• X, Y, Z: 2D-массивы
    ◦ Данные для построения поверхности.
• rcount, ccount: int, значение по умолчанию: 50
    ◦ Максимальное количество элементов каркаса, которое будет использовано в каждом из направлений.
• rstride, cstride: int
    ◦ Параметры, определяющие величину шага, с которым будут браться элементы строки/столбца из переданных массивов.
      Параметры rstride, cstride и rcount, ccount являются взаимоисключающими.
• **kwargs
    ◦ Дополнительные аргументы, которые являются параметрами конструктора класса Line3DCollection.
"""

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z)
ax.legend()


# Поверхность
# используется функция plot_surface() из Axes3D:
# Axes3D.plot_surface(self, X, Y, Z, *args, norm=None, vmin=None, vmax=None, lightsource=None, **kwargs)
"""
Параметры функции Axes3D.plot_surface():
    • X, Y, Z: 2D-массивы
        ◦ Данные для построения поверхности.
    • rcount, ccount: int
        ◦ см. rcount, ccount из “5.3 Каркасная поверхность”.
    • rstride, cstride : int
        ◦ см.rstride, cstride из “5.3 Каркасная поверхность”.
    • color: один из доступных способов задания цвета (см. раздел“2.3.2 Цвет линии”).
        ◦ Цвет для элементов поверхности.
    • cmap: str или Colormap, optional
        ◦ Цветовая карта для поверхности (см. "4.4.1 Цветовые карты (colormaps)")
    • facecolors: массив цветовых элементов
        ◦ Индивидуальный цвет для каждого элемента поверхности.
    • norm: Normalize
        ◦ Нормализация для colormap.
    • vmin, vmax: float
        ◦ Границы нормализации.
    • shade: bool; значение по умолчанию: True
        ◦ Использование тени для facecolors.
    • lightsource: LightSource
        ◦ Объект класса LightSource определяет источник света, используется, только если shade=True.
    • **kwargs
        ◦ Дополнительные аргументы, которые являются параметрами конструктора класса Poly3DCollection.
"""

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='inferno')
ax.legend()



plt.show()
import Graphs
import CIRCLE
import Spline
import math

'CNC parameters'
BLU = 0.01 #mm
T = 0.01 #sec
V = 25 #mm/sec
V = [20.000110983746588, 20.000886687703122, 20.002985931975907, 20.007055788833704, 20.01372583924846, 20.023602584690025, 20.037264063776195, 20.05525472156099, 20.078080577001817, 20.106204731499396, 20.140043258376924, 20.179961509783816, 20.226270873804157, 20.279226010554023, 20.339022591800262, 20.40579556416404, 20.47961795132508, 20.560500205858308, 20.64839011645606, 20.743173271359343, 20.84467407388471, 20.952657301032858, 21.0668301913446, 21.18684504347234, 21.312302302401807, 21.442754105930693, 21.57770825992522, 21.71663260707015, 21.858959750334776, 22.004092089229133, 22.15140712414826, 22.30026298172275, 22.450004112132238, 22.59996710781199, 22.749486591905445, 22.897901124196263, 23.044559072098533, 23.188824394593734, 23.33008228777584, 23.46774464189432, 23.601255261457908, 23.73009480206516, 23.853785380142146, 23.971894814670858, 24.08404046325854, 24.18989261849864, 24.289177434477104, 24.381679357448096, 24.467243039104297, 24.54577471545948, 24.617243039104295, 24.681679357448097, 24.739177434477103, 24.789892618498637, 24.83404046325854, 24.87189481467086, 24.903785380142146, 24.930094802065163, 24.95125526145791, 24.96774464189432, 24.980082287775843, 24.988824394593735, 24.994559072098532, 24.997901124196265, 24.99948659190545, 24.999967107811994, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
'Corner parameters'
Lt = 1
n = 0.9

'Построение окружности'
"""center_point = [1, 0, 0]
start_point = [-4, 0, 0]
finish_point = [6, 0, 0]
circle_result = CIRCLE.Circle_interpolation(center_point, 5, BLU)
volume = 50
u_r = [0, math.pi/2]
circle_test = CIRCLE.Circle_parametric_interpolation(V, T, volume, u_r)
#Russian
#Graphs.Plotting_bw(circle_test[0], circle_test[1], 'Ось X, мм', 'Ось Y', 'Окружность', 'da', 'circle')
#English
Graphs.Plotting_bw(circle_test[0], circle_test[1], 'X, mm', 'Y, mm', 'Arc interpolation', 'Tool path', 'PIC_2')
print('Минимальная величина сегмента: ' + str(min(circle_test[2])))
print('Максимальная величина сегмента: ' + str(max(circle_test[2])))
print('Число сегментов: ' + str(len(circle_test[2])))
print('Контурная ошибка: ' + str(max(circle_test[3])))
print('Контурная ошибка: ' + str(min(circle_test[3])))
print('_________________________________')
"""

'Построение кривой с равными u'
"""
curve_r = CIRCLE.Curve_conventional_2D ()
print('Число сегментов: ' + str(curve_r[2]-1))
#Russian
#Graphs.Plotting_01(curve_r[0], curve_r[1], 'Ось X', 'Ось Y', 'Кривая', 'траектория движения инструмента', 'circle1')
#English
#Graphs.Plotting_bw(curve_r[0], curve_r[1], 'X, mm', 'Y, mm', 'Curve example', 'Tool trajectory', 'PIC_1')
print('Минимальная величина сегмента: ' + str(min(curve_r[4])))
print('Максимальная величина сегмента: ' + str(max(curve_r[4])))
print('Максимальная подача: ' + str(max(curve_r[4])/T))
print('Минимальная подача: ' + str(min(curve_r[4])/T))
print('Максимальная контурная ошибка: ' + str(max(curve_r[3])))
print('Минимальная контурная ошибка: ' + str(min(curve_r[3])))
"""
print('_________________________________')

'Построение кривой с равными участками'
curve_r = CIRCLE.Curve_equal_s_2D (V, T)
Graphs.Plotting_01(curve_r[0], curve_r[1], 'мм', 'мм', 'Кривая', 'траектория движения инструмента', 'circle2')
print('Число сегментов: ' + str(len(curve_r[4])))
print('Максимальная контурная ошибка: ' + str(max(curve_r[3])))
print('Минимальная контурная ошибка: ' + str(min(curve_r[3])))
print('Минимальная величина сегмента: ' + str(min(curve_r[4])))
print('Максимальная величина сегмента: ' + str(max(curve_r[4])))

'Построение траектории со скруглениями'
'Траектория'
points = [[2, 2, 0],
          [2, 5, 0],
          [6, 8, 0],
          [8, 4, 0],
          [5, 0, 0],
          [2, 2, 0]]
x_points = []
y_points = []
x_no_smooth = []
y_no_smooth = []
for i in range (len(points)):
    x_no_smooth.append(points[i][0])
    y_no_smooth.append(points[i][1])
x_points.append(points[0][0])
y_points.append(points[0][1])
for i in range (len(points)-2):
    corner_smooth = Spline.Spline_6(Lt, n, points[i], points[i+1], points[i+1],  points[i+2])
    for j in range (len(corner_smooth[0])):
        x_points.append(corner_smooth[0][j])
        y_points.append(corner_smooth[1][j])
x_points.append(points[len(points)-1][0])
y_points.append(points[len(points)-1][1])

#Graphs.Plotting_01(x_no_smooth, y_no_smooth, 'Ось X', 'Ось Y', 'Исходная траектория', 'Траектория', 'input_trajectory')
#Graphs.Plotting_01(x_points, y_points, 'Ось X', 'Ось Y', 'Скругление', 'Реальная траектория', 'output_trajectory')
#Graphs.Plotting_02(x_points, y_points, x_no_smooth, y_no_smooth,
#                   'Ось X', 'Ось Y', 'Построение треаектории со скруглениями', 'Реальная траектория', 'Заданная траектория', 'final_trajectories')

#Graphs.Plotting_01(x_coord, y_coord, 'Ось X', 'Ось Y', 'Угол', 'da', 'circle')
#Graphs.Plotting_01(corner_smooth[0], corner_smooth[1], 'Ось X', 'Ось Y', 'Скругление', 'Реальная траектория', 'circle')

#Graphs.Plotting_02(corner_smooth[0], corner_smooth[1], corner_smooth[3], corner_smooth[4],
#                   'Ось X', 'Ось Y', 'Скругление', 'Реальная траектория', 'circle', 'smoothing')

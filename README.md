# Цифровая обработка сигналов
# Лабораторная работа 1
1. Написать программную функцию формирования гармонического сигнала.  
а) при постоянных A и fi задать 5 значений фазы f. Вывести 5 реализаций сигнала, отследить изменение графиков. Значения A, f, fi выбираются в соответствии с вариантом задания.  
б) при постоянных A и f задать 5 значений частоты fi. Вывести 5 реализаций сигнала, отследить изменение графиков. Значения A, f, fi выбираются в соответствии с вариантом задания.  
в) при постоянных f и fi задать 5 значений амплитуды A. Вывести 5 реализаций сигнала, отследить изменение графиков. Значения A, f, fi выбираются в соответствии с вариантом задания.  
2. Написать программу формирования полигармонического сигнала. Значения A, f, fi задаются из таблицы в соответствии с вариантом задания. При постоянных A, fi изменять f, исследовать влияние фазы на максимум сигнала.  
3. Написать программу формирования полигармонического сигнала, у которого амплитуды, частоты, начальные фазы изменяются по линейному закону в сторону возрастания или убывания, при этом на одном периоде полигамонического сигнала параметр не должен изменяться более чем на 20%.  

# Лабораторная работа 2
1. Написать программу формирования гармонического сигнала. 
2. Для каждой реализации сигнала вычислить среднее квадратическое значение (СКЗ). 
3. Для каждой реализации сигнала с помощью дискретного преобразования Фурье вычислить амплитуду сигнала. 
4. Для каждого вычисления СКЗ определить погрешность вычисления СКЗ и амплитуды. 
5. Повторть все то же, для формулы с fi.

# Лабораторная работа 3
1. Обработка гармонических сигналов:  
а) Разработать функцию для вычисления дискретного преобразования Фурье. В соответствии с вариантом задания сформировать тестовые сигналы. Для каждого из тестовых сигналов построить амплитудный и фазовый спектры.  
б) Восстановить исходный сигнал по спектру. Сравнить исходный и восстановленный сигналы.
2. Обработка полигармонических сигналов  
а) Сформировать полигармонический сигнал. Для сформированного сигнала вычислить амплитудный и фазовый спектр сигнала.  
б) Восстановить исходный сигнал по спектру. Сравнить исходный и восстановленный сигналы.  
в) Восстановить исследуемый сигнал по спектру без учета начальных фаз. Сравнить исходный и восстановленный  сигналы.  
3. Реализовать цифровую фильтрацию сигналов (НЧ-фильтр, ВЧ-фильтр, полосовой фильтр) на основе применения прямого и обратного преобразования Фурье и удаления ненужных спектральных составляющих. Исследовать модельные и реальные сигналы с помощью разработанных функций.

# Лабораторная работа 4
1. Сформировать сигнал для исследований.  
2. Вычислить спектр сформированного сигнала.  
3. Провести сглаживание сигнала следующими способами:  
- скользящим усреднением с окном сглаживания в соответствии с вариантом задания;  
- параболой четвертой степени;  
- медианной фильтрацией с размером окна в соответствии с вариантом задания.  
Для каждого случая, после выполнения сглаживания, выводить в виде графика форму сигнала.  
4. Вычислить спектр сглаженного сигнала.  

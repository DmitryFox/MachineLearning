
# Непараметрическая регрессия.<br />Формула Надарая-Ватсона. Метод LOWESS.

## Функция Ядра:
В [непараметрической статистике](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0 "Непараметрическая статистика") под ядром понимается весовая функция, используемая при оценке распределений и параметров ([ядерная оценка плотности](https://ru.wikipedia.org/wiki/%D0%AF%D0%B4%D0%B5%D1%80%D0%BD%D0%B0%D1%8F_%D0%BE%D1%86%D0%B5%D0%BD%D0%BA%D0%B0_%D0%BF%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D0%B8 "Ядерная оценка плотности"), [ядерная регрессия](https://ru.wikipedia.org/wiki/%D0%AF%D0%B4%D0%B5%D1%80%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F "Ядерная регрессия")).  Ядерная оценка плотности является задачей сглаживания данных. Смысл ядерной регрессии заключается в поиске нелинейного отношения между парой случайных величин **X** и **Y**. Ядерная оценка требует специфицировать ширину окна.

**В задаче непараметрической регрессии были реализованы следующие ядра на языке Python:**
* Гауссовское ядро:<br />
![equation](https://latex.codecogs.com/gif.latex?{\displaystyle%20K(u)={\frac%20{1}{\sqrt%20{2\pi%20}}}e^{-{\frac%20{1}{2}}u^{2}}})
* Квартическое ядро (оно же биквадратичное):<br />
![equation](https://latex.codecogs.com/gif.latex?{\displaystyle%20K(u)={\frac%20{15}{16}}(1-u^{2})^{2}})<br />
Носитель: ![equation](https://latex.codecogs.com/gif.latex?{\displaystyle%20|u|\leq%201})

## Формула Надарая-Ватсона:

Формула Надарая-Ватсона используется для решения задачи непараметрического [восстановления регрессии.](http://www.machinelearning.ru/wiki/index.php?title=%D0%A0%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7 "Восстановление регрессии")

Реализована формула Надарая-Ватсона на языке python:<br />
![equation](https://latex.codecogs.com/gif.latex?a_h(x;X^l)%20=%20\frac{\sum_{i=1}^{l}%20y_i\omega_i(x)}{\sum_{i=1}^{l}%20\omega_i(x)}%20=%20\frac{\sum_{i=1}^{l}%20y_iK\left(\frac{\rho(x,x_i)}{h}%20\right%20)}{\sum_{i=1}^{l}%20K\left(\frac{\rho(x,x_i)}{h}%20\right%20)})

Функция находиться в файле `regression.py`
```python
def nadaraya_watson(value, x, y, h, kernel, metric):
```
Принимает аргументы: `value` - искомое, оптимальное значение в точке x;  `x` - вектор объектов;  `y` - вектор ответов; `h` - коэффициент сглаживания (ширина окна); `kernel` - функция ядра; `metric` - функция метрики (находящая длину).

Пример в виде графика:<br />
<img src="https://raw.githubusercontent.com/DmitryFox/MachineLearning/master/Task_2_1_NonparametricRegression_NadarayaWatson/image/nadaray_watson_gauss_and_quartic.png" width="350" />

<br />

> Использованная литература:
> 1) MachineLearning.ru (Надаряйа-Ватсон) - http://www.machinelearning.ru/wiki/index.php?title=%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0_%D0%9D%D0%B0%D0%B4%D0%B0%D1%80%D0%B0%D1%8F-%D0%92%D0%B0%D1%82%D1%81%D0%BE%D0%BD%D0%B0);
> 2) MachineLearning.ru (LOWESS) - http://www.machinelearning.ru/wiki/index.php?title=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_LOWESS
> 2) Википедия (Функция ядра) - https://ru.wikipedia.org/wiki/%D0%AF%D0%B4%D1%80%D0%BE_(%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0);
> 3) Книга - Математические методы обучения по прецедентам (теория обучения машин) К. В. Воронцов


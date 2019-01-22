
# Непараметрическая регрессия.<br />Формула Надарая-Ватсона. Метод LOWESS.

## Метод LOWESS

Оценка Надарайя–Ватсона крайне чувствительна к большим одиночным выбросам. Идея обнаружения выбросов заключается в том, что чем больше величина ошибки, тем в большей степени прецеддент является выбросом, и тем меньше должен быть его вес.

Алгоритм LOWESS  выглядит следующим образом:
* Вход:
	* ![equation](https://latex.codecogs.com/gif.latex?X^m) — обучающая выборка;
	* ![equation](https://latex.codecogs.com/gif.latex?w_t,%20\,\,\,%20t=1,\ldots,m) весовые функции;
* Выход:
	* коэффициенты ![equation](https://latex.codecogs.com/gif.latex?\delta_t,%20\,\,\,%20t=1,\ldots,m)
#
1. Инициализировать ![equation](https://latex.codecogs.com/gif.latex?\gamma_1:=\ldots=\gamma_m:=1)
2. **повторять**
3. Вычислить оценки скользящего контроля на каждом объекте: <br />
![equation](https://latex.codecogs.com/gif.latex?a_i:=a_h(x_i;%20X^\ell\setminus\{x_i\})%20=%20\frac{%20\sum_{i=1,%20i\neq%20t%20}^{m}%20{y_i%20\gamma_i%20K\left(%20\frac{\rho(x_i,x_t)}%20{h(x_t)}\right)}}%20{\sum_{i=1,%20i\neq%20t%20}^{m}%20{\gamma_i%20K\left(%20\frac{\rho(x_i,x_t)}{h(x_t)}\right)}%20})
4. Вычислить коэфициенты: ![equation](https://latex.codecogs.com/gif.latex?\gamma_i)<br />
![equation](https://latex.codecogs.com/gif.latex?\gamma_i:=%20\tilde{K}(|%20a_i%20-%20y_i%20\|);%20i%20=%201,...,\ell;)
5. **пока** коэффициенты ![equation](https://latex.codecogs.com/gif.latex?\gamma_i) не стабилизируются;

Примеры в виде графика:<br />
<img src="https://raw.githubusercontent.com/DmitryFox/MachineLearning/master/Task_2_2_LowessMethodForNonparametricRegression/image/lowess_gauss_and_quartic.png" width="350" />

<br />

## Сравнение Формулы Надарая-Ватсона с методом LOWESS:

Примеры в виде графика:<br />
1) Использовано Гауссовское Ядро:<br />
<img src="https://github.com/DmitryFox/MachineLearning/blob/master/Task_2_2_LowessMethodForNonparametricRegression/image/lowess_watson_gauss.png?raw=true" width="350" /><br />

Method | SSE
------------- | -------------
Nadaraya-Watson  | 425.4048270963928
LOWESS | 276.610708711001

2) Использовано Квадратичное Ядро:<br />
<img src="https://github.com/DmitryFox/MachineLearning/blob/master/Task_2_2_LowessMethodForNonparametricRegression/image/lowess_watson_quartic.png?raw=true" width="350" /><br />

Method | SSE
------------- | -------------
Nadaraya-Watson  | 595.2909859959468
LOWESS | 466.56825738979785

<br />

> Использованная литература:
> 1) MachineLearning.ru (Надаряйа-Ватсон) - http://www.machinelearning.ru/wiki/index.php?title=%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0_%D0%9D%D0%B0%D0%B4%D0%B0%D1%80%D0%B0%D1%8F-%D0%92%D0%B0%D1%82%D1%81%D0%BE%D0%BD%D0%B0);
> 2) MachineLearning.ru (LOWESS) - http://www.machinelearning.ru/wiki/index.php?title=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_LOWESS
> 2) Википедия (Функция ядра) - https://ru.wikipedia.org/wiki/%D0%AF%D0%B4%D1%80%D0%BE_(%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0);
> 3) Книга - Математические методы обучения по прецедентам (теория обучения машин) К. В. Воронцов


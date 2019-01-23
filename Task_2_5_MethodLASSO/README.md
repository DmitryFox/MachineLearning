## Lasso
**Lasso** (Least absolute shrinkage and selection operator)  - метод оценивания коэффициентов линейной регрессионной модели. 

Метод заключается во введении ограничения на норму вектора коэффициентов модели, что приводит к обращению в 0 некоторых коэффициентов модели. Метод приводит к повышению устойчивости модели в случае большого числа обусловленности матрицы признаков X, позволяет получить интерпретируемые модели  - отбираются признаки, оказывающие наибольшее влияние на вектор ответов.

Метод регуляризации внешне похож на гребневую регрессию, но приводит к качественно иному поведению вектора коэффициентов. Вместо добавления
штрафного слагаемого к функционалу качества вводится ограничение-неравенство,
запрещающее слишком большие абсолютные значения коэффициентов:

![equation](https://latex.codecogs.com/gif.latex?\left\{\begin{array}{l}{Q(\alpha)=\|F%20\alpha-y\|^{2}%20\rightarrow%20\min%20_{\alpha}}%20\\%20{\sum_{j=1}^{n}\left|\alpha_{j}\right|%20\leqslant%20x}\end{array}\right.)
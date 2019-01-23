## Метод главных компонент
Решение проблемы мультиколлинеарности заключается в том, чтобы подвергнуть исходные признаки некоторому функциональному преобразованию,
гарантировав линейную независимость новых признаков, и, возможно, сократив их
количество, то есть уменьшив размерность задачи.

В методе главных компонент (principal component analysis, PCA) строится
минимальное число новых признаков, по которым исходные признаки восстанавливаются линейным преобразованием с минимальными погрешностями. PCA относится к методам обучения без учителя (unsupervised learning), поскольку матрица
«объекты–признаки» F преобразуется без учёта целевого вектора y.

Важно отметить, что PCA подходит и для регрессии, и для классификации,
и для многих других типов задач анализа данных, как вспомогательное преобразование, позволяющее определить эффективную размерность исходных данных

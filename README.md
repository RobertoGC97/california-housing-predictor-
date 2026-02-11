# California Housing Prediction

Este proyecto utiliza datos del censo de Estados Unidos para predecir el **valor medio de las viviendas** en diversos distritos de California. El análisis abarca desde la exploración de datos y la ingeniería de variables hasta la implementación de modelos de aprendizaje supervisado para optimizar la precisión de las predicciones financieras en el sector inmobiliario. El conjunto de datos contiene información de **20,640 ubicaciones** con las siguientes variables clave:

* **Geográficas:** Latitud y longitud.
* **Demográficas:** Población total, número de hogares y edad promedio de las casas.
* **Económicas:** Ingreso medio de los habitantes (predictor principal).
* **Vivienda:** Total de habitaciones y dormitorios.
* **Target:** Valor medio de la casa (`median_house_value`).

## Metodología y Preprocesamiento

Durante la fase de preparación de datos se realizaron las siguientes tareas críticas:

1. **Análisis Exploratorio (EDA):** Identificación de distribuciones estadísticas y correlaciones.
2. **Tratamiento de Nulos:** Se realizó la imputación de valores faltantes en la columna `total_bedrooms` utilizando la **mediana** del conjunto de entrenamiento.
3. **Ingeniería de Variables:** Creación de nuevos ratios para mejorar el rendimiento del modelo:
* Habitantes por casa.
* Dormitorios por habitaciones.


4. **Codificación:** Transformación de la variable categórica `ocean_proximity` a formatos numéricos procesables.

## Modelos Evaluados

Se compararon dos aproximaciones tecnológicas para resolver el problema de regresión:

| Modelo | Error (RMSE) | Descripción |
| --- | --- | --- |
| **XGBoost (Modelo A)** | **$46,283.18** | El más eficiente; maneja mejor las variaciones naturales de los datos. |
| **Regresión Lineal (Modelo B)** | $61,725.10 | Presentó un error significativamente mayor debido a la  naturaleza de los datos. |

## Hallazgos Clave

* El **ingreso medio (`median_income`)** es la variable con mayor peso real en el precio, con una importancia del **46.6%**.
* Las variables finales seleccionadas para la optimización fueron: ingreso medio, ratio de habitantes, longitud y latitud.

## Conclusión

El modelo basado en **XGBoost** es el recomendado para la implementación operativa, ya que ofrece una capacidad de generalización superior para predecir el valor del mercado inmobiliario en California, minimizando el ruido estadístico identificado.

---

### Tecnologías Utilizadas

* **Lenguaje:** Python 3.12
* **Librerías:** Pandas, NumPy, Scikit-Learn, XGBoost, Seaborn, Matplotlib, Plotly.

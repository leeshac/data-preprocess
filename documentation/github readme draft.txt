purpose:
a data pre processor pypi package to efficiently take care of the process of cleaning and splitting both various data types.

===========================================================
NUMERICAL DATA

numerical-discrete.py
- numerical discrete data is data that is counted, such as ages, cars, days. float numbers do not exist, only whole numbers.
> due to this we need to consider removing null values and clipping outliers

numerical-continuous.py
- numerical continuous data is data that exists within a range, so can be measured like height, speed, grades. both whole and float numbers coexist.
> due to this we need to consider removing null values, clipping outliers, transforming distribution and scaling numbers (normalisation).
===========================================================
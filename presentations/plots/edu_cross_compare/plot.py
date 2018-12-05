import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

plt.plot([1985, 1990, 1995, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2017], [95.9, 97.8, 98.5, 99.1, 98.6, 98.9, 99.3, 99.5, 99.7, 99.9, 99.8, 99.9, 99.9], 'ro')
plt.axis([1985, 2017, 95, 100])

plt.xlabel('Net Enrolment Ratio of School-age Children in Primary Schools')
plt.ylabel('Year')

plt.savefig('cnelementry.png')

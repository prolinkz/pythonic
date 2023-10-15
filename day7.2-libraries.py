
print('''
      
      In Python, modules and libraries are two different ways of organizing and structuring code.

A module is a single Python file that contains a set of related functions, classes, and variables. Modules can be imported into other Python files, allowing you to reuse code across multiple projects.

A library is a collection of modules that are related to a specific task or domain. Libraries can be installed from the Python Package Index (PyPI) or from third-party sources. Once installed, libraries can be imported into your Python projects.

Modules and libraries are essential for organizing and structuring Python code. They allow you to reuse code, share code with others, and extend the functionality of your Python programs.

Here are some of the benefits of using modules and libraries in Python:

Reusability: Modules and libraries allow you to reuse code across multiple projects. This can save you time and effort, and it can also help to ensure that your code is consistent and well-organized.
Sharing: Modules and libraries can be shared with others, making it easy to collaborate on Python projects. This can be especially helpful if you are working on a project with a team of developers.
Extensibility: Modules and libraries can be used to extend the functionality of your Python programs. This can allow you to add new features to your programs without having to write all of the code yourself.
If you are new to Python, I recommend that you start by learning about modules and libraries. These are essential tools for organizing and structuring Python code, and they can help you to write more efficient and effective programs.
    
    ''')

print('''
      Python for Data Analytics
      Python Cheatsheet 
      Pandas Documenetation - Getting started https://pandas.pydata.org/docs/

      Ctrl+J to open Teegle Terminal on Visual Studio Editor
      Install library : > pip install library_name    # like, pandas

      # or, conda install library_name   # like, numpy
      ''')

print('''
Python Libraries:
      - Pandas: https://pandas.pydata.org/
      open source data analysis and manipulation tool,
built on top of the Python programming language.
      - Numpy: https://numpy.org/
      NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more.
      - Matplotlib: https://matplotlib.org/
      Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python
      - Seaborn: https://seaborn.pydata.org/
      Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
      - scipy: https://scipy.org/
      SciPy provides algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations, statistics and many other classes of problems.
      Extends NumPy providing additional tools for array computing and provides specialized data structures, such as sparse matrices and k-dimensional trees.
      - statsmodel: https://www.statsmodels.org/stable/index.html
      StatsModel provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration.
      statsmodels supports specifying models using R-style formulas and pandas DataFrames.
      - Scikit-learn: https://scikit-learn.org/stable/
      Simple and efficient tools for predictive data analysis.
      Built on NumPy, SciPy, and matplotlib
      - NLTK: https://www.nltk.org/
      NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries
      - BeautifulSoup: https://pypi.org/project/beautifulsoup4/ 
      A Python package for parsing HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
      Web Scrapper project at https://realpython.com/beautiful-soup-web-scraper-python/

      ''')

print('''
      
Ctrl+J to open Teegle Terminal on Visual Studio Editor
      Install library : > pip install library_name    # like, pandas
*** check the project environment if it ml_env enviroment which is created on Day2 or 3 for (Machine Learning)
*** If the ml_env is not activated, then Open MiniConda and Activate the ml_env first then Install libraries on VS code Editor or direct from MiniConda console.
      
      (ml_env) C:/..> pip install pandas numpy matplotlib seaborn scipy statsmodel

- Once we Install the libraries, we can then Import these libraries
  import pandas
      import math
      from math import sqrt  ## import square root functiion from math library, so we dont need to write thhese functions which also known as buuilt-in functions, we only need to import
      print(sqrt(9))


      ''')

## Import square root function from math library 
import pandas
import math
from math import sqrt  ## import square root functiion from math library, so we dont need to write thhese functions which also known as buuilt-in functions, we only need to import
print(sqrt(9))

# or we can import simply, like
import math
print(math.sqrt(9))  # Output: 3


# We can name to these libraries to not use all the time, like
import pandas as pd
import math as mt
import numpy as np


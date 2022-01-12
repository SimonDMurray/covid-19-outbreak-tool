# Python code compliance

## Instructions

This must be assessed by the pycodestyle and pylint tools. 
Please note your code must conform to the 79 characters line length limit. 
You must use the `pycodestyle` and `pylint` tools and include the output for 
all python code in this file `README_PEP8.md`. 

pycodestyle should not produce any warnings.

It is acceptable to have pylint warnings (for instance missing docstrings for unit tests)
 provided they are justified in README_PEP8.md..

## `pycodestyle *.py` output
```
pwd 
/Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/covid19_graphs
```
No output

```
pwd
/Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/covid19_graphs/tests
```
No output

``` 
pwd
/Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray
```
No output
## `pylint *.py` output
```
pwd 
/Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/covid19_graphs
```

```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

```
pwd
/Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/covid19_graphs/tests
```

``` 
************* Module test_covid19processing
test_covid19processing.py:8:0: C0116: Missing function or method docstring (missing-function-docstring)
test_covid19processing.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
test_covid19processing.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
test_covid19processing.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
test_covid19processing.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
test_covid19processing.py:77:0: C0116: Missing function or method docstring (missing-function-docstring)
test_covid19processing.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module test_parse_command_line_args
test_parse_command_line_args.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)
```

``` 
pwd
/Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray
```

```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## justification for pylint warnings
1) Missing function docstring in testing script is acceptable as otherwise there
    would be unnecessary repetition of information 

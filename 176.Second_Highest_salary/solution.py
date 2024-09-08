import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if len(employee) < 2:
        return pd.DataFrame(data=[None], columns=['SecondHighestSalary'])
    s = employee['salary']
    s = s[s != s.max()]
    if not len(s):
        return pd.DataFrame(data=[None], columns=['SecondHighestSalary'])
    return pd.DataFrame(data=[s.max()], columns=['SecondHighestSalary'])

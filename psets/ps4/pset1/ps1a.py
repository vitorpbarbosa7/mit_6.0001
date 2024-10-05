def solve_for_months(dream_house, annual_salary, pct_save_salary, r):

    A = dream_house*0.25
    P = (annual_salary/12)*pct_save_salary

    months = 0

    current_amount = 0

    while current_amount <= A:

        current_amount = (current_amount + P)*(1+(r/12))

        months += 1

    return months

if __name__ == '__main__':

    dream_houses = [1_000_000, 500_000]
    annual_salarys = [120_000, 80_000]
    pcts_save_salary = [0.1, 0.15]

    r = 0.04

    months = []

    for dream_house, annual_salary, pct_save_salary in zip(dream_houses, annual_salarys, pcts_save_salary):

        print(dream_house)
        print(annual_salary)
        print(pct_save_salary)
        
        months.append(solve_for_months(dream_house, annual_salary, pct_save_salary, r))

    print(months)


def solve_for_months(dream_house, 
                     annual_salary, 
                     pct_save_salary, 
                     semi_annual_raise, 
                     r):

    A = dream_house*0.25

    monthly_salary = annual_salary/12

    months = 1

    current_amount = 0

    while current_amount <= A:
        
        # modulo 6, mod6, remainder zero
        if months % 6 == 0:
            
            monthly_salary *= (1+semi_annual_raise)
            
        P = monthly_salary*pct_save_salary

        current_amount = (current_amount + P)*(1+(r/12))

        months += 1

        

    return months

if __name__ == '__main__':

    case1 = [120_000, 0.05, 500_000, 0.03]
    case2 = [80_000, 0.1, 800_000, 0.03]
    case3 = [75_000, 0.05, 1_500_000, 0.05]
    r = 0.04

    months = []

    for annual_salary, pct_save_salary, dream_house, semi_annual_raise in [case1,case2,case3]:

        months.append(solve_for_months(dream_house, annual_salary, pct_save_salary, semi_annual_raise, r))

    print(months)


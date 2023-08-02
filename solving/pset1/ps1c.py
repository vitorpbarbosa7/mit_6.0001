import contextlib

from math import log2

def suppress_print(suppress=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if suppress:
                # Redirect stdout to a dummy stream to suppress the print statements
                with contextlib.redirect_stdout(None):
                    return func(*args, **kwargs)
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@suppress_print(True)
def solve_for_months(dream_house, 
                     annual_salary, 
                     semi_annual_raise, 
                     r):

    A = dream_house*0.25

    eps = 100 # difference allowed between the actual down payment value (A) and the saved value

    bisect_iterations = 0

    MAX_SIGNIFICANT_DIGITS_FLOAT = 10000
    UPPER_BOUND_BISECT_SEARCH = log2(MAX_SIGNIFICANT_DIGITS_FLOAT)

    low = 0
    high = 1
    pct_save_salary = ((low + high) / 2)

    bisect_search_amount_saved = 0
    while abs(bisect_search_amount_saved - A) > eps and bisect_iterations < UPPER_BOUND_BISECT_SEARCH:

        # this will change in the bisect search procedure

        monthly_salary = annual_salary/12
        P = monthly_salary*pct_save_salary
        current_amount_saved = 0

        print('Needs to keep constant:')
        print('Necessary amount to save :', A)
        print('Monthly salary ', monthly_salary)
        print('------------\n')

        print('Must change:')
        print('P ', P)
        print('pct_value ', pct_save_salary)
        print('current amount saved ', bisect_search_amount_saved)
        print('-----------\n')

        # -------------
        months = 1
        while months <= 36:
        
            # modulo 6, mod6, remainder zero
            if months % 6 == 0:
                
                monthly_salary *= (1+semi_annual_raise)
                
            P = monthly_salary*pct_save_salary

            current_amount_saved = (current_amount_saved + P)*(1+(r/12))

            months += 1
        # -------------

        bisect_iterations += 1    

        if current_amount_saved > A:
            # set high standards to current high value which resulted in higher value than desired
            high = pct_save_salary
        else:
            # set low value to higher value since desired output was lower than expected
            low = pct_save_salary
        
        # update save salary percentage
        pct_save_salary = (low + high)/2

        bisect_search_amount_saved = current_amount_saved
        print(f'Amount saved after {bisect_iterations} bisect_iterations is : {bisect_search_amount_saved}\n\n')

        #breakpoint()

    return bisect_iterations, pct_save_salary, bisect_search_amount_saved

if __name__ == '__main__':

    r = 0.04

    HOUSE_PRICE = 1_000_000
    SEMI_ANNUAL_RAISE = 0.07

    case1 = [HOUSE_PRICE, SEMI_ANNUAL_RAISE, 150_000]
    case2 = [HOUSE_PRICE, SEMI_ANNUAL_RAISE, 300_000]
    case3 = [HOUSE_PRICE, SEMI_ANNUAL_RAISE, 10_000]

    res = []
    for dream_house, semi_annual_raise, annual_salary in [case1, case2, case3]:

        res.append(solve_for_months(dream_house, annual_salary, semi_annual_raise, r))

    [print(res, '\n\n') for res in res]


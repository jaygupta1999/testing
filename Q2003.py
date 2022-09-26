from test_framework import generic_test



 
# Returns no. of ways to
# reach sth stair
def q2003(top: int, maximum_step: int) -> int:
    res = [0] * (top + 2)
    res[0] = 1
    res[1] = 1
    res[2] = 2
 
    for i in range(3, top + 1):
        for j in range(1,maximum_step+1):
            res[i] += res[i - j] 
 
    return res[top]


if __name__ == "__main__":
    exit(generic_test.generic_test_main("Q2003.py", "Q2003.tsv", q2003))

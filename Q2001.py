from typing import List

from test_framework import generic_test


def q2001(paragraph: List[str]) -> int:
    # TODO - you fill in here.
    dict = {}
    for i in range (0,len(paragraph)):
        if paragraph[i] not in dict :
            for j in range(i,len(paragraph)):
                if paragraph[i] == paragraph[j] :
                    if paragraph[i] not in dict :
                        dict[paragraph[i]] = j - i 
                    else :
                        if dict[paragraph[i]] > j - i :
                            dict[paragraph[i]] = j - i 

            
    return min(dict.values())


if __name__ == "__main__":
    exit(generic_test.generic_test_main("Q2001.py", "Q2001.tsv", q2001))

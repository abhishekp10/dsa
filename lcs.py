"""
Function to determine longest common subsequence between given two strings
"""


def longest_comm_ss(a, b, na=0, nb=0):
    if na == len(a) or nb == len(b):
        return ""

    if a[na] == b[nb]:
        return a[na] + longest_comm_ss(a, b, na + 1, nb + 1)
    else:
        var_x = longest_comm_ss(a, b, na + 1, nb)
        var_y = longest_comm_ss(a, b, na, nb + 1)
        return max(var_x, var_y, key=len)


str1 = input("Enter first string?\n")
str2 = input("Enter second string?\n")

lcs = longest_comm_ss(str1, str2)
print(
    "longest common subsequence between str1 and str2 is ",
    lcs,
    " having length ",
    len(lcs),
)

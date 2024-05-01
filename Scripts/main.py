# main.py
print("////////1////////")
#1
def variant6(par2, par3, par1, var1=150):
    result = 89

    if result == var1:
        result += par3 + par1

        if result > 150 and par2 is True:
            if result > 250 and par2 is False:
                if result > 350:
                    return ">350"
                else:
                    result = result * 2
                    return result
            else:
                result = result * 3
                return result
        else:
            result = result * 2
            return result
    else:
        if var1 == 89:
            result = result * 2
            return result
        else:
            result = result * 3
            return result

print(variant6(False, 11, 20, 100))
print(variant6(False, 10, 20))
print(variant6(True, 11, 12, 100))
print(variant6(True, 10, 20))

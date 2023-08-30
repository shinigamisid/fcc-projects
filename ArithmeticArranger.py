def arithmetic_arranger(argument,ans_visibility = False):
    y = []
    z = []
    plusminus = []
    lenmax = []
    temp_arranged_problems = []
    arranged_problem_1 = []
    dashes = []
    final_ans = []
    ans = []
    if len(argument) > 5:
        return "Error: Too many problems."
    for ind_problem in argument:
        ind_ans = 0
        x = ind_problem.split()
        if x[1] not in ('+','-'):
            return "Error: Operator must be '+' or '-'."
        if len(x[0]) > 4 or len(x[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        lenmax.append(max(len(x[0]),len(x[2]))+2)
        y.append(x[0])
        plusminus.append(x[1])
        z.append(x[2])
        try:
            x[0] = int(x[0])
            x[2] = int(x[2])
        except:
            return "Error: Numbers must only contain digits."
        if x[1] == "+":
            ind_ans = x[0] + x[2]
        elif x[1] == "-":
            ind_ans = x[0] - x[2]
        ans.append(str(ind_ans))
    for i in range(len(z)):
        bottom = f"{plusminus[i]}{' ' * (lenmax[i]-len(z[i])-1)}{z[i]}"
        
        spaced_ans = f"{' ' * (lenmax[i]-len(ans[i]))}{ans[i]}"
        dash_single = '-' * (len(bottom))
        top = f"{' ' * (lenmax[i]-len(y[i]))}{y[i]}"
        
        dashes.append(dash_single)
        arranged_problem_1.append(top)
        temp_arranged_problems.append(bottom)
        final_ans.append(spaced_ans)
    a = "    ".join(arranged_problem_1)
    b = "    ".join(temp_arranged_problems)
    c = "    ".join(dashes)
    d = "    ".join(final_ans)
    if ans_visibility == True:
        arranged_problems = f"{a}\n{b}\n{c}\n{d}"
    else:
        arranged_problems = f"{a}\n{b}\n{c}"
    return arranged_problems

print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'],True))
print(arithmetic_arranger(['1 + 2', '1 - 9380'],True))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'],True))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'],True))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'],True))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'],True))


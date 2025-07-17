def cat_hat(str):
    cat_occurences = 0
    hat_occurences = 0
    for i in range(len(str) - 2):
        if str[i] == "c" and str[i+1] == "a" and str[i+2] == "t" :
            cat_occurences += 1
        elif str[i] == "h" and str[i+1] == "a" and str[i+2] == "t" :
            hat_occurences += 1
    if cat_occurences == hat_occurences:
        return True
    else:
        return False

a = [26,51,52,80,676,702,705]

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def excel_col(x):
    if x<26:
        return alpha[x-1]
    else:
        q,r = x//26, x%26
        if r==0:
            if q==1:
                return alpha[r-1]
            else:
                return excel_col(q-1) + alpha[r-1]
        else:
            return excel_col(q) + alpha[r-1]

for i in a:
    print(excel_col(i))
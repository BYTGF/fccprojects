import numpy as np

def calculate(list):

    if len(list) < 9:
        calculations = print("List must contain nine numbers")
    else:
        arrays = np.array(list)
        matrix = arrays.reshape(3, 3)
        
        meana1 = matrix.mean(0)
        meana2 = matrix.mean(1)
        meanf = matrix.mean()
        mean = [meana1.tolist(), meana2.tolist(), meanf.tolist()]
        
        vara1 = matrix.var(0)
        vara2 = matrix.var(1)
        varf = matrix.var()
        var = [vara1.tolist(), vara2.tolist(), varf.tolist()]
        
        stda1 = matrix.std(0)
        stda2 = matrix.std(1)
        stdf = matrix.std()
        std = [stda1.tolist(), stda2.tolist(), stdf.tolist()]
        
        maxa1 = matrix.max(0)
        maxa2 = matrix.max(1)
        maxf = matrix.max()
        max = [maxa1.tolist(), maxa2.tolist(), maxf.tolist()]
        
        mina1 = matrix.min(0)
        mina2 = matrix.min(1)
        minf = matrix.min()
        min = [mina1.tolist(), mina2.tolist(), minf.tolist()]
        
        suma1 = matrix.sum(0)
        suma2 = matrix.sum(1)
        sumf = matrix.sum()
        sum = [suma1.tolist(), suma2.tolist(), sumf.tolist()]

        calculations = f"'mean': {mean},\n 'variance': {var},\n 'standard deviation': {std},\n 'max': {max},\n 'min': {min},\n 'sum': {sum}"



    return calculations
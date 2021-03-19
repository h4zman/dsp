#https://www.askpython.com/python/array/print-an-array-in-python
#https://numpy.org/doc/1.19/reference/generated/numpy.convolve.html
#https://www.geeksforgeeks.org/timeit-python-examples/
#https://www.geeksforgeeks.org/append-extend-python/
#https://scilab.in/lab_migration/generate_lab/8/1



def my_convol(x, h):
    y = []
    m = len(x)
    n = len(h)

#i start from 0, while the given code in scilab i = 1
    for i in range(n + m - 1):
        mul_sum = 0
        for j in range(i + 1):
            if ((j < m) & (i - j < n)):
#1 in this loop, i-j is because else the array of x and h will multiply the same location array
#2 to save the mul_sum value when looping, it should be mul_sum = mul_sum + x[j] * h[i-j]
                mul_sum = mul_sum + x[j] * h[i - j]
#append mul_sum to add the array at the end of the y which is initially [null] but it will be fill when loop is completed
        y.append(mul_sum)
    return y








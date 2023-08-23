# Numpy Array Dimensions

https://youtu.be/BNAfVruKKkU?t=105

a 1D array in numpy
```
a = np.array([1, 2, 3])
# 1
print(np.ndim(a))
```

a 0 dimensional array
```
b = np.array(5)
# 0
print(np.ndim(b))
```


a list of lists is a 2D array...
```
a = [[1,2,3], [5,6,7], [8,9,10]]
A = np.array(a)
print(A)
# 2 
print(A.ndim)
```

a 3D array! 
```
b = [[[1,2], [3,4]], [[5,6], [7,8]], [[9,10], [11, 12]]]
B = np.array(b)
print(B)
print(B.ndim)
```

ok I think for that example, each inner list could represent the value for a given coordinate. 


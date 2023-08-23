# Overview

Xarray introduces labels in the form of dimensions, coordinates, and attributes on top 
of raw Numpy-like multidimensional arrays.

Multidimensionanl arrays are sometimes called tensors.  
NumPy provides support for ND arrays.  

Dimensions are labeled! So you can do things like this:
```
x.sum('time')
```
where you sum over the time intervals. 

You can select values by label! 
```
x.sel(time='2014-01-01')
```
or 
```
x.loc['2014-01-01']
```

Mathematical operations (e.g. `x - y`) vectorize across multiple dimensions (array 
broadcasting) based on dimension names, not shape.  

Easily use the `split-apply-combine` paradigm with `groupby`:
```
x.groupby('time.dayofyear').mean()
```


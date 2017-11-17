# mathnetwrapper
A thin (iron) python wrapper for [MathNet.Numerics](https://numerics.mathdotnet.com/api/)

## Usage:

Full MathNet.Numerics namespace available as MN

Example:
### Make a random 2x2 Matrix
```
import mathnetwrapper as mnw

x = mnw.matrix((2, 2), distribution=mnw.MN.Distributions.Normal())

print x
  DenseMatrix 2x2-Double
   0.308277 -0.47732
  -0.0486687 1.38952
```

### Make matrix from python list-of-lists, multiply by something random
```
a = [1, 2, 3, 4]
b = [a, a[::-1]]

c = mnw.matrix((2, 4), input_list=mnw.list_transpose_stack(b))

d = mnw.matrix((4, 3), distribution=mnw.MN.Distributions.Cauchy())

print c, d
  DenseMatrix 2x4-Double
  1 2 3 4
  4 3 2 1

  DenseMatrix 4x3-Double
  -0.310471 0.287797 -0.704258
  0.0676569 0.588943 -1.3042
   -3.50351 0.408381 2.23867
   3.62503 -1.40826 -0.569192

e = c.Multiply(d)  # c is .NET class, use DenseMatrix method .Multiply()

print e
  DenseMatrix 2x3-Double
   3.81443 -2.94222 1.12658
  -4.42091 2.32652 -2.82149
```

More to come...

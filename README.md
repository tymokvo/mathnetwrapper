# mathnetwrapper
A thin (iron) python wrapper for [MathNet.Numerics](https://numerics.mathdotnet.com/api/)

## Usage:

Full MathNet.Numerics namespace available as MN

Example:
```
import mathnetwrapper as mnw

x = mnw.matrix((2, 2), distribution=mnw.MN.Distributions.Normal())

print x
DenseMatrix 2x2-Double
 0.308277 -0.47732
-0.0486687 1.38952
```
More to come...

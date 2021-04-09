# hexifier
A hexifier module for Python 3+

# INSTALLATION

```
pip3 install git+https://github.com/9u3/hexifier/
```

# USAGE

```py
import hexifier
hexi = hexifier.hexifier()

print(hexi.rgbify("7FAA11")) # rgbify explicitly reqiures a string.
print(hexi.hexify((123,123,123))) # hexify explicity requires a tuple.
```

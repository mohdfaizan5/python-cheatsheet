# Regular Expressions:

    Regular expression(regexes) are used for validations and it is a pattern

instead of writing huge code for small cheching and validations
python has _re_ library


```python
import re
re.search(pattern, string, flags=0)
```

| Symbols | Feature |
|---|---|
|. |any charactor except a newline|
|*|0 or more repetitions|
|+|1 or more repetitions|
|?|0 or 1 repetitions|
|{n}| n repetitions |
|{n,m}|n-m repetitions|


```python
import re

em = "a@"

if re.search(".+@.+", em):
    print("valid")
else:
    print("Invalid")
```

Other re

|Symbol|Function of symbol|
|---|---|
|^(carrot symbol)|matches the start of the string|
|$|matches the end of the string just before the new line at the end of the string|

If we want specific charactor
|Symbol|Function of symbol|
|---|---|
|[ ]|  set of charactors|

|Symbol|Function of symbol|
|---|---|
|[^]|  Complementing the set|

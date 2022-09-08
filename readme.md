# 0xAnsi  <img width="60px" src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif">

A handy package to use ansi escape sequences without having to know all possible sequences by heart

# Installation :

From pip :

```bash
pip3 install oxansi
```

From source :

```bash
git clone https://github.com/0x68616469/oxansi/
```

# Example :

```python
from oxansi import Long as ansi

# Print "/!\ ERROR : " in red
print(f"{ansi.red}/!\\ ERROR : {ansi.reset}404 Not found")

# Print "Hello World" in cyan with white background
print(f"{ansi.background.white}{ansi.cyan}Hello World")
```

<hr>

![Follow me](https://img.shields.io/badge/-Follow%20Me-222222?logo=twitter&logoColor=black&color=272838&labelColor=C09891&style=for-the-badge&logoWidth=30&link=https://twitter.com/0x68616469)

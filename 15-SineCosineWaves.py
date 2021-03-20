import numpy as np
from matplotlib import pyplot as plt
from fractions import Fraction as frac
from matplotlib.ticker import FuncFormatter, MultipleLocator

def pi_axis_formatter(val, pos, denomlim=10, pi=r'\pi'):
    """
    format label properly
    for example: 0.6666 pi --> 2π/3
               : 0      pi --> 0
               : 0.50   pi --> π/2
    """
    minus = "-" if val < 0 else ""
    val = abs(val)
    ratio = frac(val / np.pi).limit_denominator(denomlim)
    n, d = ratio.numerator, ratio.denominator

    fmt2 = "%s" % d
    if n == 0:
        fmt1 = "0"
    elif n == 1:
        fmt1 = pi
    else:
        fmt1 = r"%s%s" % (n, pi)

    fmtstring = "$" + minus + (fmt1 if d == 1 else r"{%s}/{%s}" % (fmt1, fmt2)) + "$"

    return fmtstring


x = np.arange(-5, 5, 0.01)

fig, ax = plt.subplots()

# making the top and right spine invisible:
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# moving bottom spine up to y=0 position:
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
# moving left spine to the right to position x == 0:
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


ax.plot(x, np.sin(x))
ax.plot(x, -np.cos(x))
ax.plot(x, -np.sin(x))

plt.title('Wave Function')

ax.set_ylabel('f(x)', loc='top')
ax.set_xlabel('x', loc='right')
ax.legend([' Sin(x)', '- Cos(x)', '- Sin(x)'], bbox_to_anchor=(1.05, 1.0), loc='upper right')
# plt.grid(True)

ticklen = np.pi/2

# setting ticks labels
ax.xaxis.set_major_formatter(FuncFormatter(pi_axis_formatter))
# setting ticks at proper numbers
ax.xaxis.set_major_locator(MultipleLocator(base=ticklen))

plt.show()

plt.savefig('15-SinCosWave.png',
            dpi=300,
            format='png')

####################################################################
#           ______________________________________         
#  ________|                OxAnsi                |_______
#  \       |                                      |      /
#   \      |              @0x68616469             |     /
#   /      |______________________________________|     \
#  /__________)                                (_________\
#
# A Handy Python library to Use ANSI Escape Sequences
#
# Github repo : https://github.com/0x68616469/oxansi
#
####################################################################

### Long version, easier to remember but longer to type.

class Long:

    ## Text rendering

    reset = '\033[0m'
    bold = '\033[1m'
    faint = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    slow_blink = '\033[5m'
    fast_blink = '\033[6m'
    reverse = '\033[7m'
    conceal = '\033[8m'
    crossed_out = '\033[9m'
    default = '\033[10m'
    fraktur = '\033[20m'
    

    ## Foreground colors
      
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'

    class bright:

        black = '\033[90m'
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        blue = '\033[94m'
        magenta = '\033[95m'
        cyan = '\033[96m'
        white = '\033[97m'


    ## Background colors

    class background:

        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        yellow = '\033[43m'
        blue = '\033[44m'
        magenta = '\033[45m'
        cyan = '\033[46m'
        white = '\033[47m'   
    
        class bright:
            black = '\033[100m'
            red = '\033[101m'
            green = '\033[102m'
            yellow = '\033[103m'
            blue = '\033[104m'
            magenta = '\033[105m'
            cyan = '\033[106m'
            white = '\033[107m'  


    ## Control the screen

    clear = '\033[2J'
    clear_line = '\033[2K'
    clear_to_end_line = '\033[K'
    

    ## Controlling the Cursor

    save = '\033[s'  # Save cursor position
    restore = '\033[u'  # Restore cursor position
    
    def move(l,c): return f'\033[{l};{c}H'  # Move cursor to l (line) c (column)
    def move_up(n): return f'\033[{n}A'  # Move up n lines
    def move_down(n): return f'\033[{n}B'  # Move down n lines
    def move_forward(n): return f'\033[{n}C'   # Move forward n columns
    def move_backward(n): return f'\033[{n}D'  # Move backward n columns


### Short version, faster to type but harder to remember

class Short:

    ## Text rendering

    rst = '\033[0m' # reset
    bld = '\033[1m' # bold
    fnt = '\033[2m' # faint
    itc = '\033[3m' # italic
    udr = '\033[4m' # underline
    sbk = '\033[5m' # slow blink
    rbk = '\033[6m' # rapid blink
    rvs = '\033[7m' # reverse
    con = '\033[8m' # conceal
    crs = '\033[9m' # crossed out
    dft = '\033[10m' # default
    fra = '\033[20m' # fraktur
    

    ## Foreground colors
      
    b = '\033[30m' # black
    r = '\033[31m' # red
    g = '\033[32m' # green
    y = '\033[33m' # yellow
    bl = '\033[34m' # blue
    m = '\033[35m' # magenta
    c = '\033[36m' # cyan
    w = '\033[37m' # white

    class br:

        b = '\033[90m' # black
        r = '\033[91m' # red
        g = '\033[92m' # green
        y = '\033[93m' # yellow
        bl = '\033[94m' # blue
        m = '\033[95m' # magenta
        c = '\033[96m' # cyan
        w = '\033[97m' # white


    ## Background colors

    class bck:

        b = '\033[40m' # black
        r = '\033[41m' # red
        g = '\033[42m' # green
        y = '\033[43m' # yellow
        bl = '\033[44m' # blue
        m = '\033[45m' # magenta
        c = '\033[46m' # cyan
        w = '\033[47m' # white    
    
        class br: # bright
            b = '\033[100m' # black
            r = '\033[101m' # red
            g = '\033[102m' # green
            y = '\033[103m' # yellow
            bl = '\033[104m' # blue
            m = '\033[105m' # magenta
            c = '\033[106m' # cyan
            w = '\033[107m' # white


    ## Control the screen

    clr = '\033[2J'
    cll = '\033[2K'
    cel = '\033[K'
    

    ## Controlling the Cursor

    sc = '\033[s'  # Save cursor position
    rc = '\033[u'  # Restore cursor position
    
    def mv(l,c): return f'\033[{l};{c}H'  # Move cursor to l (line) c (column)
    def mu(n): return f'\033[{n}A'  # Move up n lines
    def md(n): return f'\033[{n}B'  # Move down n lines
    def mf(n): return f'\033[{n}C'   # Move forward n columns
    def mb(n): return f'\033[{n}D'  # Move backward n columns
# Python '42

Top down scroller test in Python and Pygame.

![example](https://github.com/madeinouweland/python-42/blob/main/example.gif)

[View it on youtube](https://www.youtube.com/shorts/ykTty3RcjdU)

usage:
- create and activate venv
- pip install pygame
- python isla.py

## How does it work?

The graphics are 64x64 bitmaps like this:

![insel1.png](https://github.com/madeinouweland/python-42/blob/main/insel1.png)
![inselc.png](https://github.com/madeinouweland/python-42/blob/main/inselc.png)
![inselv.png](https://github.com/madeinouweland/python-42/blob/main/inselv.png)
![inselx.png](https://github.com/madeinouweland/python-42/blob/main/inselx.png)
![insely.png](https://github.com/madeinouweland/python-42/blob/main/insely.png)

And a plane:

![plane.png](https://github.com/madeinouweland/python-42/blob/main/plane.png)

The graphics are mapped on cells according to this data:

```
..........
.......3..
oo.2......
11r...2...
111r......
uur...3...
.......2..
....3...lo
......l1v1
..23...luu
.
.
```

10 rows of data are shown on the screen and each requested frame, the y-offset is incremented. When 64 pixels have passed, y-offset is reset and the data file is shifted down

```
    if yy > 64:
        yy = yy - 64
        mapdata.map = [mapdata.map[-1]] + mapdata.map[0:-1]  # shift map down
```

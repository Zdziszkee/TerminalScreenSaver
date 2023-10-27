import curses


def main():
    stdscr = curses.initscr()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    height, width = stdscr.getmaxyx()
    y, x = height // 2, width // 2
    vy, vx = 1, 1
    text = "Hello world"

    while True:
        stdscr.clear()
        stdscr.addstr(y, x, text)

        stdscr.refresh()
        key = stdscr.getch()

        if y + vy >= height - 1 or y + vy <= 0:
            vy = -vy
        if x + vx >= width - len(text) or x + vx <= 0:
            vx = -vx

        y += vy
        x += vx

        if key == ord('q'):
            break
main()
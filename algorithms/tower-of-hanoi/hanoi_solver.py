import turtle
import time


class HanoiVisualizer:
    def __init__(self, n, disk_delay=0.3):
        self.n = n
        self.delay = disk_delay

        self.rod_positions = [-250, 0, 250]
        self.rod_height = 200
        self.min_width = 40   # smallest disk width in px
        self.max_width = 180  # largest disk width in px
        self.disk_h = 24      # fixed disk height in px

        self.screen = turtle.Screen()
        self.screen.bgcolor("#1e1e2f")
        self.screen.title(f"Tower of Hanoi Visualizer ({n} Disks)")
        self.screen.setup(width=900, height=600)
        self.screen.tracer(0)

        self._draw_base_and_rods()
        self.status_writer = self._make_status_writer()

        self.disk_turtles = []
        self._create_disks()

        self.move_count = 0
        self.total_moves = 2 ** n - 1

        self.screen.update()
        time.sleep(1)

    def _draw_base_and_rods(self):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.color("#e0e0e0")
        pen.pensize(4)
        pen.penup()
        pen.goto(-330, -120)
        pen.pendown()
        pen.goto(330, -120)
        for x in self.rod_positions:
            pen.penup()
            pen.goto(x, -120)
            pen.pendown()
            pen.goto(x, -120 + self.rod_height)

    def _make_status_writer(self):
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.color("#f5f5f5")
        writer.goto(0, 220)
        return writer

    def _disk_width(self, i):
        """Width scales between min_width and max_width based on disk rank,
        completely independent of n — this is the bug that was making disks
        blow up to 300+ px wide."""
        if self.n == 1:
            return self.max_width
        frac = (i - 1) / (self.n - 1)
        return self.min_width + frac * (self.max_width - self.min_width)

    def _create_disks(self):
        palette = ["#FF6B6B", "#FFA94D", "#FFD93D", "#6BCB77",
                   "#4D96FF", "#9D4EDD", "#F15BB5", "#00C2A8"]
        for i in range(self.n, 0, -1):
            t = turtle.Turtle()
            t.shape("square")
            t.penup()
            t.shapesize(stretch_wid=self.disk_h / 20,
                        stretch_len=self._disk_width(i) / 20)
            t.color(palette[(i - 1) % len(palette)])
            t.pencolor("#1e1e2f")

            label = turtle.Turtle()
            label.hideturtle()
            label.penup()
            label.color("#1e1e2f")

            self.disk_turtles.append((i, t, label))

    def _disk_y(self, stack_pos):
        return -120 + 12 + stack_pos * (self.disk_h + 4)

    def update_visuals(self, rods, move_desc=""):
        if move_desc:
            self.move_count += 1

        for rod_idx, rod_content in enumerate(rods):
            x = self.rod_positions[rod_idx]
            for stack_pos, disk_val in enumerate(rod_content):
                for val, t, label in self.disk_turtles:
                    if val == disk_val:
                        y = self._disk_y(stack_pos)
                        self._animate_move(t, label, x, y, val)
                        break

        if move_desc:
            self.status_writer.clear()
            self.status_writer.write(
                f"Move {self.move_count}/{self.total_moves}:  {move_desc}",
                align="center", font=("Arial", 14, "bold"))

        self.screen.update()
        time.sleep(self.delay)

    def _animate_move(self, t, label, target_x, target_y, disk_val, steps=8):
        start_x, start_y = t.xcor(), t.ycor()
        if (round(start_x), round(start_y)) == (round(target_x), round(target_y)):
            label.clear()
            label.goto(target_x, target_y - 6)
            label.write(str(disk_val), align="center", font=("Arial", 10, "bold"))
            return
        for step in range(1, steps + 1):
            nx = start_x + (target_x - start_x) * step / steps
            ny = start_y + (target_y - start_y) * step / steps
            t.goto(nx, ny)
            label.clear()
            label.goto(nx, ny - 6)
            label.write(str(disk_val), align="center", font=("Arial", 10, "bold"))
            self.screen.update()

    def finish(self):
        self.status_writer.clear()
        self.status_writer.write(
            f"Solved in {self.total_moves} moves!",
            align="center", font=("Arial", 16, "bold"))
        self.screen.update()

    def close(self):
        self.screen.mainloop()


def hanoi_solver_visualized(n, delay=0.3):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []
    rod_names = ['A', 'B', 'C']

    viz = HanoiVisualizer(n, disk_delay=delay)
    moves.append(format_state(rods))
    viz.update_visuals(rods)

    def move_disks(count, source, destination, auxiliary):
        if count == 0:
            return

        move_disks(count - 1, source, auxiliary, destination)

        disk = rods[source].pop()
        rods[destination].append(disk)

        moves.append(format_state(rods))
        desc = f"Disk {disk}: {rod_names[source]} -> {rod_names[destination]}"
        viz.update_visuals(rods, move_desc=desc)

        move_disks(count - 1, auxiliary, destination, source)

    move_disks(n, 0, 2, 1)
    viz.finish()

    print("\n--- Solver Completed ---")
    print(f"Total moves required: {2**n - 1}")
    print("\nMove History:")
    print('\n'.join(moves))

    time.sleep(1.5)
    viz.close()


def format_state(rods):
    return ' '.join(str(rod) for rod in rods)


if __name__ == '__main__':
    while True:
        try:
            num_disks = int(input("Enter number of disks (e.g., 3-8): "))
            if num_disks > 0:
                break
            print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    print("\nSelect animation delay (seconds per move):")
    try:
        speed_input = float(input("Enter delay in seconds [Default: 0.3]: ") or 0.3)
    except ValueError:
        speed_input = 0.3

    print(f"\nStarting Hanoi Solver for {num_disks} disks...")
    hanoi_solver_visualized(num_disks, delay=speed_input)
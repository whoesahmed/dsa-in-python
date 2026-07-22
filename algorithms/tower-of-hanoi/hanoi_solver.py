import turtle
import time

class HanoiVisualizer:
    def __init__(self, n, disk_delay=0.3):
        self.n = n
        self.delay = disk_delay
        
        # Screen Setup
        self.screen = turtle.Screen()
        self.screen.title(f"Tower of Hanoi Visualizer ({n} Disks)")
        self.screen.setup(width=800, height=500)
        self.screen.tracer(0)  # Turn off auto-animation for crisp redrawing
        
        # Rod X Positions
        self.rod_positions = [-250, 0, 250]
        self.rod_height = 200
        
        self._draw_base_and_rods()
        
        # Create visual disk turtle objects
        self.disk_turtles = []
        self._create_disks()
        
        self.screen.update()
        time.sleep(1)  # Brief pause before solver starts moving

    def _draw_base_and_rods(self):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.penup()
        
        # Base line
        pen.goto(-350, -100)
        pen.pendown()
        pen.goto(350, -100)
        
        # 3 vertical rods
        for x in self.rod_positions:
            pen.penup()
            pen.goto(x, -100)
            pen.pendown()
            pen.goto(x, -100 + self.rod_height)

    def _create_disks(self):
        """Creates dynamic rectangular disk objects sized proportionally."""
        for i in range(self.n, 0, -1):
            t = turtle.Turtle()
            t.shape("square")
            t.penup()
            
            # Adjust disk widths based on how many disks there are
            width_stretch = (i * (15 / max(self.n, 1))) + 0.8
            t.shapesize(stretch_wid=1, stretch_len=width_stretch)
            
            colors = ["#E74C3C", "#3498DB", "#2ECC71", "#F1C40F", "#9B59B6", "#E67E22"]
            t.color(colors[(i - 1) % len(colors)])
            
            self.disk_turtles.append((i, t))

    def update_visuals(self, rods):
        """Redraws disk positions whenever a rod array state changes."""
        for rod_idx, rod_content in enumerate(rods):
            x = self.rod_positions[rod_idx]
            
            for stack_pos, disk_val in enumerate(rod_content):
                for val, t in self.disk_turtles:
                    if val == disk_val:
                        y = -90 + (stack_pos * 22)
                        t.goto(x, y)
                        break
                        
        self.screen.update()
        time.sleep(self.delay)

    def close(self):
        self.screen.mainloop()


def hanoi_solver_visualized(n, delay=0.3):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    viz = HanoiVisualizer(n, disk_delay=delay)
    
    # Record and display initial state
    moves.append(format_state(rods))
    viz.update_visuals(rods)

    def move_disks(count, source, destination, auxiliary):
        if count == 0:
            return

        move_disks(count - 1, source, auxiliary, destination)

        # Move disk logic
        disk = rods[source].pop()
        rods[destination].append(disk)
        
        moves.append(format_state(rods))
        viz.update_visuals(rods)

        move_disks(count - 1, auxiliary, destination, source)

    move_disks(n, 0, 2, 1)
    
    print("\n--- Solver Completed ---")
    print(f"Total moves required: {2**n - 1}")
    print("\nMove History:")
    print('\n'.join(moves))
    
    viz.close()


def format_state(rods):
    return ' '.join(str(rod) for rod in rods)


if __name__ == '__main__':
    # Input handling with basic validation
    while True:
        try:
            num_disks = int(input("Enter number of disks (e.g., 3-8): "))
            if num_disks > 0:
                break
            print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # Speed selection
    print("\nSelect animation delay (seconds per move):")
    try:
        speed_input = float(input("Enter delay in seconds [Default: 0.3]: ") or 0.3)
    except ValueError:
        speed_input = 0.3

    print(f"\nStarting Hanoi Solver for {num_disks} disks...")
    hanoi_solver_visualized(num_disks, delay=speed_input)
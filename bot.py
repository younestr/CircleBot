import pyautogui
import time
import math
import keyboard

screen_width, screen_height = pyautogui.size()
base_center_x = screen_width // 2
base_center_y = screen_height // 2 - 20

print(f"✅ Using base center at ({base_center_x}, {base_center_y})")

def safe_move(x, y):
    x = min(max(0, int(x)), screen_width - 1)
    y = min(max(0, int(y)), screen_height - 1)
    pyautogui.moveTo(x, y, _pause=False)

def draw_perfect_circle_like_js():
    # Parameters inspired by the JS snippet
    radius = screen_width // 3
    steps = 50
    arc_step = math.acos(1 - (60 ** 2) / (2 * radius ** 2))  # step angle based on chord length = 60px

    center_x = base_center_x
    center_y = base_center_y

    angle = 0
    print(f"🚀 Drawing perfect JS-style circle (r={radius}, steps={steps})...")

    # Compute first point
    x = round(center_x + radius * math.cos(angle))
    y = round(center_y + radius * math.sin(angle))
    safe_move(x, y)
    pyautogui.mouseDown()
    safe_move(x, y)

    # Draw points around the circle
    for _ in range(steps):
        angle += arc_step
        x = round(center_x + radius * math.cos(angle))
        y = round(center_y + radius * math.sin(angle))

        safe_move(x, y)
        time.sleep(0.002)

    pyautogui.mouseUp()
    print("✅ Perfect circle complete.\n")

print("🎮 Press 's' for perfect JS-style circle, 'm' for infinite imperfect loops, 'e' to exit.")

def draw_random_circle():
    import random
    radius = random.randint(250, 310)
    steps = random.randint(40, 600)
    jitter_amplitude = random.uniform(0.8, 2.5)
    draw_delay = random.uniform(0.0006, 0.0015)

    center_x = base_center_x + random.randint(-3, 3)
    center_y = base_center_y + random.randint(-3, 3)

    start_x = center_x + radius
    start_y = center_y

    print(f"🚀 Drawing shape (r={radius}, steps={steps}, jitter={jitter_amplitude:.2f})...")
    safe_move(start_x, start_y)
    pyautogui.mouseDown()
    safe_move(start_x + 1, start_y + 1)
    safe_move(start_x, start_y)

    for i in range(steps + 1):
        if keyboard.is_pressed("e"):
            print("⛔ Interrupted by 'e' — stopping drawing.")
            pyautogui.mouseUp()
            return

        angle = 2 * math.pi * i / steps
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        x += random.uniform(-jitter_amplitude, jitter_amplitude)
        y += random.uniform(-jitter_amplitude, jitter_amplitude)
        safe_move(x, y)
        time.sleep(draw_delay)

    pyautogui.mouseUp()
    print("✅ Shape complete.\n")

# Main loop
while True:
    if keyboard.is_pressed("e"):
        print("👋 Exiting.")
        break
    elif keyboard.is_pressed("s"):
        draw_perfect_circle_like_js()
        while keyboard.is_pressed("s"):
            time.sleep(0.1)
    elif keyboard.is_pressed("m"):
        print("🔁 Infinite random mode (press 'e' to stop)...")
        while True:
            draw_random_circle()
            if keyboard.is_pressed("e"):
                print("👋 Exiting infinite mode.")
                break
                
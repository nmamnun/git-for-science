import numpy as np
from pendulum_equations import get_period, max_height, max_speed, check_small_angle, bpm

def main():
    length = 1.0         # meters
    theta = np.pi / 6    # 30 degrees in radians

    print(f"Pendulum length: {length} m")
    print(f"Initial angle: {theta:.3f} radians ({np.degrees(theta):.1f} degrees)")

    period = get_period(length)
    print(f"Period: {period:.4f} s")

    height = max_height(length, theta)
    print(f"Maximum height: {height:.4f} m")

    speed = max_speed(length, theta)
    print(f"Maximum speed: {speed:.4f} m/s")

    is_small = check_small_angle(theta)
    print(f"Small angle approximation valid? {is_small}")

    bpm_value = bpm(length)
    print(f"Beats per minute: {bpm_value:.2f}")

if __name__ == "__main__":
    main()

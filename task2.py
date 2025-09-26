import argparse
import matplotlib.pyplot as plt
import math


def draw_tree(ax, x, y, length, angle, depth, split_angle=math.pi/4):
    if depth == 0 or length <= 0:
        return

    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)

    ax.plot([x, x2], [y, y2], color='brown')

    if depth == 1:
        return

    left_branch_length = length * math.cos(split_angle)
    right_branch_length = length * math.sin(split_angle)

    left_branch_angle = angle + split_angle
    right_branch_angle = angle - (math.pi / 2 - split_angle)

    draw_tree(ax, x2, y2, left_branch_length,
              left_branch_angle, depth - 1, split_angle)
    draw_tree(ax, x2, y2, right_branch_length,
              right_branch_angle, depth - 1, split_angle)


def main():
    parser = argparse.ArgumentParser(
        description="Pythagorean tree fractal generator."
    )
    parser.add_argument(
        "-d", "--depth", type=int, default=10,
        help="Recursion depth (1-15, default 10)"
    )
    parser.add_argument(
        "-a", "--angle", type=float, default=45.0,
        help="split angle in degrees (0-90, default 45.0)"
    )
    parser.add_argument(
        "--length", type=float, default=1.2,
        help="initial branch length (default 1.2)"
    )

    args = parser.parse_args()

    if not (0.0 < args.angle < 90.0):
        raise SystemExit(
            "Error: angle must be in (0, 90) degrees range.")

    split_angle = math.radians(args.angle)

    fig, ax = plt.subplots(figsize=(8, 8))

    start_x, start_y = 0.0, -1.0
    start_angle = math.pi / 2  # 90° (вгору)

    draw_tree(ax, start_x, start_y, args.length,
              start_angle, args.depth, split_angle)

    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    plt.show()


if __name__ == "__main__":
    main()

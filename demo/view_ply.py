"""Simple local viewer for .ply point clouds exported from the demos.

Usage:
    python view_ply.py pca.ply
    python view_ply.py pc.ply pca.ply    # view multiple side-by-side in one window
"""

import argparse
import sys

import open3d as o3d


def main():
    parser = argparse.ArgumentParser(description="View one or more .ply point clouds.")
    parser.add_argument("paths", nargs="+", help="Path(s) to .ply file(s).")
    parser.add_argument(
        "--offset",
        type=float,
        default=0.0,
        help="X-axis offset between successive clouds (useful when viewing several at once).",
    )
    args = parser.parse_args()

    geometries = []
    for i, path in enumerate(args.paths):
        pcd = o3d.io.read_point_cloud(path)
        if len(pcd.points) == 0:
            print(f"Warning: {path} has no points", file=sys.stderr)
            continue
        if args.offset and i > 0:
            pcd.translate((args.offset * i, 0.0, 0.0))
        print(f"Loaded {path}: {len(pcd.points)} points")
        geometries.append(pcd)

    if not geometries:
        sys.exit("No point clouds to show.")

    o3d.visualization.draw_geometries(geometries)


if __name__ == "__main__":
    main()

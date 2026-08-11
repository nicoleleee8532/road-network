from __future__ import annotations

import argparse
from pathlib import Path

from src.pipeline import Config, TDriveProject


def main() -> None:
    parser = argparse.ArgumentParser(description="T-Drive project pipeline")
    parser.add_argument("--data_dir", type=str, default="data", help="Folder containing raw T-Drive .txt files")
    parser.add_argument("--output_dir", type=str, default="output", help="Folder to save outputs")
    parser.add_argument("--sample_files", type=int, default=None, help="Only use the first N files for quick testing")
    parser.add_argument("--time_gap_minutes", type=int, default=30)
    parser.add_argument("--min_trip_points", type=int, default=3)
    parser.add_argument("--min_trip_distance_km", type=float, default=0.5)
    parser.add_argument("--min_trip_duration_minutes", type=float, default=5.0)
    args = parser.parse_args()

    config = Config(
        time_gap_minutes=args.time_gap_minutes,
        min_trip_points=args.min_trip_points,
        min_trip_distance_km=args.min_trip_distance_km,
        min_trip_duration_minutes=args.min_trip_duration_minutes,
    )
    project = TDriveProject(config=config)
    project.execute(
        data_dir=Path(args.data_dir),
        output_dir=Path(args.output_dir),
        sample_files=args.sample_files,
    )
    print("Done. Check the output folder for CSV files, charts, and model results.")


if __name__ == "__main__":
    main()

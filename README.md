# T-Drive Group Project Full Version

## Project title
Urban Taxi Trajectory Analysis and Trip Pattern Discovery Using the T-Drive Dataset

## What this project does
This project reads raw T-Drive taxi trajectory `.txt` files, cleans the GPS records, splits the trajectory into trips, performs exploratory data analysis, and trains simple machine learning models to predict trip duration.

## Dataset format
Each raw file should look like this:

```text
1,2008-02-02 15:36:08,116.51172,39.92123
```

Each line contains:
- taxi id
- date time
- longitude
- latitude

## Project folder structure

```text
project/
├── data/
├── output/
├── src/
├── run_all.py
├── requirements.txt
└── README.md
```

## Step-by-step running guide

### 1. Put the raw files into the data folder
Copy many T-Drive `.txt` files into:

```text
data/
```

### 2. Open terminal in the project folder
Make sure you are inside the folder that contains `run_all.py`.

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate it on Windows

```bash
.venv\Scripts\activate
```

### 5. Install packages

```bash
pip install -r requirements.txt
```

### 6. Run the full pipeline

```bash
python run_all.py --data_dir data --output_dir output
```

### 7. Quick test on only part of the data

```bash
python run_all.py --data_dir data --output_dir output --sample_files 100
```

## Main output files
After running, check the `output` folder.

You should see files such as:
- `dataset_summary.csv`
- `dataset_summary.json`
- `clean_points_preview.csv`
- `trip_level_table.csv`
- `top_hotspots.csv`
- `hourly_trip_counts.png`
- `weekday_weekend_trip_counts.png`
- `trip_distance_histogram.png`
- `trip_duration_histogram.png`
- `gps_point_distribution.png`
- `model_metrics.csv`
- `prediction_vs_actual.png`

## Suggested report writing flow
1. Explain the problem and motivation.
2. Introduce the T-Drive dataset.
3. Describe preprocessing and trip extraction rules.
4. Show temporal and spatial EDA results.
5. Explain the prediction task and models.
6. Compare model results with MAE, RMSE, and R².
7. Summarize findings and future work.

## Notes
- Duplicate rows are removed.
- Out-of-range Beijing coordinates are removed.
- Very unrealistic segments are filtered using speed.
- Trips are split using a time-gap threshold.
- Very short or trivial trips are removed.


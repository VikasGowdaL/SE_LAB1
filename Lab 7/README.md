# Lab 7 — Fuzz Testing: Train Fare

## Objective
Identify and fix input-validation crashes using Hypothesis property-based fuzz testing.

## Files
- `train_fare.py`: Hardened train PNR, distance, and berth utilities.
- `test_train_fare.py`: Three Hypothesis fuzz tests for crash resistance.
- `Lab7_Fuzz_Testing_Report.pdf`: Screenshots of original run, failing tests, fixed run, and passing tests (add the PDF separately).

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest hypothesis
```

## Run
```bash
python train_fare.py
python -m pytest test_train_fare.py -v
```

## Results
Before fixes: **3 failed**. After fixes: **3 passed** (user-provided terminal screenshots, November 12, 2026).

Malformed inputs return `None` instead of raising exceptions. Valid sample inputs preserve original output. Tests cover crash resistance, not all business rules.

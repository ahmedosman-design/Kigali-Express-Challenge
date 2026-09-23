# Kigali Express — Driver Lookup Optimization

## Team
- Ahmed Osman
- Junior Nyamu

## The Problem
A fast food delivery app in Kigali has 10,000 drivers stored in a list. Every customer request scans the list sequentially to find a driver, causing high latency as the app scales — an O(N) search.

## The Solution
We converted the raw list of driver objects into a dictionary keyed by `driver_id`, turning lookups into an O(1) operation — a direct lookup instead of a scan.

## Files
- `kigali_express.py` — generates sample driver data, builds the driver dictionary, and defines both the old (linear) and new (instant) lookup functions
- `drivers.json` — sample dataset of 10,000 generated drivers
- `test.py` — measures and compares lookup speed between the two approaches

## Results
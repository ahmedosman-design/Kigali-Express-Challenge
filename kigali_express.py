import json
import random
import time

def generate_drivers(n=10000):
    drivers = []
    for i in range(n):
        drivers.append({
            "driver_id": f"KGL-{i:05d}",
            "name": f"Driver_{i}",
            "rating": round(random.uniform(3.5, 5.0), 1),
        })
    return drivers

def save_drivers_to_json(drivers, filename="drivers.json"):
    with open(filename, "w") as f:
        json.dump(drivers, f, indent=2)

def load_drivers_from_json(filename="drivers.json"):
    with open(filename, "r") as f:
        return json.load(f)

def build_driver_map(drivers):
    driver_map = {}
    for driver in drivers:
        driver_map[driver["driver_id"]] = driver
    return driver_map

def find_driver_linear(drivers, target_id):
    for driver in drivers:
        if driver["driver_id"] == target_id:
            return driver
    return None

def find_driver_instant(driver_map, target_id):
    return driver_map.get(target_id)

def verify_lookups_match(drivers, driver_map, target_id):
    """Sanity check: both lookup methods must return the same driver
    before we trust any speed comparison between them."""
    linear_result = find_driver_linear(drivers, target_id)
    instant_result = find_driver_instant(driver_map, target_id)
    assert linear_result == instant_result, "Lookup methods disagree on result!"

def benchmark_lookups(drivers, driver_map, target_id, runs=1000):
    """Time both lookup approaches averaged over `runs` calls, verify
    they agree, and return (linear_time, instant_time) in seconds."""
    verify_lookups_match(drivers, driver_map, target_id)

    start = time.perf_counter()
    for _ in range(runs):
        find_driver_linear(drivers, target_id)
    linear_time = (time.perf_counter() - start) / runs

    start = time.perf_counter()
    for _ in range(runs):
        find_driver_instant(driver_map, target_id)
    instant_time = (time.perf_counter() - start) / runs

    return linear_time, instant_time

if __name__ == "__main__":
    drivers_list = generate_drivers(10000)
    save_drivers_to_json(drivers_list)
    driver_map = build_driver_map(drivers_list)

    target_id = "KGL-09999"
    linear_time, instant_time = benchmark_lookups(drivers_list, driver_map, target_id)

    print(f"Linear scan:  {linear_time*1e6:.2f} µs")
    print(f"Dict lookup:  {instant_time*1e6:.2f} µs")
    print(f"Speedup:      {linear_time/instant_time:,.0f}x faster")
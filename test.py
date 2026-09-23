import time
from kigali_express import (
    generate_drivers,
    build_driver_map,
    find_driver_linear,
    find_driver_instant,
)

# Set up test data
drivers_list = generate_drivers(10000)
driver_map = build_driver_map(drivers_list)
target_id = "KGL-09999"  # worst case: last driver in the list

# Time the old O(N) approach
start = time.perf_counter()
find_driver_linear(drivers_list, target_id)
linear_time = time.perf_counter() - start

# Time the new O(1) approach
start = time.perf_counter()
find_driver_instant(driver_map, target_id)
instant_time = time.perf_counter() - start

# Report results
print(f"Linear scan (O(N)):  {linear_time*1e6:.2f} µs")
print(f"Dict lookup (O(1)):  {instant_time*1e6:.2f} µs")
print(f"Speedup:              {linear_time/instant_time:,.0f}x faster")
from kigali_express import generate_drivers, build_driver_map, benchmark_lookups

# Set up test data
drivers_list = generate_drivers(10000)
driver_map = build_driver_map(drivers_list)
target_id = "KGL-09999"  # worst case: last driver in the list

# Run the shared benchmark (also verifies both methods agree)
linear_time, instant_time = benchmark_lookups(drivers_list, driver_map, target_id)

# Report results
print(f"Linear scan (O(N)):  {linear_time*1e6:.2f} µs")
print(f"Dict lookup (O(1)):  {instant_time*1e6:.2f} µs")
print(f"Speedup:              {linear_time/instant_time:,.0f}x faster")
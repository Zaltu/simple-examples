# Overview
I was simply curious to see what the actual efficiency improvement would be on a `sort`/`max` operation combination if sorted lists were marked as such, meaning the max operation could immediately assume the last entry to be the largest.

From these results, looks like there's a relatively noticable improvement for larger lists, as expected, but overall there are incredibly few situations which would actually benefit from such an improvement. Especially since most cases could see a complete mix of sorted and unsorted lists. It is still technically an improvement however, and if the allocation time for the `is_sorted` key is made up for in time saved (which is probably is the case, but may not be for normal use), there's no real downside.


## Test values
List length: 5000
Iterations: 50,000
With/Without key ratio: 50/50


## Results
Average with key (sort+max): 0.0023173793488224
Average without key (sort+max): 0.0026120122049141

Average with key (max): 3.9851751484555e-07
Average without key (max): 0.00038220651999357


Total time with key (sort+max): 58.15
Total time without key (sort+max): 65.06

Total time with key (max): 0.010000000000019
Total time without key (max): 9.5199999999999


## Notes
Turns out LuaJIT is limited to 2GB RAM by default under 64-bit due to GC constraints.
With a List length of 500, LuaJIT will work, but this 5000 test was run on normal Lua 5.1.4

## Python baseline

Nothing special here - I just made Python inserter at Workshop.

I tuned it for speed as far as it made sense for me:

* bulk insert (10 per request)
* better regex (good regex library from pip)
* multiprocessing to run 4 copies of Python interpreter at once

Going more parallel is possible but much simpler to do mm D program to run about x2 times faster,
and the best part of it - I'm not eating  breaking my arms while doing it.
Java/Scala also should be very fast. ElasticSearch must take > 50% of the CPU to begin with!

It's all yours, show us that you can do better then this _slow baseline_.

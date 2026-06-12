# analytics-agent-lab

A reliable Python toolkit for basic analytics workflows.

## Usage

### Available Metrics Helpers

The `project_app.metrics` module provides simple statistical helper functions:

#### average(values)

Returns the arithmetic mean of a non-empty collection of numbers.

```python
from project_app.metrics import average

result = average([2, 4, 6])  # Returns 4
```

#### median(values)

Returns the median of a non-empty collection of numbers.

- For odd-length collections, returns the middle value.
- For even-length collections, returns the average of the two middle values.

```python
from project_app.metrics import median

result = median([3, 1, 5])    # Returns 3
result = median([1, 2, 3, 4])  # Returns 2.5
```

#### summarize_range(values)

Returns a dictionary with the minimum and maximum values from a non-empty collection.

```python
from project_app.metrics import summarize_range

result = summarize_range([1, 5, 3])  # Returns {"min": 1, "max": 5}
```

All functions require at least one value and will raise a `ValueError` if given an empty collection.
# API Reference

## Python — `calculator.py`

| Function | Signature | Description |
|---|---|---|
| `add` | `(a, b) -> Number` | Addition |
| `subtract` | `(a, b) -> Number` | Subtraction |
| `multiply` | `(a, b) -> Number` | Multiplication |
| `divide` | `(a, b) -> float` | Division; raises `ValueError` on zero divisor |
| `power` | `(base, exp) -> Number` | Exponentiation |
| `square_root` | `(n) -> float` | Square root; raises `ValueError` for negatives |
| `factorial` | `(n: int) -> int` | Integer factorial |
| `is_prime` | `(n: int) -> bool` | Primality test |
| `fibonacci` | `(n: int) -> list[int]` | First `n` Fibonacci numbers |

## Python — `data_processor.py`

| Function | Signature | Description |
|---|---|---|
| `load_csv` | `(filepath) -> list[dict]` | Parse CSV into list of row dicts |
| `load_json` | `(filepath) -> Any` | Parse JSON file |
| `save_json` | `(data, filepath, indent=2)` | Serialize data to JSON file |
| `filter_rows` | `(rows, key, value) -> list[dict]` | Keep rows where `row[key] == value` |
| `pluck` | `(rows, key) -> list` | Extract a single column |
| `numeric_summary` | `(values) -> dict` | Descriptive statistics |
| `group_by` | `(rows, key) -> dict` | Group rows by a key |
| `flatten` | `(nested) -> list` | Flatten one level of nesting |
| `deduplicate` | `(rows, key) -> list[dict]` | Remove duplicate rows |

## JavaScript — `utils.js`

| Function | Description |
|---|---|
| `clamp(value, min, max)` | Constrain a number to a range |
| `deepClone(obj)` | Deep-copy via JSON round-trip |
| `chunk(arr, size)` | Split array into sub-arrays of `size` |
| `debounce(fn, delay)` | Wrap a function to fire after `delay` ms of quiet |
| `sleep(ms)` | Promise-based delay |
| `groupBy(arr, key)` | Group objects by a key's value |
| `capitalize(str)` | Uppercase first character |
| `toSnakeCase(str)` | camelCase → snake_case |
| `flatten(arr)` | Flatten one level |
| `unique(arr)` | Remove duplicates (shallow) |

## JavaScript — `api_client.js`

### `new ApiClient(baseUrl, opts?)`

| Option | Default | Description |
|---|---|---|
| `timeout` | 10 000 ms | Per-request timeout |
| `retries` | 3 | Retry count on 5xx / network errors |
| `headers` | `{}` | Default headers merged into every request |

### Methods

```js
client.get(path, { params, headers })
client.post(path, { body, headers })
client.put(path, { body, headers })
client.patch(path, { body, headers })
client.delete(path, { headers })
```

All methods return a `Promise` that resolves to parsed JSON or plain text.
Throws `ApiError` (with `.status` and `.body`) on HTTP errors.

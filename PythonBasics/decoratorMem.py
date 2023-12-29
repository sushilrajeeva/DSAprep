from typing import Callable, Dict, Any

def memoize(f: Callable[..., Any]) -> Callable[..., Any]:
    memory: Dict[Any, Any] = {}  # Simple dictionary for caching

    def inner(*args: Any) -> Any:
        key = (f.__name__, args)  # Key includes function name and arguments
        if key not in memory:
            memory[key] = f(*args)
            print(f'result for {f.__name__} with arguments {args} saved in memory')
        else:
            print(f'returning result for {f.__name__} with arguments {args} from memory ->', end=" ")
        return memory[key]

    return inner

@memoize
def facto(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)

# Example usage
print(facto(5))
print(facto(5)) # directly coming from saved memory
print(facto(3)) # directly coming from saved memory

# The memoize decorator can now be used with other functions as well
@memoize
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 4))
print(add(3, 4)) # directly coming from saved memory

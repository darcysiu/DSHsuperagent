"""Greeting helpers used to test the agent."""


def greet(name: str) -> str:
    """Return a greeting for name.

    This sentence deliberately contains a spelling mistake.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))

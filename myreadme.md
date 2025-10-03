# Calculus Differentiation Rules

## Scalar Multiple Rule

If you have a constant multiplied by a function, you can "pull out" the constant when taking the derivative.

**Rule:** If *c* is a constant and *f(x)* is a function, then:
* d/dx[c · f(x)] = c · f'(x)

**Example:**
* d/dx[5x³] = 5 · d/dx[x³] = 5 · 3x² = 15x²

The constant 5 stays put while you differentiate x³ normally.

---

## Sum Rule

The derivative of a sum is simply the sum of the derivatives. You can differentiate each term separately.

**Rule:** If *f(x)* and *g(x)* are functions, then:
* d/dx[f(x) + g(x)] = f'(x) + g'(x)

This also works for subtraction: d/dx[f(x) - g(x)] = f'(x) - g'(x)

**Example:**
* d/dx[x³ + 4x² - 7x] = 3x² + 8x - 7

You just differentiate each term independently and add/subtract the results.

---

## Chain Rule

This is for **composite functions** (a function inside another function). It tells you how to differentiate when functions are nested.

**Rule:** If you have a composite function *f(g(x))*, then:
* d/dx[f(g(x))] = f'(g(x)) · g'(x)

In words: differentiate the outer function (leaving the inside alone), then multiply by the derivative of the inner function.

**Example:**
* d/dx[(3x + 1)⁵]

Here, the outer function is "something to the 5th power" and the inner function is "3x + 1"

* Outer derivative: 5(3x + 1)⁴
* Inner derivative: 3
* Result: 5(3x + 1)⁴ · 3 = 15(3x + 1)⁴

**Another way to think about it:** If *y = f(u)* and *u = g(x)*, then dy/dx = (dy/du) · (du/dx)


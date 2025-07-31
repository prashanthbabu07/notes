
# Functional Programming

- Functor 

fn add_1(x: i32) -> i32 {
    return x + 1;
}

f(x) = x + 1;

Lifting f(x) to Option<F>

Option::lift(f)
This return a new function that works with Option types with below signature:
Fn(Option<T>) -> Option<T> 

If there a function that converts a -> b then we can lift it to work with Option types.
Fn(Option<T>) -> Option<U>

Lifting add_1 to Option<F>
Option::lift(add_1)

- Endofunctor
A category that maps a type to itself.
e.g. Option<T> -> Option<T>
same type system or in the same world.

-- Monaid 
A set of elements M with a binary operation which take two elements of M and returns an element of M.
e.g.
[1, 2, 3].reduce(|a, b| a + b) // returns 6

-- monad is a monoid in the category of endofunctors

now we can perform operations like.

Some(1).map(add_1).map(add_2).map(add_3);

Here Some(1) is a monad, add_1, add_2, add_3 are functions that can be lifted to work with Option types.

All the chains of operations return a new Option type which is a monad.





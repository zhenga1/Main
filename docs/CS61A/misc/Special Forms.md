# Special Forms
Special form expressions contain a **special form** as the operator. Special form expressions _do not_ follow the same rules of evaluation as call expressions. Each special form has its own rules of evaluation -- that's what makes them special! Here's the [Scheme Specification](https://cs61a.org/articles/scheme-spec/#special-forms-2) to reference the special forms we will cover in this class.

It is important to note that everything in Scheme is either an **atomic** or an **expression**, so although these special forms look and operate similarly to Python, they are evaluated differently.

Special forms like `if`, `cond`, `and`, `or` in Python direct the control flow of a program and allow you to evaluate specific expressions under some condition. In Scheme, however, these special forms are expressions that take in a set amount of parameters and return some value based on the condition passed in.


# Built-in Procedures

To be able to call built-in procedures, such as `+`, you need to complete the `BuiltinProcedure` case within the `scheme_apply` function in `scheme_eval_apply.py`. Built-in procedures are applied by calling a corresponding Python function that implements the procedure.

> To see a list of all Scheme built-in procedures used in the project, look in the `scheme_builtins.py` file. Any function decorated with `@builtin` will be added to the globally-defined `BUILTINS` list.

A `BuiltinProcedure` has two instance attributes:

-   `py_func`: the _Python_ function that implements the built-in Scheme procedure.
-   `need_env`: a Boolean flag that indicates whether or not this built-in procedure will need the current environment to be passed in as the last argument. The environment is required, for instance, to implement the built-in `eval` procedure.

`scheme_apply` takes the `procedure` object, a list of argument values, and the current environment. `args` is a Scheme list represented as a `Pair` object or `nil`.
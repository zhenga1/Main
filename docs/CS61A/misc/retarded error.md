# Scheme
Traceback (most recent call last):
k (most recent call last):
  File "D:\Downloads\released_proj_scheme_scheme\scheme\ok\client\sources\ok_test\scheme.py", line 58, in evaluate
    result = timesr.timed(self.timeout, self.scheme.scheme_eval,
  File "D:\Downloads\released_proj_scheme_scheme\scheme\ok\client\utils\timer.py", line 33, in timed
    raise submission.error
  File "D:\Downloads\released_proj_scheme_scheme\scheme\ok\client\utils\timer.py", line 49, in run
    self.result = self.fn(*self.args, **self.kargs)
  File "D:\Downloads\released_proj_scheme_scheme\scheme\scheme_eval_apply.py", line 47, in scheme_eval
    return scheme_apply(op,operands,env)
  File "D:\Downloads\released_proj_scheme_scheme\scheme\scheme_eval_apply.py", line 71, in scheme_apply
    return procedure.py_func(*pythonlist)
  File "D:\Downloads\released_proj_scheme_scheme\scheme\scheme_builtins.py", line 431, in scheme_load
    read_eval_print_loop(next_line, env, quiet=quiet, report_errors=True)   
  File "D:\Downloads\released_proj_scheme_scheme\scheme\scheme.py", line 28, in read_eval_print_loop
    src = next_line()
  File "D:\Downloads\released_proj_scheme_scheme\scheme\scheme_builtins.py", line 427, in next_line
    return buffer_lines(lines)
NameError: name 'buffer_lines' is not defined

Code that doesn't work:
(if (integer? k)

  (let ((k k+1))

    (cond ((not (pair? s)) nil)

  (else (cons (cons k (car s)) (enumerate (cdr s))))

  ))

  (let ((k 0))

  (cond ((not (pair? s)) nil)

  (else (cons (cons k (car s)) (enumerate (cdr s)))))

  ) )
(let ((k

  ())))
 (

    cond ((not (pair? s)) nil

  )

  (

    else (cons (cons ((lambda (x) ()) (car s)) (car s)) (enumerate (cdr s) ) )

  )

)


#lang racket
;;  -------------------------------------------------------------------------
;; |   FILE           :  interpreter.rkt                                    |
;; |   AUTHOR         :  Alec Arcand                                        |
;; |   CREATION DATE  :  2019/04/27                                         |
;; |   DESCRIPTION    :  Contains functions that operate on the language    |
;;  -------------------------------------------------------------------------
(require "syntax-procs.rkt")
(require "utilities.rkt")
(provide (all-defined-out))
;; --------------------------------------------------------------------------
;; preprocess
;; --------------------------------------------------------------------------

(define preprocess 
  (lambda (exp)
    (cond 
      ((and (binary-exp? exp)
            (eq? '@ (binary->operator exp)))
       (let ((left  (preprocess (binary->exp1  exp)))
             (right (preprocess (binary->exp2 exp))))
         (make-binary (make-binary left '+ right)
                      '/
                      (make-num 2))))
      ((and (unary-exp? exp)
            (eq? 'sq (unary->operator exp)))
       (let ((operand (preprocess (unary->operand exp))))
         (make-binary operand '* operand)))
      ((do? exp)
       (if ((list-of? 3) exp) (make-do 'do (list (first (second exp)) ':= (preprocess (third (second exp))))
                                       (preprocess (third exp)))
           (make-do 'do (preprocess (second exp)))))
      ((number-in? exp)
       (make-num-in (second exp) (preprocess (fourth exp))
                    (preprocess (sixth exp))))
      ((varref? exp) exp)
      ((num? exp) exp)
      ((unary-exp? exp)
       (make-unary (unary->operator exp)
                   (preprocess (unary->operand exp))))
      ((binary-exp? exp)
       (make-binary (preprocess (binary->exp1 exp))
                    (binary->operator exp)
                    (preprocess (binary->exp2 exp))))
      (else (error 'preprocess "unreachable state ~a" exp)) )))

;; --------------------------------------------------------------------------
;; eval-exp
;; --------------------------------------------------------------------------

(define *init-env*
  (bind 'zero (cell 0)
        (bind 'two (cell 2)
              (bind 'ten (cell 10)
                    (make-bindings)))))

(define eval-exp 
  (lambda (exp)
    (if (boom-exp? exp)
        (eval-boom-exp (preprocess exp) *init-env*)
        (error 'eval-exp "illegal expression ~a" exp))))

(define eval-boom-exp
  (lambda (exp env)
    (cond
      ((number-in? exp)
       (eval-boom-exp (num-in-exp2 exp)
                      (bind (num-in-var exp)
                            (cell (eval-boom-exp (num-in-exp1 exp)
                                           env)) (make-bindings))))
      ((varref? exp) (look-up exp env))
      ((do? exp)
       (if ((list-of? 3) exp)
           (eval-boom-exp (third exp) ((cell-set! (first (second exp)))
                                       (eval-boom-exp (third (second exp))
                                                      env)) env)
           (eval-boom-exp (second exp) env)))
      ((num? exp)
       (make-num exp) )
      ((unary-exp? exp)
       (eval-unary-op
        (unary->operator exp)
        (eval-boom-exp (unary->operand exp) env))) 
      ((binary-exp? exp)
       (eval-binary-op
        (binary->operator exp)
        (eval-boom-exp (binary->exp1  exp) env)
        (eval-boom-exp (binary->exp2 exp) env))) 
      (else (error 'eval-exp "unreachable state ~a" exp)) )))

(define eval-unary-op
  (lambda (op-code exp)
    (cond
      ( (eq? op-code '- ) (- exp) )
      ( else (error 'eval "illegal operator ~a" op-code)))))

(define eval-binary-op
  (lambda (op-code exp1 exp2)
    (cond ( (eq? op-code '+) (+ exp1 exp2) )
          ( (eq? op-code '-) (- exp1 exp2) )
          ( (eq? op-code '*) (* exp1 exp2) )
          ( (eq? op-code '/) (quotient  exp1 exp2) )
          ( (eq? op-code '%) (remainder exp1 exp2) )
          ( else (error 'eval-binary-op "illegal operator ~a" op-code) ))))

;; --------------------------------------------------------------------------
;; run-boom
;; --------------------------------------------------------------------------

(define run-boom
  (lambda ()
    (display "==> ")
    (let ((answer (read)))
      (if (boom-exp? answer)
          (write (eval-exp answer))
          (begin (displayln "Illegal expression, input must be a boom expression!")
                 (run-boom)))
      (newline)
      (run-boom))))

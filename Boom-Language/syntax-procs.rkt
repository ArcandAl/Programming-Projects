#lang racket
;;  -------------------------------------------------------------------------
;; |   FILE           :  syntax-procs.rkt                                   |
;; |   AUTHOR         :  Alec Arcand                                        |
;; |   CREATION DATE  :  2019/04/27                                           |
;; |   DESCRIPTION    :  Holds all syntax procedures                        |
;;  -------------------------------------------------------------------------
(require "utilities.rkt")
(provide (all-defined-out))

;----------------------------------------------------------------------------
; general type predicate

(define boom-exp?
  (lambda (exp)
    (or (num?        exp)
        (unary-exp?  exp)
        (binary-exp? exp)
        (varref? exp)
        (number-in? exp)
        (do? exp))))

;----------------------------------------------------------------------------
; number expressions

(define num?
  (lambda (n)
    (number? n) ))

(define make-num identity)

(define number->value identity) 
;----------------------------------------------------------------------------
; unary expressions

(define unary-exp?
  (lambda (n)
    (and ((list-of? 2) n)
         (unary-op? (first n))
         (boom-exp? (second n)))))

(define unary-op?
  (lambda (n)
    (cond
      ((eq? n '-) #t )
      ((eq? n 'sq) #t)
      (else #f))))

(define unary->operator first)
(define unary->operand second)

(define make-unary
  (lambda (operator operand)
    (list operator operand)))
;----------------------------------------------------------------------------
; binary expressions

(define binary-exp?
  (lambda (n)
    (and ((list-of? 3) n)
         (boom-exp?  (first  n))
         (binary-op? (second n))
         (boom-exp? (third  n)))))

(define binary-op?
  (lambda (n)
    (cond
      ((eq? n '+) #t)
      ((eq? n '-) #t)
      ((eq? n '*) #t)
      ((eq? n '/) #t)
      ((eq? n '%) #t)
      ((eq? n '@) #t)
      (else #f))))

(define binary->exp1 first)
(define binary->operator second)
(define binary->exp2 third)

(define make-binary
  (lambda (exp1 operator exp2)
    (list exp1 operator exp2)))


;; --------------------------------------------------------------------------
;; variable references
;; --------------------------------------------------------------------------

(define varref?
  (lambda (exp)
    (symbol? exp)))

(define make-varref identity)
(define get-var identity)

;; --------------------------------------------------------------------------
;; number-in expressions
;; --------------------------------------------------------------------------

(define number-in?
  (lambda (exp)
    (and (list? exp)
         (= (length exp) 6)
         (eq? 'number (first exp))
         (varref? (second exp))
         (eq? '= (third exp))
         (boom-exp? (fourth exp))
         (eq? 'in (fifth exp))
         (boom-exp? (sixth exp)))))

(define num-in-var second)
(define num-in-exp1 fourth)

(define num-in-exp2 sixth)

(define make-num-in
  (lambda (var exp1 exp2)
    (list 'number var '= exp1 'in exp2)))

;; --------------------------------------------------------------------------
;; do expressions
;; --------------------------------------------------------------------------

(define do?
  (lambda (exp)
    (or (and ((list-of? 3) exp)
         (eq? 'do (first exp))
         (assignment? (second exp))
         (boom-exp? (third exp)))
        (and ((list-of? 2) exp)
             (eq? 'do (first exp))
             (boom-exp? (second exp))))))

(define do-exp third)

(define make-do list)

(define assignment?
  (lambda (exp)
    (and ((list-of? 3) exp)
         (varref? (first exp))
         (eq? ':= (second exp))
         (boom-exp? (third exp)))))

(define assign-exp
  (lambda (n)
    (third (second n))))

(define assign-var
  (lambda (n)
    (first (second n))))

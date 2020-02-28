#lang racket
;;  -------------------------------------------------------------------------
;; |   FILE           :  tests.rkt                                          |
;; |   AUTHOR         :  Alec Arcand                                        |
;; |   CREATION DATE  :  2019/04/27                                           |
;; |   DESCRIPTION    :  Contains all tests                                 |
;;  -------------------------------------------------------------------------
(require rackunit)
(require "utilities.rkt")
(require "syntax-procs.rkt")
(require "interpreter.rkt")

;----------------------------------------------------------------------------
; checks for type predicates

(check-true (boom-exp? '(sq 16)))
(check-true (boom-exp? '(2 * (4 / (sq 16)))))
(check-true (boom-exp? '((8 % 3) + ((- 4) * (6 @ 10)))))

(check-true (boom-exp? 'z))
(check-true (boom-exp? '(number z = (x * y) in (- z))))
(check-true (boom-exp? '(number square = (x * x) in
                              (number half = (square / 2) in
                                 (half + (x + 4))))))

;-----------------------------------------------------------------------------
; checks for preprocess

(check-equal? (preprocess '(5 @ 10)) '((5 + 10) / 2))
(check-equal? (preprocess '(- (5 @ 10))) '(- ((5 + 10) / 2)))
(check-equal? (preprocess '((1 * 5) + (123 @ 54))) '((1 * 5) + ((123 + 54) / 2)))

(check-equal? (preprocess 'two) 'two)
(check-equal? (preprocess 'z) 'z)

(check-equal? (preprocess '(number z = (x @ y) in (- z)))
              '(number z = ((x + y) / 2) in (- z)))
(check-equal? (preprocess '(number square = (sq x) in
                      (number average = (square @ x) in
                        ((sq average) - 4))))
              '(number square = (x * x) in
        (number average = ((square + x) / 2) in
          ((average * average) - 4))))

;------------------------------------------------------------------------------
; checks for eval-exp

(check-equal? (eval-exp '((2 * 14) + (13 @ 29))) 49)
(check-equal? (eval-exp '((8 % 3) + (4 * (6 - (20 / 10))))) 18)
(check-equal? (eval-exp '((- 3) + (sq (4 * 2)))) 61)

(check-equal? (eval-exp '(number z = (4 @ 2) in (- z))) -3)
(check-equal? (eval-exp '(number z = (1 + 8) in (- z))) -9)
(check-equal? (eval-exp '(number z = (5 % 8) in (- z))) -5)
(check-equal? (eval-exp '(number square = (sq 5) in
                      (number average = (square @ 5) in
                        ((sq average) - 4)))) 221)

;(check-equal? (eval-exp '(do (2 @ 4))) 3)
;(check-equal? (eval-exp '(number c = 10 in
;                    (do (c := ((sq c) + c))
;                        (c := (c / 10))
;                        (c - 1)))) 10)
;(check-equal? (eval-exp '(number x = 26 in
;                    (do (x := (x * 2))
;                        (x @ 30)))) 41)

;------------------------------------------------------------------------------
; checks for cell ADT

(define var (cell 0))
(define foo (cell 10))

(check-equal? ((cell-value var)) 0)
(check-equal? ((cell-value foo)) 10)

(check-equal? ((cell-set! var) 10) 10)
(check-equal? ((cell-set! foo) 350) 350)

(check-equal? ((cell-set! var) (+ ((cell-value var)) 5)) 15)
(check-equal? ((cell-set! foo) (+ ((cell-value foo)) 5)) 355)



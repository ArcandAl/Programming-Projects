#lang racket
;;  -------------------------------------------------------------------------
;; |   FILE           :  utilities.rkt                                      |
;; |   AUTHOR         :  Alec Arcand                                        |
;; |   CREATION DATE  :  2019/04/27                                           |
;; |   DESCRIPTION    :  Holds all helper functions                         |
;;  -------------------------------------------------------------------------
(provide (all-defined-out))

;----------------------------------------------------------------------------
; helper functions

(define list-of?
  (lambda (n)
    (lambda (obj)
      (and (list? obj)
           (eq? n (length obj))))))


(define every?
  (lambda (test? lst)
    (or (null? lst)
        (and(test? (car lst))
            (every? test? (cdr lst))))))

;----------------------------------------------------------------------------
; Environment ADT

(define make-bindings
  (lambda ()
    (list)))

(define bind
  (lambda (var val existing-bindings)
    (cons (cons var val) existing-bindings)))

(define look-up
  (lambda (var existing-bindings)
    (if (null? existing-bindings)
        (error 'environment "undefined variable -- ~a" var)
        (if (eq? var (car (car existing-bindings)))
            ((cell-value (cdr (car existing-bindings))))
            (look-up var (drop existing-bindings 1))))))

(define var-exists?
  (lambda (var existing-bindings)
    (if (null? existing-bindings)
        #f
        (if (eq? var (first existing-bindings))
            #t
            (var-exists? var (drop existing-bindings 2))))))
;----------------------------------------------------------------------------
; Cell ADT


(define cell            
  (lambda (init-value)
   (list (lambda (value)
           (begin (set! init-value value)
                  init-value))
         (lambda ()
           init-value ))))

(define cell-value second)
(define cell-set! first )




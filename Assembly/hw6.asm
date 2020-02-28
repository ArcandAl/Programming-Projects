	.data
array:			.word 10 -5 -30 15 20 -1 -26 -18 0
largestNumber:		.word 0
smallestNumber:		.word 0
	
	.text
	.globl main
main:
	li 	$8, 0			#load immediate 0 in reg $8 (largestNumber)
	li	$7, 0			#load immediate 0 in reg $7 (smallestNumber)	
	la	$11, array		#load base addr of array into $11
for:	
	li	$9, 0			#initialize i in $9 to 0
while:
	beq	$9, 0, end_while	#end when number = 0
if:	blt 	$9, $8, if_2		#jump if_2 if $9 < largestNumber
	
	move 	$8, $9			#set i as new largestNumber
if_2:
	bgt	$9, $7, before_while	#jump while if $9 > smallestNumber
	
	move	$7, $9			#set i as new smallestNumber
before_while:
	mul	$12, $9, 4
	add	$12, $11, $12
	lw	$12, 0($12)
	addi 	$9, $9, 1		#increment i
	j	while			
end_while:
	sw	$8, largestNumber	
	sw	$7, smallestNumber
	li 	$v0, 10
	syscall
	.data
array:		.word 60 35 10 50 45 20 25 40 30
n:		.word 9
		
		.text
		.globl main
main:
		la	$a1, array		# starting address of array
		lw	$a2, n			# length of array
		
		jal	mergeSort

		li	$v0, 10
		syscall				# system call to exit program
	
merge:
		li	$t0, 0			# $t0 is left
		li	$t1, 0			# $t1 is right
		li	$t2, 0			# $t2 is next
		move	$t3, $a1		# move array
		add	$t3, $t3, $t2		# get sortedArray[next]
		add	$s2, $s2, $t0		# get leftArray[left]
		add	$s3, $s3, $t1		# get rightArray[right]
while_1:
		bgt	$t0 ,$s0, while_2	# if left > leftSize
		bgt	$t1, $s1, while_2	# if right > rightSize
if:
		bgt	$s2, $s3, else		# if leftArray < rightArray
		move	$s2, $t3		# sortedArray[next] = leftArray[left]
		addi	$t0, $t0, 1		# increment left
		addi	$t2, $t2, 1		# increment next
		addi	$t3, $t3, 4		# increment sortedArray
		addi	$s2, $s2, 4		# increment leftArray
		j	while_1
else:
		move	$s3, $t3		# sortedArray[next] = rightArray[right]
		addi	$t1, $t1, 1		# increment right
		addi	$t2, $t2, 1		# increment next
		addi	$t3, $t3, 4		# increment sortedArray
		addi	$s3, $s3, 4		# increment rightArray
		j 	while_1
while_2:
		bgt	$t0, $s0, while_3	# if left > leftSize
		move	$s2, $a1		# sortedArray[next] = leftArray[left]	
		addi	$t0, $t0, 1		# increment left
		addi	$t2, $t2, 1		# increment next
		j	while_2
while_3:
		bgt	$t1, $s1, end_while	# if right > rightSize
		move	$s3, $a1		# sortedArray[next] = rightArray[right]
		addi	$t1, $t1, 1		# increment right
		addi	$t2, $t2, 1		# increment next
	
end_while:
		jr	$ra

mergeSort:
		addi	$sp, $sp, -20		# save room for return address
		sw	$ra, 4($sp)		# push return address onto stack
		sw	$s0, 8($sp)
		sw	$s1, 12($sp)
		sw	$s2, 16($sp)
		sw 	$s3, 20($sp)

		li	$t0, 2
		ble	$a2, $t0, end_mergeSort	# if size < 2
		move	$s0, $a2
		srl	$s0, $s0, 1		# $s0 = size/2 (leftSize)
		sub	$s1, $a2, $s0 		# $s1 = size - leftSize (rightSize)
		mul	$t1, $a2, 4
		li	$a0, 18  		# $a0 contains number of bytes needed
		li	$v0, 9			# alocate memory
		syscall
		move	$s2, $v0		# $s2 = leftArray
		li	$a0, 18                 # $a0 contains number of bytes needed
		li	$v0, 9			# allocate memory
		syscall
		move	$s3, $v0		# $s3 = rightArray

for_init_1:		
		li 	$t3, 0			# $t3 = index 
		move	$t4, $a1		# move array

for_1:
		bgt	$t3, $s0, for_init_2	# if index > leftSize 
		move	$s2, $t4		# leftArray[index] = array[index]
		addi	$t3, $t3, 1		# increment index
		addi	$t4, $t4, 4		# next element to copy
		addi	$s2, $s2, 4
		j	for_1

for_init_2:
		li	$t3, 0			# $t3 =  index 
		move	$t5, $a1		# move array
		add	$t5, $t3, $s0		# index + leftSize
for_2:
		bgt	$t3, $s1, recursive	# if size > rightSize
		move	$s3, $t5		# rightArray[index] = array[leftSize + index]
		addi	$t3, $t3, 1		# increment index
		addi	$t5, $t5, 4		# next element to copy
		addi	$s3, $s3, 4		
		j	for_2
recursive:
		move	$a1, $s2		# makes leftArray new array to sort
		move	$a2, $s0
		jal	mergeSort		# mergeSort leftArray

		move	$a1, $s3		# makes rightArray new array to sort
		move	$a2, $s1
		jal	mergeSort		# mergeSort rightArray
		
		jal	merge 			# call merge to merge sorted halfs back together

end_mergeSort:
		lw	$ra, 4($sp)		# restore return address to $ra
		lw	$s0, 8($sp)		# restore $s registers
		lw	$s1, 12($sp)
		lw	$s2, 16($sp)
		lw 	$s3, 20($sp)
		addi	$sp, $sp, 20		# pop call frame from stack	

		jr	$ra
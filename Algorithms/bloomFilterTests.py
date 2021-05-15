from BloomFilter import Bloom_Filter

#start_bits = int(input("Enter number of bits to use: "))
#hash_count = int(input("Enter numbe of hash functions to be used: "))

start_bits = 124
hash_count = 4

bloom = Bloom_Filter(start_bits, hash_count)
print()
print("Bloom Filter successfully created with",start_bits,"bits and",hash_count, "hash functions.","\n")

to_add = ["cs","bloom","filter","algorithms","class","professor","activity","5","binary","hash","bytes","bits"]
not_added = ["seed","file","cryptographic","murmur3","keys","function","append",]

for i in to_add:
    bloom.add(i)

all_words = to_add + not_added

for i in all_words:
    if bloom.probablyContains(i):
        if i in to_add:
            print("The Bloom Filter might contain", "'"+i+"'")
        else:
            print("'"+i+"'", "is a false key in the Bloom Filter")
    else:
        print("'"+i+"'", "is not in the Bloom Filter")

print()
bloom.save("tester_file")
print("Thhe Bloom Filter was saved to a binary file successfully!")


bloom.add('testWord')
print("'testWord' was added to Bloom Filter")
print("Search for 'testWord' should be true. Testing for 'testWord'...")
print("Search returned: ",bloom.probablyContains('testWord'),"\n")

bloom.restore("tester_file")
print("The old Bloom Filter was uploaded successfully!")
print("Search for 'testWord' should be false now. Testing for 'testWord'...")
print("Search returned: ",bloom.probablyContains('testWord'))

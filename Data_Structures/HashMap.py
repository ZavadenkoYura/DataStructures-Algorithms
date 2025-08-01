class HashTable(object):
    _capacity = 10
    _size = 0
    _data = [[] for _ in range(_capacity)]
    _load_factor = 0
    
    def put(self, key, value):
        slot = self.__hash(key)
        self._data[slot].append(value)
        self._size += 1
        
        print(f"Element {value} with key {key} was inserted at slot {slot}")

        
    def remove(self, key):
        slot = self.__hash(key)
        if len(self._data[slot]) <= 0:
            print(f"No elements in slot {key}")
            return 
        
        removed_element = self._data[slot].pop()
        return removed_element

    
    def search(self, key):
        slot = self.__hash(key)
        if len(self._data[slot]) == 0:
            print(f"No elements in slot {key}")
            return
        
        print(f"Key {key} map -> to slot {slot}: ")
        for element in self._data[slot]:
            print(element)

        
    def compute_load_factor(self):
        return self._capacity / self._size


    def __hash(self, key):
        """Using chaining"""
        h = key % self._capacity # Division method could use multiplication method like h = self._size * ((A * key) % 1) 
        return h
    
    
ht = HashTable()

ht.put(1, "Apple")
ht.put(2, "Banana")
ht.put(12, "Orange") 

ht.search(1)  
ht.search(2)  
ht.search(12) 

removed_item = ht.remove(1) 
print(f"Removed item: {removed_item}")
ht.search(1) 

ht.put(3, "Grapes")

load_factor = ht.compute_load_factor()
print(f"Current load factor: {load_factor}")

"""
 Direct addressing is a simple technique that works well when the universe U of
 keys is reasonably small

 The downside of direct addressing is obvious: if the universe U is large, storing
 atableT of size jUj may be impractical, or even impossible, given the memory
 available on a typical computer

 So we use chaining with linked-list for collision resolution.

 What makes a good hash function? 
    A good hash function satisfies (approximately) the assumption of simple uniform
    hashing: each key is equally likely to hash to any of the m slots, independently of
    where any other key has hashed to
 
    1. The division method ->  h(k) = k % m
        When using the division method, we usually avoid certain values of m. For
        example, m should not be a power of 2, since if m D 2p, then h(k) is just the p
        lowest-order bits of k.
        A prime not too close to an exact power of 2 is often a good choice for m. For
        example, suppose we wish to allocate a hash table, with collisions resolved by
        chaining, to hold roughly n = 2000 character strings, where a character has 8 bits.
        We do not mind examining an average of 3 elements in an unsuccessful search, and
        so we allocate a hash table of size m = 701. We could choose m = 701 because
        it is a prime near 2000 / 3 but not near any power of 2. Treating each key k as an
        integer, our hash function would be
        h(k) = k % 701
    
    2. The multiplication method -> h(k) = m((kA) mod 1), where m is the size of the hash table, A is a 'golden ration' (0.6180339887)
        suggested by Knuth which is equel to A = s / 2^w where s is an integer and w is a word size of a computer (32-bit, 64-bit)
        An advantage of the multiplication method is that the value of m is not critical. We typically choose it to be a power of 2 
        (m = 2^p for some integer p), since we can then easily implement the functions like binary shifts on most computers.

 Why Universal Hashing?
    If we always use the same hash function, an attacker could craft inputs that cause many collisions (bad performance). 
    Universal hashing solves this by choosing a random hash function from a family of functions, 
    making it hard to predict and exploit. A set of hash functions H is called universal if for any two different keys 
    k1 and k2, the probability that they collide is 1/m, where m is a number of slots in a hash table:
        
        Pr(h(k1) = h(k2)) ≤ 1/m

    A universal class of hash functions: 
        
        h_ab(k) = ((ak + b) % p) % m, where p is a prime number larger than any key and a, b 
        are random integers such that 1 ≤ a < p and 0 ≤ b < p. The universal collection 
        contains p(p - 1) hash functions, as there are p - 1 choices for a and p choices for b 
    
 Open addressing
    To perform insertion using open addressing, we successively examine, or probe the hash table until we find an empty slot in which to put the key
    Instead of being fixed in the order 0, 1, ..., m - 1 (which requires O(n) searchtime), the sequence
    of positions probed depends upon the key being inserted. To determine which slots
    to probe, we extend the hash function to include the probe number (starting from 0)
    as a second input -> (h(k, 0), h(k, 1), h(k, 2) ... h(k, m - 1)). Uniform hashing generalizes the notion of simple uniform hashing defined earlier to a
    hash function that produces not just a single number, but a whole probe sequence. True uniform hashing is difficult to implement, however, and in practice suitable
    approximations such as linear, quadratic and double hashing are used:
    
    
    1. Linear probing:
        Linear probing is a method for resolving hash collisions in open addressing hash tables. It uses an auxiliary hash function to determine the probe sequence.
        Auxiliary Hash Function h_0 maps an element k from the universe U to the range {0..m-1}, 
        h_0(k) gives the initial slot to probe in the hash table. The probe function is defined as:
    
            h(k, i) = (h_0(k) + i) % m, for i=0, 1, ..., m-1

        There are exactly m distinct probe sequences since the initial probe determines the rest of the sequence.
        Issues with Linear Probing: Primary clustering occurs when long runs of occupied slots form. 
        These clusters increase the average search time for keys, especially as the table fills up.
        When an empty slot is preceded by i occupied slots, then the next empty slot will be filled with a probability i+1 / m 
        
    2. Quadratic probing:
        Unlike linear probing, the probe sequence depends quadratically on the probe number. The hash function for quadratic probing is defined as:

            h(k, i) = (h_0(k) + c_1 * i + c_2 * i^2) % 𝑚, where h_0(k) is the auxiliary hash function that gives the initial probe position, 
            c_1 and c_2 are positive constants that control the offset of the probe sequence, i is the probe number, ranging from 0 to 𝑚 - 1
            
        The position to probe next increases faster than linear probing. Quadratic probing helps reduce clustering compared to linear probing by spreading out the probe sequence.
        
    3. Double probing:
         Double hashing uses a hash function of the form:
                
                h(k, i) = (h_1(k) + i * h_2(k)) % m where both h_1 and h_2 are auxiliary hash functions. The initial probe goes to position T[h1(k)]; 
                successive probe positions are offset from previous positions by the amount h2(k), modulo m. Thus, unlike the case of linear or quadratic probing, the
                probe sequence here depends in two ways upon the key k, since the initial probe position, the offset, or both, may vary.
                
        The value h2(k) must be relatively prime to the hash-table size m for the entire hash table to be searched as 
        this helps ensure that each probe sequence is unique and that the hash table is fully explored. 
                  
        For double hashing, each probe sequence is defined by the pair (h_1(k), k_2(k)). Since both ℎ_1(𝑘) and h_2(k)  depend on the key k and there are m possible values for 
        ℎ_1(𝑘) (because it’s computed modulo m), and m possible values for ℎ_2(𝑘), the total number of distinct combinations of ℎ_1(𝑘) and ℎ_2(𝑘) is 𝑚^2. 
        This allows double hashing to explore many more possible probe sequences than linear or quadratic probing can, 
        leading to better distribution of keys and fewer collisions, which results in better performance.
        
        If 𝑚 is prime, it guarantees that ℎ_2(𝑘) is likely to be relatively prime to 𝑚, ensuring a full table scan without cycles or repeated probe sequences.
        If 𝑚 is a power of 2, you can design ℎ_2(𝑘) to be an odd number, which is also guaranteed to be relatively prime to 𝑚.
        
        When 𝑚 is prime or a power of 2, double hashing has the flexibility to explore all 𝑚^2 possible probe sequences, 
        which is a huge improvement over linear or quadratic probing that can only explore 𝑚 sequences.
        
    4. Perfect hashing:
        Perfect hashing is when O(1) memory accesses are required to perform a search in the worst case. To create a perfect hashing scheme, we use two levels of hashing, with universal
        hashing at each level. The first level is essentially the same as for hashing with chaining. Instead of making a linked list of the keys hashing to slot j, however, we use a
        small secondary hash table S_j with an associated hash function h_j. We choose the size of the hash table S_j to be the square of the number n_j keys which hash to slot j. 
        The first level hash function is chosen from a universal set H_1 and those keys that map to slot j use universal hash values of H_j. 
"""

# Uniform Random Generator
import random

class MyRandomGen():
    def randomGen(self, lo, hi):
        """
        Generate a random number between lo and hi

        :param lo: Lower bound of the number
        :param hi: Higher bound of the number

        :return: generated number
        """

        # We can easily find a number between 0 and n.
        #
        # Approach:
        # --------
        #
        # We check how many bits it takes to create a number n.
        #   - "2^i - 1" defines the maximum number with "i" bits
        #   - Therefore, to find how many bits it takes to find n, we need to make sure that
        #
        #           2^i - 1 >= n  <=>  2^i >=  n + 1
        #           i is the number of bits that can represent n
        #
        #
        # We randomly choose each bit and concatenate them to generate a number that is in the range of n.
        #

        # Find a number between lo and hi
        #
        # Method:
        # ------

        # To find a number between lo to hi, we can take the same approach as above by randomly generating a number
        # between 0 and n.
        # n is the maximum value that can be added to "lo", so the final result can be in the range between lo
        # and hi.
        #
        #       lo + n <= hi




        # Repeat this number generation procedure until we get a number that is in the range of (hi - lo)
        while (True):

            i = 0 # number of bits
            generated_number = 0 # number generated from a combination of random bits


            max_value = hi - lo # maximum value that can be added to "lo" to achieve a number between "lo" and "hi"

            # As long as 2^i is smaller than (n-m) + 1, add a bit
            #
            # T(n) = log(n)
            # n is the range of numbers (hi-lo)
            while ((1 << i) < (hi - lo + 1)):

                #generate a random bit
                bit = random.getrandbits(1)

                #concatenate to the previous one
                generated_number = (generated_number << 1) | bit

                i += 1

            # Check if the generated number is in the range between 0 and max value
            # Time complexity can be slower if we don't find a number in the range soon enough
            if (generated_number <= max_value):
                break

            # Number of tries converge to O(1) (explanation to follow)
        return lo + generated_number




number = MyRandomGen().randomGen(1, 6)
print ("Random number: %s " % number)
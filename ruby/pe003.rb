#!/usr/bin/env ruby

class PE003
    def largest_prime_factor_of(n)
        # dont check 2 because number given is odd
        factor = 3
        while n != 1
            while n % factor == 0
                n /= factor
            end
            last = factor
            factor += 2
        end
        return last
    end

    def solve 
        bignumber = 600851475143
        puts largest_prime_factor_of 13195
    end
end

if __FILE__ == $0
    pe = PE003.new
    pe.solve
end

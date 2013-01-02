#!/usr/bin/env ruby
#

class PE002 
    def fib(n)
        s = Math.sqrt(5)
        x = (1 + s) ** n
        y = (1 - s) ** n
        return ((x - y) / (2**n * s)).to_i
    end

    def solve
        max = 4000000
        sum = 0
        n = 1
        num = fib n
        while num < max
            if num % 2 == 0
                sum += num
            end
            n += 1
            num = fib n
        end
        return sum
    end

    def show_result
        puts solve
    end
end


if __FILE__ == $0
    pe = PE002.new
    pe.show_result
end

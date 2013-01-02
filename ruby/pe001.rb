#!/usr/bin/env ruby

class PE001
    def solve_python
        sum = 0
        (0..999).each do |n| 
            if n % 5 == 0 || n % 3 == 0
                sum += n
            end
        end
        return sum
    end

    def solve_reduce
        return (0..999).reject{|i| i % 3 != 0 and i % 5 !=0}.reduce(:+)
    end

    def show_result
        puts solve_python
        puts solve_reduce
    end
end

if __FILE__ == $0
    pe = PE001.new
    pe.show_result
end

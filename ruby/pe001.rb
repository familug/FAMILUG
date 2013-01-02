#!/usr/bin/env ruby

class PE001
    def solve
        sum = 0
        (0..999).each do |n| 
            if n % 5 == 0 || n % 3 == 0
                sum += n
            end
        end
        return sum
    end

    def show_result
        puts solve
    end
end

if __FILE__ == $0
    pe = PE001.new
    pe.show_result
end

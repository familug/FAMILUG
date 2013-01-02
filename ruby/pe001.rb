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

    def solve_inject
        #http://blog.jayfields.com/2008/03/ruby-inject.html
        #i hate this subtle sugar syntax
        return (0..999).reject {|i| i % 3 != 0 and i % 5 != 0}.inject{|sum, num| sum + num}
    end

    def show_result
        puts solve_python
        puts solve_reduce
        puts solve_inject
    end
end

if __FILE__ == $0
    pe = PE001.new
    pe.show_result
end

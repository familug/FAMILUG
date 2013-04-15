#!/usr/bin/env ruby
# Wed Jan  2 17:58:42 ICT 2013
# by hvn@familug.org

def fib(n)
    s5 = Math.sqrt 5
    a = (1 + s5) ** n
    b = (1 - s5) ** n
    return (a - b) / (2 ** n * s5)
end

# user recursive for fib
# def fib(n)
#     return n if n < 2
#     return fib(n-1) + fib(n-2)
# end

def do_math
    puts "Fast fibonacci\n"
    (1..10).each do |n|
        print n ," ", fib(n).to_i, "\n"
    end
end


if __FILE__ == $0
    do_math
end

#!/usr/bin/env ruby
#Today: 20130103

#longer with class
#class FMLB1
#    def list_users
#        file = File.new('/etc/passwd', 'r')
#        while(line = file.gets)
#            puts line.split(':')[0]
#        end
#    end
#end
#
#if __FILE__ == $0
#    fmlb = FMLB1.new
#    fmlb.list_users
#end

#and shorter just as needed
file = File.new('/etc/passwd', 'r')
while(line = file.gets)
    puts line.split(':')[0]
end

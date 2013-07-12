victim = arg[1]
SEP = "\n+------------------------------------+"

print(">> Fingerprinting "..victim)
print(SEP)


handle = io.popen("ping -c 3 "..victim)
result = handle:read("*a")

print(">> PING: "..string.match(result, "%w%% packet loss"))
print(SEP)

print("Scanning open port...")

handle = io.popen("nmap -sT "..victim.." | grep http")
result = handle:read("*a")

if string.find(result,"80/tcp") ~= nil then
    print(">> WARNING 80 is OPEN")
else
    print(">> Port 80 closed")
end
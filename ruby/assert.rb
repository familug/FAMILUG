def assert_equals(assuming, result)
    raise "False" unless assuming == result
end

assert_equals 1, 1
assert_equals (nil, nil)
assert_equals nil, nil

require("mathop")
clock = os.clock

function test_sorted ()
    lists = {}
    for i=0,50000,1 do
        table.insert(lists, generate_list())
    end

    with_keys_full = {}
    with_keys_max = {}
    without_keys_full = {}
    without_keys_max = {}
    for _, alist in pairs(lists) do
        if math.random(1, 2) == 1 then
            wk = with_key(alist)
            table.insert(with_keys_full, wk[1])
            table.insert(with_keys_max, wk[2])
        else
            wk = without_key(alist)
            table.insert(without_keys_full, wk[1])
            table.insert(without_keys_max, wk[2])
        end
    end

    print("Average with key (sort+max): "..average(with_keys_full))
    print("Average without key (sort+max): "..average(without_keys_full))
    print()
    print("Average with key (max): "..average(with_keys_max))
    print("Average without key (max): "..average(without_keys_max))
    print()
    print()
    print("Total time with key (sort+max): "..sum(with_keys_full))
    print("Total time without key (sort+max): "..sum(without_keys_full))
    print()
    print("Total time with key (max): "..sum(with_keys_max))
    print("Total time without key (max): "..sum(without_keys_max))
end

function generate_list ()
    alist = {}
    for i=0,5000,1 do
        table.insert(alist, math.random(-200, 200))
    end
    return alist
end

function with_key (alist)
    start = clock()
    table.sort(alist)
    alist.is_sorted = true
    maxtime = clock()
    max(alist)
    theend = clock()
    return {theend-start, theend-maxtime}
end

function without_key (alist)
    start = clock()
    table.sort(alist)
    maxtime = clock()
    max(alist)
    theend = clock()
    return {theend-start, theend-maxtime}
end


function average (times)
    total = 0
    for _, time in pairs(times) do
        total = total + time
    end
    return total/#times
end


function sum (times)
    total = 0
    for _, time in pairs(times) do
        total = total + time
    end
    return total
end



test_sorted()
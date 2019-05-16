function max (list)
    if list.is_sorted then
        return list[#list]
    end
    local max = nil
    for _, value in pairs(list) do
        if max==nil or value > max then
            max = value
        end
    end
    return max
end

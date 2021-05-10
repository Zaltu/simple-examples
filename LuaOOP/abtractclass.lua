-- This is not technically a true "abstract" "class", as you could easily call `Job()` from anywhere
-- relevant, however it does provide only a very pure table, and cannot be reference as pseudo-objects
-- usually are in Lua.
Job = function () return {title="Wagie", industry=nil} end

-- Subclass starts with these default values.
Programmer = Job()
Programmer.__index = Programmer

function Programmer:new(title)
    local prog = {}
    prog.knownlangs = {"Lua", "Luajit", "More Lua"}
    prog.title = title
    setmetatable(prog, Programmer)
    return prog
end


-- Example of overwriting with child class
local programmer1 = Programmer:new("Lead")
print(programmer1.knownlangs)
print(programmer1.title)

-- Example of using defaults from parent class
local programmer2 = Programmer:new()
print(programmer2.knownlangs)
print(programmer2.title)
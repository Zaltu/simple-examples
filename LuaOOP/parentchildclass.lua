-- Create a parent class, Creature, which can be instatiated and also inherited.
Creature = {planet="Earth"}
Creature.__index = Creature
-- Constructor
function Creature:new()
    -- Object instances are basically empty, since they don't need anything. Values could be placed here however.
    local creat = {}
    creat.breathes = "Nothing"
    setmetatable(creat, Creature)
    return creat
end



-- Child class is defined here. The generic Person inherits from Creature, and therefore has all it's default properties.
Person = Creature:new()
Person.__index = Person
-- Constructor
function Person:new(firstname, lastname, breathes)
    -- Here we can define attributes of the child class
    local person = {}
    person.name = firstname.." "..lastname
    -- We can overwrite any of the values of the "parent" class, because Lua
    person.breathes = breathes
    -- Set the "type" of this table
    setmetatable(person, Person)
    return person
end

-- We can also define any other functions we want, for our child or parent classes
function Person:say_my_name()
    print(self.name)
end

-- Example of fully set child class
local mrjohnny = Person:new("Johnny", "Thunder", "Oxygen")
mrjohnny:say_my_name()
print(mrjohnny.planet)
print(mrjohnny.breathes)

-- Example of falling back on parent class defaults
local mrsandman = Person:new("Johnny", "Thunder")
mrsandman:say_my_name()
print(mrsandman.planet)
print(mrsandman.breathes)

-- Example of parent class
local something = Creature:new()
print(something.planet)
print(mrsandman.breathes)
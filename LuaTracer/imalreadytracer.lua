bit32 = require('bit32')

local function add_vector(a, b)  -- +
    return {
        a.x+b.x,
        a.y+b.y,
        a.z+b.z
    }
end

local function multi_vector(a, f)  -- *
    return {
        a.x*f,
        a.y*f,
        a.z*f
    }
end

local function dot_prod_vector(a, b)  -- %
    return a.x*b.x + a.y*b.y + a.z*b.z
end

local function cross_prod_vector(a, b)  -- ^
    return {
        a.y*b.z-a.z*b.y,
        a.z*b.x-a.x*b.z,
        a.x*b.y-a.y*b.x
    }
end

local function normalize_vector(a)  -- !
    return multi_vector(a, 1/math.sqrt(dot_prod_vector(a, a)))
end

G = {247570,280596,280600,249748,18578,18577,231184,16,16}

local function random()
    return math.random(0, 1)
end

local function trace(o, d, t, n)
    t = 1e9
    local m = 0
    local p = -o.z/d.z
    if 0.01<p then
        t = p
        n = {x=0, y=0, z=1}
        m = 1
    end

    for k=19,0,-1 do
    for j=9,0,-1 do
        if bit32.extract(G[j], k) then
            p = add_vector(o, {x=-k, y=0, z=-j-4})
            b = dot_prod_vector(p, d)
            c = dot_prod_vector(p, p) - 1
            q = dot_prod_vector(b, b) - c
            if q>0 then
                s = -b-math.sqrt(q)
                if s<t and s>0.01 then
                    t = s
                    n = normalize_vector(add_vector(p, multi_vector(d, t)))
                    m = 2
                end
            end
        end
    end
    end
    return m
end

local function sample (o, d)
    t = nil
    n = {}
    m = trace(o, d, t, n)

    if m==0 then
        return multi_vector({x=0.7, y=0.6, z=1}, math.pow(1-d.z, 4))
    end

    h = add_vector(o, multi_vector(d, t))
    l = normalize_vector(add_vector({x=9+random(), y=9+random(), z=16}, multi_vector(h, -1)))
    r = add_vector(d, multi_vector(n, (dot_prod_vector(n,  multi_vector(d, -2)))))

    b = dot_prod_vector(l, n)

    if b<0 or trace(h, l, t, n) then
        b = 0
    end
    

    if b>0 then bholder = 1 else bholder = 0 end  -- Custom
    p = math.pow(dot_prod_vector(l, multi_vector(r, bhodler)), 99)

    if m==1 then
        h = multi_vector(h, 0.2)

        if bit32.band((math.ceil(h.x) + math.ceil(h.y)), 1) then vholder = {x=3, y=1, z=1} else vholder = {x=3, y=3, y=3} end  -- Custom
        return multi_vector(vholder, b*0.2 + 0.1)
    end

    return add_vector({x=p, y=p, z=p}, multi_vector(sample(h, r) * 0.5))
end


local function main ()
    encode = "P6 512 512 255 "
    g = normalize_vector({x=-6, y=-16, z=0})
    a = multi_vector(normalize_vector(cross_prod_vector({x=0, y=0, z=1}, g)), 0.002)
    b = multi_vector(normalize_vector(cross_prod_vector(g, a)), 0.002)
    c = add_vector(multi_vector(add_vector(a, b), -256), g)

    for y=512,0,-1 do
    for x=512,0,-1 do
        p = {13, 13, 13}

        for r=64,0,-1 do
            t = add_vector(multi_vector(multi_vector(a, (random()-0.5)), 99), multi_vector(multi_vector(b, (random()-0.5)), 99))
            p = add_vector(multi_vector(sample(
                add_vector({x=17, y=16, z=8}, t),
                normalize_vector(add_vector(multi_vector(t, -1), multi_vector((add_vector(add_vector(multi_vector(a, (random()+x)), multi_vector(b, (y+random()))), c)), 16)))
            ), 3.5), p)
        end
        encode = encode..p.x..p.y..p.z
    end
    end
end
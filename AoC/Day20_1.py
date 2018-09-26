
import string
from timeit import default_timer as timer
start = timer()




class dpoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a
        self.distance = None

def updateDistance(particle):
    particle.distance = abs(particle.p.x) + abs(particle.p.y) + abs(particle.p.z)

def move(particle):
    particle.v.x += particle.a.x
    particle.v.y += particle.a.y
    particle.v.z += particle.a.z
    particle.p.x += particle.v.x
    particle.p.y += particle.v.y
    particle.p.z += particle.v.z

particles = []

with open('Day20_input.txt') as f:
    data = f.readlines()
for d in data:
    d = d.replace('\n','')
    print(d)
    d = d.replace('<','')
    d = d.replace('>','')
    d = d.split(', ')
    p = d[0]
    p = p.replace('p=','')
    p = list(map(int, p.split(',')))
    p = dpoint(p[0],p[1],p[2])
    v = d[1]
    v = v.replace('v=','')
    v = list(map(int, v.split(',')))
    v = dpoint(v[0],v[1],v[2])
    a = d[2]
    a = a.replace('a=','')
    a = list(map(int, a.split(',')))
    a = dpoint(a[0],a[1],a[2])
    part = particle(p,v,a)
    particles.append(part)
#p=<4170,-2482,2893>, v=<-135,-63,-125>, a=<0,9,2>
print(particles[0].distance)
for p in particles:
    updateDistance(p)

print(particles[0].distance)

for p in particles:
    move(p)
    updateDistance(p)

print(particles[0].distance)

while True:
    closest = 999999999
    closestNo = 0
    for i in range(len(particles)):
        updateDistance(particles[i])
        if (closest > particles[i].distance):
            closest = particles[i].distance
            closestNo = i
        move(particles[i])
    print(closestNo,':',closest)


end = timer()
print("Time elapsed: ",end - start)
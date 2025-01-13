s1={5,6,8,2,4,5,9}
s2={1,2,5,3,2,4,7,1,8}

s2.add(10)
print(s2)

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

s3={"book","bottle", "laptop","bag"}
print(s1.union(s3))
group1 = {"Marta", "Basia", "Wanda"}
group2 = {"Irek", "Marta", "Wojtek"}

g1_but_not_g2 = group1.difference(group2)

g2_but_not_g1 = group2.difference(group1)

print(g1_but_not_g2)
print(g2_but_not_g1)

not_in_g1_neither_g2= group1.symmetric_difference(group2)

print(not_in_g1_neither_g2)

in_g1_and_g2 = group1.intersection(group2)
print(in_g1_and_g2)

all_groups = group1.union(group2)

print(all_groups)

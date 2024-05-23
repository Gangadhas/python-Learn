name=["John","David","Sumon","Sundar"]
print([f"{x} vs {y}" for x in name for y in name if x!=y ])

score=[33,44,55,66]
print({f"{name[i]}:{score[i]}" for i in range(4)})

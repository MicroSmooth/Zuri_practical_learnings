# %%

with open("story.txt", "r") as f:
    content = f.read() .splitlines()
print(content)

for word in content:
    print(len(word))

#%%
file = open('story.txt', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words:', len(per_word))

# %%
from collections import Counter

def count_word(file_name):
        with open(file_name) as f:
                return Counter(f.read().split())

print("Frequency :",count_word("story.txt"))
def remove_deplicates(word):
     new_string = ' '.join(sorted(set(word)))
     removed_len = len(word) - len(new_string)
     return new_string, removed_len
n = "refuge wise"
print remove_deplicates(n)

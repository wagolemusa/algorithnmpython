def remove_deplicates(word):
     new_string = ' '.join(sorted(set(word)))
     return new_string

n = "refuge wise"

print remove_deplicates(n)

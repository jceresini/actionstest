from git import Repo

repo = Repo(".")

cur = repo.remote().fetch()
cur = repo.remote().repo.commit("origin/main")
last = repo.commit("main")

x = cur.tree.blobs[0]
print(x.path)

exit()

print(cur, "..", last)

d = cur.diff(last)

for x in d:
    print(x.change_type, x.b_path)

import glob

# /Users/shigeho/Documents/GitHub/vivito_renew/src/assets/css

org = "/Users/shigeho/Documents/GitHub/vivito_renew/src/assets/css/style.css"
new = "/Users/shigeho/Documents/GitHub/vivito_renew/src/assets/css/style_new.css"

file = open(new)
contents = file.read()
contents_all = contents.split()
print(contents_all.count('}'))
file.close()

file = open(org)
contents = file.read()
contents_all = contents.split()
print(contents_all.count('}'))
file.close()



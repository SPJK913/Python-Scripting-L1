urls=["www.annauniv.edu","www.google.com","www.ndtv.com","www.website.org","www.bis.org.in","www.rbi.org.in"]
def myfun(s):
  return list(reversed(s.split('.')))
print(sorted(urls,key=myfun))

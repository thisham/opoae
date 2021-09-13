def forLoop():
  anggota = ["hamdan", "rifqi", "hana"]
  for name in anggota:
    print(name)

def whileLoop():
  i = 4
  while i < 10:
    print(i)
    i += 1

def cobaDir():
  anggota = ["hamdan", "rifqi", "hana"]
  dir(anggota)

class Opoae:
  hayo = 1321

  def opoyo():
    return "asdfg"
  
  def sembarang():
    return 123

# help

# forLoop()
# whileLoop()
# cobaDir()

print(dir(Opoae))
print(Opoae.hayo)

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
  def pair1(a, b):
    return a
  return pair(pair1)

def cdr(pair):
  def pair1(a, b):
    return b
  return pair(pair1)

def main():
  print(cdr(cons(3, 4)))
  print(car(cons(3, 4)))
  
if __name__ == "__main__":
  main()

#Truth Table Generator - www.101computing.net/truth-table-generator/

def truthTable(expression,inputs=2):
  print("Boolean Expression:")
  print("  X = " + expression.upper())
  expression = expression.lower()
  
  #replace Boolean Operators with bitwise operators
  expression = expression.replace("and","&")
  expression = expression.replace("xor","^")
  expression = expression.replace("or","|")
  expression = expression.replace("not","~")

  if inputs==3:
    print("  -----------------")
    print("  | A | B | C | X |")
    print("  -----------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          x = eval(expression)
          print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(x) + " |" )
          print("  -----------------")
    
 
##############################################

expression = "(NOT A AND NOT C) OR NOT B"
truthTable(expression,3)
expression = "((NOT A OR NOT B) AND (A OR NOT C) OR NOT B AND (B OR C))"
truthTable(expression,3)



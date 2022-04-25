#include <stdio.h>
#include <stdbool.h>

int main(){
int a,b,c;
int i = 0;
a = 0;
b = 0;
c = 0;
  for(a = 0;a < 2;a++){
  for(b = 0;b < 2;b++){
  for(c = 0;c < 2;c++){
if (((!a || !b)&&(a || !c)) || (!b && (b || c)) == (!a && !c) || !b)
i = i + 1;
}}}
if (i == 8) printf("True");
return 0;
}

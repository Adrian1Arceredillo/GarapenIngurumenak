
#include <stdio.h>
#include <string.h>

int main() {  
          
         int num1 = 0;
         int num2 = 1;
         int num3 = 0;
         const int azken_fibo = 10;
         
         printf(" %d", num2);	//imprime el primer n�mero fibonacci. Es decir, imprime el contenido de num1.
         
         int i = 2;		//como hemos imprimido num1, tenemos que seguir con el segundo n�mero fibonacci.
         
         while (i <= azken_fibo) { 	//partimos del segundo n�mero, hasta llegar al �ltimo (azken_fibo = 10)
         	
         	
		 	num3 = num1 + num2;
		 	
		 	printf(" %d", num3);
		 	
		 	num1 = num2;
		 	num2 = num3;
		 	
			++i;		          	
         	
		 }


}

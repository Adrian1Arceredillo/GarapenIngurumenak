

#include <stdio.h>      // Hau derrigorrezkoa da printf funtzioa exekutatzeko
int main(){    
    
    int num1, num2, num3;
    int batuketa;
    	    	
    	
        printf("Sartu zenbakiak: ");  //komila artekoa bistaratuko da pantailan 
        scanf("%d",&num1);
        
        printf("Sartu zenbakiak: ");  //komila artekoa bistaratuko da pantailan 
        scanf("%d",&num2);
        
        printf("Sartu zenbakiak: ");  //komila artekoa bistaratuko da pantailan 
        scanf("%d",&num3);
        
        batuketa = num1 + num2 + num3;
        printf("Batuketaren Emaitza: %d\n", batuketa);
        
        return 0;
        


} 

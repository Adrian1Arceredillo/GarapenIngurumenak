

#include <stdio.h>
#include <string.h>

int zenbakiarenPotentziaKalkulatu(int base, int exp) {
	int valorPotencia = 1;
	for (int i = 0; i < exp; ++i) {
		valorPotencia = valorPotencia * base;
	}
	return valorPotencia;
}


int main() {
	
	int zenbakia;
	int exponentea;
	
	printf("Sartu zenbakia (basea): ");
	scanf("%d", &zenbakia);
	
	printf("Sartu berretzailea (exponentea): ");
	scanf("%d", &exponentea);
	
	printf("%d",zenbakiarenPotentziaKalkulatu(zenbakia, exponentea));
		
}







/*el programa har� lo siguiente:
	* leer un n�mero
	* mostrar el siguiente men�:
		a) Calcular el factorial del n�mero
		b) Calcular la suma de los d�gitos del n�mero
		c) Mostrar� una cuenta atr�s desde el n�mero hasta el cero
*/


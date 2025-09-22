package Lista1;
import java.util.Scanner;

public class Q3 {
	public static void main(String[] args) { 
		Scanner scan = new Scanner(System.in);

		System.out.print("Quantos metros cubicos foram utilizados: ");
		int m3 = scan.nextInt();
		
		int valor = 0;
		int extra;
		
		if(m3<=10) {
			valor = 7;
		}else if(m3<=30){
			extra= m3-10;
			valor = 7 + extra;
		}else if(m3<=100){
			extra = m3 - 30;
			valor = 7 + 20 + (extra *2);
		}else if(m3<=120) {
			extra = m3 - 100;
			valor = 7 + 20 + 140 + (extra *5);
		}else {
			extra = m3 - 120;
			valor = 7 + 20 + 140 + 100 + (extra *5);
		}
		
		System.out.printf("Valor da conta será: R$%d,00",valor);
		scan.close();
	}
}


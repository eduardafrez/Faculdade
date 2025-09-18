package Lista1;
import java.util.Scanner;

public class Q4 {
	public static void main(String[] args) { 
		Scanner scan = new Scanner(System.in);

		System.out.print("digite um numero: ");
		int num = scan.nextInt();
		
		int cont = 0;
		int cont_2 = 0;
		
		while(cont<num){
			cont++;
			cont_2 = 0;
			while(cont_2<cont){
			System.out.print("*");
			++cont_2;
			}
			System.out.print("\n");
		}
		
		scan.close();
	}
}

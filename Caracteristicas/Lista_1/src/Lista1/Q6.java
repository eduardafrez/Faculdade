package Lista1;
import java.util.Scanner;

public class Q6 {
	public static void main(String[] args) { 
		Scanner scan = new Scanner(System.in);

		System.out.print("Digite um numero para verificar se é perfeito: ");
		int num = scan.nextInt();
		
		int soma = 0;
		
		for(int i = 1; i<num; i++) {
			if(num%i ==0) {
				soma += i;
			}
		}
		
		if(soma == num) {
			System.out.printf("O numero %d é um numero perfeito",num);
		}else {
			System.out.printf("O numero %d não é um numero perfeito",num);
		}

		scan.close();
	}
}


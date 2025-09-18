package Lista1;
import java.util.Scanner;

public class Q1 {
	public static void main(String[] args) { 
		Scanner scan = new Scanner(System.in);

		System.out.print("digite seu dia de nascimento: ");
		int dia = scan.nextInt();
		System.out.print("digite seu mes de nascimento: ");
		int mes = scan.nextInt();
		System.out.print("digite seu ano de nascimento(por exemplo: 1999): ");
		int ano = scan.nextInt();
		
		int numero = ((dia*100)+mes)+ano;
		int milhar_dezena = (numero - (numero%100))/100;
		int dezena_unidade = (numero%100);
		
		switch ((milhar_dezena + dezena_unidade)%5){
			case 0:
				System.out.println("Perfil tímido.");
				break;
			case 1:
				System.out.println("Perfil sonhador.");
				break;
			case 2:
				System.out.println("Perfil paquerador.");
				break;
			case 3:
				System.out.println("Perfil atraente.");
				break;
			default:
				System.out.println("Perfil irresistível.");
		}
		scan.close();
	}
}

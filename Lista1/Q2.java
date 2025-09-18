package Lista1;
import java.util.Scanner;

public class Q2 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("--- Verififação de Triangulo ---\nonde A é o maior lado");
		
		System.out.print("digite o lado A: ");
		int a = scan.nextInt();
		System.out.print("digite o lado B: ");
		int b = scan.nextInt();
		System.out.print("digite o lado C: ");
		int c = scan.nextInt();
		
		int quad_1 = a*a;
		int quad_2 = (b*b)+(c*c);
		
		if(a >= b +c ){
			System.out.print("Não forma um triangulo");
		}else if(quad_1 == quad_2){
			System.out.print("Temos um triângulo retângulo");
		}else if(quad_1 > quad_2){
			System.out.print("Temos um triângulo obtusângulo");
		}else{
			System.out.print("Temos um triângulo acutângulo");
		}
		
		scan.close();
	}
}

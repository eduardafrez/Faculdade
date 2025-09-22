package antes;

public class aula {
	public static void main(String[] args) { 
		String nome = "Eduarda";
		String sobrenome = new String("de oliveira");
		int tamanho_nome = nome.length();
		int posicao = 3;
		char caractere = nome.charAt(posicao);
		String part1 = nome.substring(posicao);
		String part2 = nome.substring(posicao,5);		
		
		System.out.println("nome: "+nome);
		System.out.println("sobrenome"+sobrenome);
		System.out.println("tamanho do nome: "+tamanho_nome);
		System.out.println("Na posição "+posicao+" esta o caractere :"+caractere);
		System.out.println("string após a posição "+posicao+" é: "+part1);
		System.out.println("string entre a posição "+posicao+" e 5 é: "+part2);
		System.out.println("\n\n-----------parte 2-------------\n\n");
		String frase = "Universidade";
		String frase2 = "universidade";
		
		
		boolean igualdade = frase.equals(frase2);		
		boolean igualdade_sem_diferenca = frase.equalsIgnoreCase(frase2);
		String minuscula = frase.toLowerCase();
		String maiuscula = frase2.toUpperCase();
		System.out.println("igualdade: "+igualdade);
		System.out.println("igualdade ignorando mai e min: "+igualdade_sem_diferenca);
		System.out.println("Frase minuscula: "+minuscula);
		System.out.println("Frase maiuscula: "+maiuscula);
		System.out.println("\n\n-----------parte 3-------------\n\n");
		String texto = " olá mundo ";
		String[] split = texto.trim().split(" ");
		System.out.println("Sem espaços de fora: "+texto.trim());
		System.out.println("Texto onde 'o' é substituido por 'i': "+texto.replace('o', 'i'));
		System.out.println("");
		for (String i : split) {
			System.out.println(i);
		}
	}
}

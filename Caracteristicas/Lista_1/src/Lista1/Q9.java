package Lista1;

public class Q9{
	public static void main(String[] args) { 
		int[] array = {1,2,3,4,5,6,7,8,12,23};
		int x = 35;
		
		verifica(array,x);
	}

	static void verifica(int s[], int x) {
		int zero = 0;
		
		for(int i = 0; i < s.length - 1 ;++i) {
			int soma = s[i] + s[i+1];
			if(soma == x){
				System.out.printf("Par encontrado: %d (índice %d) e %d (índice %d).\n" ,s[i],i,s[i+1],(i+1));
				zero++;
			}
		}
		if (zero==0){
			System.out.println("Nenhum par consecutivo encontrado.");
		}
	}
}
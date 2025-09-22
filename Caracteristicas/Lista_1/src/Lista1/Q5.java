package Lista1;

public class Q5 {
	public static void main(String[] args) { 
		int num = 8;
		String a = "* * * * * * *";
		
		for(int i=0 ; i<num ; i++) {
			if(i%2==0){
				System.out.println(a);
			}else{
				System.out.println(" "+a);
			}
		}
	}
}

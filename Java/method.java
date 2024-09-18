import java.util.Scanner;
public class method {
  Scanner sc=new Scanner(System.in);
  void add(){
  int a=sc.nextInt();
  int b=sc.nextInt();
  int sum=a+b;
  System.out.println(sum);

}
public static void main(String[] args) {
    method obj=new method();
    obj.add();
}
}

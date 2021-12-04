
public class permutatedMultiples{
    public static void main(String[] args){
        for(int i=1;i<500000;i++){
            
        }
        System.out.println("Worki9ngh");
        func(1234343);
    }

    static void func(int i){
        if(i<10){
            System.out.print(i+" ");
        }
        else {
            func(i/10);
            System.out.print(i%10+" ");
        }
        
    }

}
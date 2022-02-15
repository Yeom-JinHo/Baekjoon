import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_6603 {
  static int[] numbers;
  static int[] result;
  static int N,R;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    while(true){
      st=new StringTokenizer(br.readLine());
      N=Integer.parseInt(st.nextToken());
      if(N==0)
        break;
      numbers=new int[N];
      result=new int[N];
      R=6;
      for(int i=0;i<N;i++){
        numbers[i]=Integer.parseInt(st.nextToken());
      }
      comb(0,0);
      System.out.println();
    }
  }
  static void comb(int cnt,int start){
    if(cnt==R){
      for(int i=0;i<R;i++){
        System.out.print(result[i]+" ");
      }
      System.out.println();
    }
    else{
      for(int i=start;i<N;i++){
        result[cnt]=numbers[i];
        comb(cnt+1,i+1);
      }
    }
  }
}

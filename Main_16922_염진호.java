import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_16922_염진호{
  static int N,result;
  static int arr[]={1,5,10,50};
  static int tmp[];
  static boolean chk[]=new boolean[1000+1];
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    tmp=new int[N];
    result=0;
    comb(0,0);
    for(int i=0;i<=1000;i++){
      if(chk[i]){
        result+=1;
      }
    }
    bw.write(String.valueOf(result));
    bw.flush();
    bw.close();
    br.close();
  }

  static void comb(int cnt,int start){
    if(cnt==N){
      int sum=0;
      for(int i=0;i<N;i++){
        sum+=tmp[i];
      }
      chk[sum]=true;
    }else{
      for(int i=start;i<4;i++){
        tmp[cnt]=arr[i];
        comb(cnt+1,i);
      }
    }
  }
}
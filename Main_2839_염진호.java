import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_2839_염진호 {
  static int N,result;
  static int[] arr={5,3};
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    result=Integer.MAX_VALUE;
    comb(0,0,0);
    if(result==Integer.MAX_VALUE)
      bw.write("-1"+"\n");
    else
      bw.write(result+"\n");
    bw.flush();
    bw.close();
    br.close();
  }

  static void comb(int cnt, int start,int total){
    if(total==N){
      result=cnt;
    }
    else if(total<N && result==Integer.MAX_VALUE){
      for(int i=start;i<2;i++){
        comb(cnt+1,i,total+arr[i]);
      }
    }
  }
}
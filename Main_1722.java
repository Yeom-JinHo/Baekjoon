import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1722 {
  static StringBuilder sb;
  static int N,K,count,com;
  static int[] arr,arr2,result;
  static Boolean[] chk;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    st=new StringTokenizer(br.readLine());
    sb=new StringBuilder();
    arr=new int[N];
    arr2=new int[N];
    result=new int[N];
    chk=new Boolean[N];
    Arrays.fill(chk, false);
    count=0;
    com=Integer.parseInt(st.nextToken());
    if(com==1){
      K=Integer.parseInt(st.nextToken());
    }else if(com==2){
      for(int i=0;i<N;i++){
        arr2[i]=Integer.parseInt(st.nextToken());
      }
    }
    for(int i=0;i<N;i++){
        arr[i]=i+1;
    }
    per(0);
    bw.write(sb.toString());
    bw.flush();
    bw.close();
    br.close();
  }
  static void per(int cnt){
    if(cnt==N){
        count+=1;
      if(com==1 && count==K){
        for(int i=0;i<N;i++){
          sb.append(result[i]).append(" ");
        }
        return;
      }else if(com==2){
        if(Arrays.equals(result, arr2)){
          sb.append(count);
          return;
        }
      }
    }else{
      for(int i=0;i<N;i++){
        if(!chk[i]){
          chk[i]=true;
          result[cnt]=arr[i];
          per(cnt+1);
          chk[i]=false;
        }
      }
    }
  }
}
// 순열의 순서 다시
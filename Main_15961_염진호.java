import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_15961_염진호{
  static int N,D,K,C;
  static int[] arr;
  static int[] chk;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    D=Integer.parseInt(st.nextToken());
    K=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    arr=new int[N];
    chk=new int[D+1];
    
    for(int i=0;i<N;i++){
      st=new StringTokenizer(br.readLine());
      arr[i]=Integer.parseInt(st.nextToken());
    }
    int eatingCount=0;
    for(int i=0;i<K;i++){
      if(chk[arr[i]]==0)
        eatingCount+=1;
      chk[arr[i]]+=1;
    }
    int answer=eatingCount;
    int start=0;
    int end=K-1;
    for(int i=0;i<N;i++){
      chk[arr[start]]-=1;
      if(chk[arr[start]]==0){
        eatingCount-=1;
      }
      start+=1;
      end=(end+1)%N;
      chk[arr[end]]+=1;
      if(chk[arr[end]]==1){
        eatingCount+=1;
      }
      if(chk[C]==0)
        answer=Math.max(answer, eatingCount+1);
      else
        answer=Math.max(answer,eatingCount);
    }
    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }
}
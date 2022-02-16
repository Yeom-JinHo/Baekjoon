import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_2138_염진호{
  static int result1,result2;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st =new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int[] nowLights= new int[N+2];
    int[] answer= new int[N+2];
    int[] tmp =new int[N+2];

    st = new StringTokenizer(br.readLine());
    String inp =st.nextToken();
    for(int i=1;i<=N;i++){
      nowLights[i]=inp.charAt(i-1)-'0';
    }
    st = new StringTokenizer(br.readLine());
    inp =st.nextToken();
    for(int i=1;i<=N;i++){
      answer[i]=inp.charAt(i-1)-'0';
    }
    tmp=nowLights.clone();
    // 그리디로 
    // 1번째가 눌린상태라면? 앞만 확인하자.
    result1=1;
    tmp[1]=(tmp[1]==1) ? 0 : 1;
    tmp[2]=(tmp[2]==1) ? 0 : 1;
    for(int i=2;i<=N;i++){
      if (tmp[i-1]!=answer[i-1]){
        tmp[i-1]=(tmp[i-1]==1) ? 0 : 1;
        tmp[i]=(tmp[i]==1)? 0 :1;
        tmp[i+1]=(tmp[i+1]==1)? 0 :1;
        result1+=1;
      }
      if(i==N){
        if(tmp[i]!=answer[i]){
          result1=-1;
        }
      }
    }
    //1번째가 안눌린 상태라면?
    result2=0;
    tmp=nowLights.clone();
    for(int i=2;i<=N;i++){
      if (tmp[i-1]!=answer[i-1]){
        tmp[i-1]=(tmp[i-1]==1) ? 0 : 1;
        tmp[i]=(tmp[i]==1)? 0 :1;
        tmp[i+1]=(tmp[i+1]==1)? 0 :1;
        result2+=1;
      }
      if(i==N){
        if(tmp[i]!=answer[i]){
          result2=-1;
        }
      }
    }
    if (result1>=0 && result2>=0){
      bw.write(Math.min(result1, result2)+"\n");
    }else if (result1<0 && result2<0){
      bw.write(-1+"\n");
    }else{
      bw.write(Math.max(result1, result2)+"\n");
    }
    bw.flush();
    bw.close();
    br.close();
  }
}
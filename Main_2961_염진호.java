import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_2961_염진호 {
  static int N,result;
  static int[][] source,tmp;
  static boolean[] chk;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken()); 
    source=new int[N][2];
    chk=new boolean[N];
    for(int i=0;i<N;i++){
      st=new StringTokenizer(br.readLine());
      source[i][0]=Integer.parseInt(st.nextToken());
      source[i][1]=Integer.parseInt(st.nextToken());
    }
    result=Integer.MAX_VALUE;
    subset(0,1,0);
    bw.write(String.valueOf(result)+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static void subset(int cnt,int sour,int bitter){
    if(cnt==N){
      int notChk=0;
      for(int i=0;i<N;i++){
        if(!chk[i])
          notChk++;
      }
      if(notChk!=N)
        result=Math.min(result,Math.abs(sour-bitter));
      return;
    }
    chk[cnt]=true;
    subset(cnt+1,sour*source[cnt][0],bitter+source[cnt][1]);
    chk[cnt]=false;
    subset(cnt+1,sour,bitter);
  }
}
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_1074_염진호{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());
    int N=Integer.parseInt(st.nextToken());
    int R=Integer.parseInt(st.nextToken());
    int C=Integer.parseInt(st.nextToken());
    //  td 위인지 아랜지 , lr 왼쪽인지 오른쪽인지 , starNum 
    int td;
    int lr;
    int len;
    int startNum=0;
    for(int i=N;i>0;i--){
      len =(int)Math.pow(2,i-1);
      td = R>=len? 1 : 0;
      lr = C>=len? 1 : 0;
      int rr=(int)Math.pow(2,2*i-1)*td;
      int cc=(int)Math.pow(2,2*i-2)*lr;
      startNum+=rr+cc;
      R-=len*td;
      C-=len*lr;
    }
    bw.write(startNum+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
}
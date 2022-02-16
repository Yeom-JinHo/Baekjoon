import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Main_1992_염진호{
  static int[][] arr;
  static StringBuilder sb;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    sb=new StringBuilder();
    int N =Integer.parseInt(br.readLine());
    arr=new int[N][N];
    for(int i=0;i<N;i++){
      String line=br.readLine();
      for(int j=0;j<N;j++){
        arr[i][j]=line.charAt(j)-'0';
      }
    }
    div(0,0,N);
    bw.write(sb.toString()+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  
  static void div(int r,int c,int len){
    if(len==1){
      sb.append(arr[r][c]);
    }else{
      int type=arr[r][c];
      boolean flag=true;
      for(int rr=0;rr<len;rr++){
        for(int cc=0;cc<len;cc++){
          if(type!=arr[r+rr][c+cc]){
            flag=false;
          }
        }
      }
      if(flag){
        sb.append(type);
      }else{
        sb.append("(");
        int n=len/2;
        div(r,c,n);
        div(r,c+n,n);
        div(r+n,c,n);
        div(r+n,c+n,n);
        sb.append(")");
      }
      
    }
  }
}
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Main_3040_염진호{
  static int[] arr=new int[9];
  static boolean[] chk=new boolean[9];
  static StringBuilder sb= new StringBuilder();
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));  
    for(int i=0; i<9;i++){
      arr[i]=Integer.parseInt(br.readLine());
    }
    subset(0);
    bw.write(String.valueOf(sb));
    bw.flush();
    bw.close();
    br.close();
  }
  static void subset(int cnt){
    if(cnt==9){
      int sum=0;
      int chkCount=0;
      for(int i=0;i<9;i++){
        if(chk[i]){
          sum+=arr[i];
          chkCount+=1;
        }
      }
      if(sum==100 && chkCount==7){
        for(int i=0;i<9;i++){
          if(chk[i])
            sb.append(arr[i]+"\n");
        }
      }
    }else{
      chk[cnt]=true;
      subset(cnt+1);
      chk[cnt]=false;
      subset(cnt+1);
    }
  }
}
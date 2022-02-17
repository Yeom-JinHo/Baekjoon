import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_3109_염진호{
  static int R,C,answer;
  static char[][] arr;
  static boolean[][] chk;
  static int[] dr={-1,0,1};
  static int[] dc={1,1,1};
  static int[] choice;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    R=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    arr =new char[R][C];
    chk =new boolean[R][C];
    choice=new int[R];
    for(int r=0;r<R;r++){
      st=new StringTokenizer(br.readLine());
      arr[r]=st.nextToken().toCharArray();
    }
    answer=0;
    for(int r=0;r<R;r++){
      findPipePath(r, 0);
    }
    bw.write(answer+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  //경로 찾기
  static boolean findPipePath(int r,int c){
    if(c==C-1){
      answer+=1;
      return true;
    }else{
      for(int i=0;i<3;i++){
        int tr=r+dr[i];
        int tc=c+dc[i];
        if (tr>=0 && tc>=0 && tr<R && tc<C){
          if(arr[tr][tc]=='.' && !chk[tr][tc]){
            chk[tr][tc]=true;
            if(findPipePath(tr, tc)){
              return true;
            };
          }
        }
      }
    }
    return false;
  }
}

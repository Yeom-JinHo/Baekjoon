import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Main_2239_염진호{
  static int arr[][]=new int[9][9];
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    for(int r=0;r<9;r++){
      String line =br.readLine();
      for(int c=0;c<9;c++){
        arr[r][c]=line.charAt(c)-'0';
      }
    }
    dfs(0);
    bw.flush();
    bw.close();
    br.close();
  }
  static void dfs(int ind){
    if(ind==9*9){
      for(int r=0;r<9;r++){
        for(int c=0;c<9;c++){
          System.out.print(arr[r][c]);
        }
        System.out.println();
      }
      System.exit(0);
    }
    int r=(int)Math.floor(ind/9);
    int c=ind%9;
    if(arr[r][c]==0){
      for(int i=1;i<=9;i++){
        if(ableInsert(r, c, i)){
          arr[r][c]=i;
          dfs(ind+1);
          arr[r][c]=0;
        }
      }
    }else{
      dfs(ind+1);
    }
  }
  static boolean ableInsert(int sr,int sc,int value){
    for(int r=0;r<9;r++){
      if(arr[r][sc]==value){
        return false;
      }
    }

    for(int c=0;c<9;c++){
      if(arr[sr][c]==value){
        return false;
      }
    }
    int boxStartR=sr-sr%3;
    int boxStartC=sc-sc%3;
    for(int r=boxStartR;r<boxStartR+3;r++){
      for(int c=boxStartC;c<boxStartC+3;c++){
        if(arr[r][c]==value){
          return false;
        }
      }
    }

    return true;
  }
}
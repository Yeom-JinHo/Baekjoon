import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_17413_염진호{
  static class Shark{
    int speed;
    int dir;
    int size;
    public Shark(int speed,int dir,int size){
      this.speed=speed;
      this.dir=dir;
      this.size=size;
    }
  }
  static int R,C,M;
  static Shark[][] arr;
  static int[] dr ={0,-1,1,0,0};
  static int[] dc ={0,0,0,1,-1};
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    R=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    M=Integer.parseInt(st.nextToken());

    arr=new Shark[R+1][C+1];

    for(int i=0;i<M;i++){
      st=new StringTokenizer(br.readLine());
      int r=Integer.parseInt(st.nextToken());
      int c=Integer.parseInt(st.nextToken());
      int s=Integer.parseInt(st.nextToken());
      int d=Integer.parseInt(st.nextToken());
      int z=Integer.parseInt(st.nextToken());
      arr[r][c]=new Shark(s,d,z);
    }

    int answer=0;
    for(int c=1;c<=C;c++){
      for(int r=1;r<=R;r++){
        if(arr[r][c]!=null){
          answer+=arr[r][c].size;
          arr[r][c]=null;
          break;
        }
      }
      moveShark();
    }
    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }
  static void moveShark(){
    Shark[][] nextArr=new Shark[R+1][C+1];
    for(int r=1;r<=R;r++){
      for(int c=1;c<=C;c++){
        if(arr[r][c]!=null){
          Shark nowShark=arr[r][c];
          int tr=r;
          int tc=c;
          for(int i=0;i<nowShark.speed;i++){
            int nr=tr+dr[nowShark.dir];
            int nc=tc+dc[nowShark.dir];
            if(nr>=1 && nc>=1 && nr<=R && nc<=C){
              tr=nr;
              tc=nc;
            }else{
              nowShark.dir=switchDirection(nowShark.dir);
              i--;
            }
          }
          if(nextArr[tr][tc]!=null){
            Shark nextShark =nextArr[tr][tc];
            if(nextShark.size<nowShark.size){
              nextArr[tr][tc]=new Shark(nowShark.speed, nowShark.dir, nowShark.size);
            }
          }else{
            nextArr[tr][tc]=new Shark(nowShark.speed, nowShark.dir, nowShark.size);
          }
        }
      }
    }
    for(int r=0;r<=R;r++){
      for(int c=0;c<=C;c++){
        arr[r][c]=nextArr[r][c];
      }
    }
  }
  static int switchDirection(int nowdir){
    switch(nowdir){
      case 1:
        return 2;
      case 2:
        return 1;
      case 3:
        return 4;
      case 4:
        return 3;
    }
    return -1;
  }
}
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

class Main_17144_염진호{
  static int R,C,T;
  static int[][] arr;
  static List<Point> ac;
  static int[] dr={-1,0,1,0};
  static int[] dc={0,1,0,-1};
  static class Point{
    int r;
    int c;
    public Point(int r,int c){
      this.r=r;
      this.c=c;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    R=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    T=Integer.parseInt(st.nextToken());
    arr=new int[R][C];
    ac=new LinkedList<>();

    // 입력받고 공기청정기는 따로 뺀다.
    for(int r=0;r<R;r++){
      st=new StringTokenizer(br.readLine());
      for(int c=0;c<C;c++){
        arr[r][c]=Integer.parseInt(st.nextToken());
        if(arr[r][c]==-1){
          ac.add(new Point(r,c));
        }
      }
    }

    // T번만큼 확산 후 돌리기, top/bottom 구분하여 구현

    for(int t =0;t<T;t++){
      spread();
      rotate(ac.get(0),true);
      rotate(ac.get(1),false);
    }

    // 다 돌고 난뒤 남은 미세먼지 구하기
    int answer=0;
    for(int r=0;r<R;r++){
      for(int c=0;c<C;c++){
        if(arr[r][c]>0){
          answer+=arr[r][c];
        }
      }
    }

    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }

  // 확산
  // dr,dc를 이용하여 for문을 돈 뒤에 확산지를 감소시켜주었고,
  // (다른 곳에 영향받으면 안되기에 tmp라는 임시 배열을 두었다)
  static void spread(){
    int[][] tmp=new int[R][C];
    for(int r=0;r<R;r++){
      for(int c=0;c<C;c++){
        if(arr[r][c]>0){
          int count=0;
          for(int i=0;i<4;i++){
            int tr=r+dr[i];
            int tc=c+dc[i];
            if(tr>=0 && tr<R& tc>=0 && tc<C){
              if(arr[tr][tc]!=-1){
                count+=1;
                tmp[tr][tc]+=Math.round(arr[r][c]/5);
              }
            }
          }
          tmp[r][c]-=Math.round(arr[r][c]/5)*count;
        }
      }
    }

    //확산이 끝난 후에는 진짜 배열에 반영시켜준다.
    for(int r=0;r<R;r++){
      for(int c=0;c<C;c++){
        arr[r][c]+=tmp[r][c];
      }
    }
  }

  // 시계방향 반시계방향으로 돈다.
  // 값을 보존해야하기에 에어컨부터 빨아드리는 식으로 구현하였다.

  static void rotate(Point ac,boolean top){
    int minR;
    int maxR;
    int flag =top?1:-1;
    if(top){
      minR=0;
      maxR=ac.r+1;
    }else{
      minR=ac.r;
      maxR=R;
    }
    int i=0;
    int r=ac.r+dr[i]*flag;
    int c=ac.c+dc[i];
    int tr;
    int tc;
    while(true){
      tr=r+dr[i]*flag;
      tc=c+dc[i];
      if(tr==ac.r && tc==ac.c){
        arr[r][c]=0;
        break;
      }
      if(tr>=minR && tr<maxR && tc>=0 && tc<C){
        arr[r][c]=arr[tr][tc];
        r=tr;
        c=tc;
      }else{
        i=(i+1)%4;
      }
    }
    
  }
}
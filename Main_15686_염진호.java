import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_15686_염진호{
  static int N,M,answer;
  static int[][] houseArr,choiceChicken;
  static ArrayList<int[]> chickenList;
  static boolean[][] chk;
  static int[] dr={-1,1,0,0};
  static int[] dc={0,0,-1,1};
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    M=Integer.parseInt(st.nextToken());
    houseArr=new int[N][N];
    chickenList=new ArrayList<>();
    choiceChicken=new int[M][2];
    answer=Integer.MAX_VALUE;
    for(int r=0;r<N;r++){
      st=new StringTokenizer(br.readLine());
      for(int c=0;c<N;c++){
        int input=Integer.parseInt(st.nextToken());
        if(input==2){
          chickenList.add(new int[]{r,c});
        }else{
          houseArr[r][c]=input;
        }
      }
    }
    comb(0,0);

    bw.write(answer+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static void comb(int cnt,int start){
    if(cnt==M){
      bfs(choiceChicken);
    }else{
      for(int i=start;i<chickenList.size();i++){
        choiceChicken[cnt]=chickenList.get(i);
        comb(cnt+1,i+1);
      }
    }
  }
  static void bfs(int[][] choiceChicken){
    Queue <int[]> que= new LinkedList<>();
    chk=new boolean[N][N];
    for(int i=0;i<choiceChicken.length;i++){
      que.add(new int[]{choiceChicken[i][0],choiceChicken[i][1],choiceChicken[i][0],choiceChicken[i][1]});
    }
    int tmpAnswer=0;
    while(!que.isEmpty()){
      int[] chicken=que.poll();
      int r=chicken[0];
      int c=chicken[1];
      int cr=chicken[2];
      int cc=chicken[3];
      chk[r][c]=true;

      for(int i=0;i<4;i++){
        int tr=r+dr[i];
        int tc=c+dc[i];
        if(tr>=0 && tc>=0 && tr<N && tc<N){
          if(!chk[tr][tc]){
            que.add(new int[]{tr,tc,cr,cc});
            chk[tr][tc]=true;
            if(houseArr[tr][tc]==1){
              tmpAnswer+=Math.abs(tr-cr)+Math.abs(tc-cc);
            }
          }
        }
      }
    }
    answer=Math.min(tmpAnswer,answer);
  }
}
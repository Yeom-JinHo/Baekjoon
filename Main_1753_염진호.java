import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Main_1753_염진호{
  static int V,E;
  static int[][] arr;
  static ArrayList<ArrayList<int[]>> eList;
  static boolean[] chk;
  static int[] wList;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    V=Integer.parseInt(st.nextToken());
    E=Integer.parseInt(st.nextToken());
    eList=new ArrayList<>();
    for(int i=0;i<V;i++){
      eList.add(new ArrayList<int[]>());
    }
    chk=new boolean[V];
    wList=new int[V];

    st=new StringTokenizer(br.readLine());
    int start=Integer.parseInt(st.nextToken());

    for(int i=0;i<E;i++){
      st=new StringTokenizer(br.readLine());
      int u=Integer.parseInt(st.nextToken());
      int v=Integer.parseInt(st.nextToken());
      int w=Integer.parseInt(st.nextToken());
      eList.get(u-1).add(new int[]{v-1,w});
    }
    dijkstra(start-1);
    for(int i=0;i<V;i++){
      if(wList[i]==Integer.MAX_VALUE){
        bw.write("INF"+"\n");
      }else{
        bw.write(wList[i]+"\n");
      }
    }
    bw.flush();
    bw.close();
    br.close();
  }
  static void dijkstra(int start){
    Arrays.fill(wList,Integer.MAX_VALUE);
    wList[start]=0;
    for(int k=0;k<V;k++){
      int minW=Integer.MAX_VALUE;
      int minInd=0;
      for(int i=0;i<V;i++){
        if(!chk[i] && minW>wList[i]){
          minW=wList[i];
          minInd=i;
        }
      }
      chk[minInd]=true;
      for(int i=0;i<eList.get(minInd).size();i++){
        int[] relateE=eList.get(minInd).get(i);
        if(!chk[relateE[0]] && relateE[1]!=0){
          wList[relateE[0]]=Math.min(wList[relateE[0]],wList[minInd]+relateE[1]);
        }
      }
    }
  }
}


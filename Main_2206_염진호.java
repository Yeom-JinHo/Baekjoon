// import java.io.BufferedReader;
// import java.io.BufferedWriter;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.io.OutputStreamWriter;
// import java.sql.Blob;
// import java.util.LinkedList;
// import java.util.Queue;
// import java.util.StringTokenizer;

// class Main{
//   static int[][] arr;
//   static int R,C;
//   static int[] dr={0,0,-1,1};
//   static int[] dc={-1,1,0,0};
//   static class Node{
//     int r;
//     int c;
//     int cnt;
//     boolean broke;
//     public Node(int r,int c,int cnt,boolean broke){
//       super();
//       this.r=r;
//       this.c=c;
//       this.cnt=cnt;
//       this.broke=broke;
//     }
//   }
//   public static void main(String[] args) throws IOException{
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     StringTokenizer st = new StringTokenizer(br.readLine());
//     R=Integer.parseInt(st.nextToken());
//     C=Integer.parseInt(st.nextToken());
//     arr=new int[R][C];
//     for(int r=0;r<R;r++){
//       String line=br.readLine();
//       for(int c=0;c<C;c++){
//         arr[r][c]=line.charAt(c)-'0';
//         // System.out.print(arr[r][c]);
//       }
//       // System.out.println();
//     }
//     bw.write(dfs()+"\n");
//     bw.flush();
//     bw.close();
//     br.close();
//   }
//   static int dfs(){
//     boolean[][][] chk=new boolean[R][C][2];
//     // int[][] distance=new int[R][C];
//     Queue<Node> que=new LinkedList<>();
//     que.add(new Node(0,0,1,false));
//     chk[0][0][0]=true;
//     chk[0][0][1]=true;
//     while(!que.isEmpty()){
//       Node current=que.poll();
//       if(current.r==R-1 && current.c==C-1)
//         return current.cnt;
//       for(int i=0;i<4;i++){
//         int tr=current.r+dr[i];
//         int tc=current.c+dc[i];
//         if(tr>=0 && tc>=0 && tr<R && tc<C){
//           // System.out.printf("r %d c %d tr %d tc %d broke%d nextArr %d\n",current.r,current.c,tr,tc,current.broke,arr[tr][tc]);
//           if(current.broke){
//             if(!chk[tr][tc][1]){
//               if(arr[tr][tc]==0){
//                 que.add(new Node(tr,tc,current.cnt+1,current.broke));
//               }
//             }
//           }else{
//             if(!chk[tr][tc][0]){
//               if(arr[tr][tc]==0){
//                 que.add(new Node(tr,tc,current.cnt+1,current.broke));
//               }else{
//                 que.add(new Node(tr,tc,current.cnt+1,true));
//               }
//             }
//           }
//           // if(!chk[tr][tc]){
            
//           //   if(arr[tr][tc]==1 && current.broke>=1){
//           //     continue;
//           //   }
            
//           //   chk[tr][tc]=true;
//           //   que.add(new Node(tr,tc,current.cnt+1,current.broke+arr[tr][tc]));
//           // }
//         }
//       }
//     }
//     return -1;
//   }
// }
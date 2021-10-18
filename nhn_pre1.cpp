#include <iostream>
#include <list>
using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int len;
int map[99][99];
int dfs(int row, int col)
{
  int count = 1;
  map[row][col] = -1;
  for (int di = 0; di < 4; di++)
  {
    int ddx = col + dx[di];
    int ddy = row + dy[di];
    if (ddx >= 0 && ddx < len)
    {
      if (ddy >= 0 && ddy < len)
      {
        if (map[ddy][ddx] == 1)
          count += dfs(ddy, ddx);
      }
    }
  }
  return count;
}
int main()
{
  list<int> answer;
  cin >> len;
  for (int row = 0; row < len; row++)
  {
    for (int col = 0; col < len; col++)
    {
      cin >> map[row][col];
    }
  }
  for (int row = 0; row < len; row++)
  {
    for (int col = 0; col < len; col++)
    {
      if (map[row][col] == 1)
      {
        answer.push_back(dfs(row, col));
      }
    }
  }
  //for(int row=0;row<len;row++){
  //    for(int col=0;col<len;col++){
  //        cout<< map[row][col]<<' ';
  //    }
  //    cout<<'\n';
  //}
  answer.sort();
  cout << answer.size() << '\n';
  if (answer.size() != 0)
  {
    for (int item : answer)
    {
      cout << item << ' ';
    }
  }

  return 0;
}

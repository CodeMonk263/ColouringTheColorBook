#include<bits/stdc++.h>
using namespace std;
#define int long long

int grid[105][105];
pair<int,int> points[10100];
int lines [10100][3];



int vis[105][105]={0};
int c=0;
void dfs(int x,int y)
{
    if(vis[y][x]==0 && grid[y][x]==0)
    {
        vis[y][x]=1;
        points[c].first=y;
        points[c].second=x;
        c++;
        dfs(x+1,y);
        dfs(x-1,y);
        dfs(x,y+1);
        dfs(x,y-1); 
    }
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    memset(grid,-1,sizeof(grid));
    int n,m;
    cout<<"Enter grid size";
    cin>>n>>m;//size of grid
    //setting lines at boundry
    for(int i=0;i<=n+1;i++)
        grid[i][0]=1,grid[i][m+1]=1;
    
    for(int j=0;j<=m+1;j++)
        grid[0][j]=1,grid[n+1][j]=1;
    cout<<"Enter Grid";
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            cin>>grid[i][j];// 0 for non lines points// 1 for lines points
    
    int x;
    int y;
    cout<<"Enter point\n";
    cin>>x>>y;//point to be colored
    dfs(x,y);
    sort(points,points + c);
    int l=0;
    int empty=0;
    int left,right,height;
    for(int i=0;i<c;i++)
    {
        if(empty==0)
        {
            empty=1;
            height=points[i].first;
            left=points[i].second;
            right=points[i].second;
        }
        else if(height != points[i].first || right+1 != points[i].second)//lines has been broken
        {
            lines[l][0]=height;
            lines[l][1]=left;
            lines[l][2]=right;
            l++;
            height=points[i].first;
            left=points[i].second;
            right=points[i].second;
            
        }
        else
            right++;
        if(i==c-1)
        {
            lines[l][0]=height;
            lines[l][1]=left;
            lines[l][2]=right;
            l++;
        }
    }
    for(int i=0;i<l;i++)
        cout<<lines[i][0]<<" "<<lines[i][1]<<" "<<lines[i][2]<<"\n";// in the order y-cordinate then left right
}
#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <sstream>

using namespace std;

#define MAX 987654321
int V, adj[201][201];

void floyd(){
    for(int i = 0; i < V; i++ ){
        for(int j = 0; j < V; j++){
            for(int k = 0; k < V; k++){
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j]);
            }
        }
    }
}

void update(int v1, int v2, int cost){
    for(int i = 0; i < V; i++ ){
        for(int j = 0; j < V; j++){
                adj[i][j] = min(adj[i][j], \
                    min(adj[i][v1]+adj[v2][j]+cost,adj[i][v2]+adj[v1][j]+cost));
        }
    }
}

int main(){
    cin.sync_with_stdio(false);

    int T = 0;
    int M,N;

    cin >> T;
    while(T--){
        cin >> V >> M >> N;
        V++;
        for(int i = 0; i < V; i++)
            for(int j = 0; j < V; j++)
                adj[i][j] = MAX;
        for(int i = 0; i < V; i++)
            adj[i][i] = 0;

        int v1,v2,cost;
        for(int i= 0; i < M; i++){
            cin >> v1 >> v2 >> cost;
            adj[v1][v2] = cost;
            adj[v2][v1] = cost;
        }

        int count = 0;
        for(int i= 0; i < N; i++){
            cin >> v1 >> v2 >> cost;
            if(adj[v1][v2] <= cost) {
                count += 1;
                continue;
            }
            update(v1,v2,cost);
        }

        cout << count <<endl;
    }
    return 0;
}

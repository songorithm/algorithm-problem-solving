#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <sstream>

using namespace std;

#define MAX 987654321
int V, adj[500][500];
int delay[500];
int W[500][500];

void solve(){
    vector<pair<int,int> > order;
    for(int i = 0; i < V; i++) {
        order.push_back(make_pair(delay[i],i));
    }
    sort(order.begin(), order.end());
    for(int i = 0; i < V; i++)
        W[i][i] = 0;

    for(int k = 0; k < V; k++) {
        int w = order[k].second;
        for(int i = 0; i < V; i++){
            for(int j = 0; j < V; j++){
                adj[i][j] = min(adj[i][j], adj[i][w]+adj[w][j]);
                W[i][j] = min(W[i][j], adj[i][w]+adj[w][j]+delay[w]);
            }
        }
    }
}

int main(){
    cin.sync_with_stdio(false);
    int E = 0;
    string s;

    cin >> V >> E;
    cin.get();
    getline(cin, s);
    stringstream ss(s);

    int n = 0;
    for(int i = 0; i < V; i++){
        ss >> n;
        delay[i] = n;
    }
    for(int i = 0; i < V; i++) {
        for(int j = 0; j < V; j++) {
            adj[i][j] = MAX;
            W[i][j] = MAX;
        }
    }

    int v1, v2, cost;
    while(E--){
        cin >> v1 >> v2 >> cost;
        v1--;v2--;
        adj[v1][v2] = cost;
        adj[v2][v1] = cost;
        W[v1][v2] = cost;
        W[v2][v1] = cost;
    }

    solve();

    int tests;
    cin >> tests;
    while(tests--) {
        cin >> v1 >> v2;
        v1--;v2--;
        cout<<W[v1][v2]<<endl;
    }

    return 0;
}

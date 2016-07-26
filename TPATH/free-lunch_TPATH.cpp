#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <sstream>
#include <cstring>

using namespace std;

#define MAX 987654321
int V, E;


bool dfs(int start, vector<vector<pair<int, int> > > adj, \
    int lo, int hi, vector<bool> visited){

    if(start == V-1)
        return true;

    visited[start] = true;
    for(int i = 0; i < adj[start].size(); i++){
        int v2 = adj[start][i].first;
        int cost = adj[start][i].second;
        if(!visited[v2] && lo <= cost && cost <= hi){
            if(dfs(v2, adj, lo, hi, visited)) {
                return true;
            }
        }
    }
    return false;
}

int solve(vector<vector<pair<int, int> > >adj, vector<int> order){
    int lo = 0;
    int hi = 0;
    int ret = MAX;

    while(true){
        vector<bool> visited(V, false);
        if(dfs(0, adj, order[lo], order[hi], visited)){
            ret = min(ret, order[hi]-order[lo]);
            lo++;
        }
        else{
            if(hi == order.size()-1){
                break;
            }
            hi++;
        }
    }
    return ret;
}

// Kruskal
struct DisjointSet {
    vector<int> parent, rank;

    DisjointSet(int n) : parent(n), rank(n, 1) {
        for(int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int u) {
        if(u == parent[u])
            return u;
        return parent[u] = find(parent[u]);
    }

    void merge(int u, int v) {
        u = find(u); v = find(v);
        if(u == v)
            return;

        if(rank[u] > rank[v])
            swap(u, v);

        if(rank[u] == rank[v])
            rank[v]++;

        parent[u] = v;
    }
};


vector<pair<int, pair<int,int> > > order;

int minUpperBound(int lo){
    DisjointSet sets(V);
    for(int i = 0; i < E; i++) {
        if(order[i].first < lo)
            continue;

        sets.merge(order[i].second.first, order[i].second.second);
        if(sets.find(0) == sets.find(V-1))
            return order[i].first;
    }

    return MAX;
}

int solve2(vector<vector<pair<int, int> > >adj) {
    int ret = MAX;
    for(int i = 0; i < E; i++){
        ret = min(ret, minUpperBound(order[i].first)-order[i].first);
    }
    return ret;
}

int main(){
    cin.sync_with_stdio(false);

    int T = 0;
    cin >> T;

    while(T--){
        cin >> V >> E;
        int v1,v2,cost;
        vector<vector<pair<int, int> > > adj(V);
        order.resize(E);
        for(int i= 0; i < E; i++){
            cin >> v1 >> v2 >> cost;
            adj[v1].push_back(make_pair(v2, cost));
            adj[v2].push_back(make_pair(v1, cost));
            // order.push_back(cost);
            order[i] = make_pair(cost, make_pair(v1, v2));
        }
        // order.erase( unique(order.begin(), order.end()), order.end() );
        sort(order.begin(), order.end());

        cout << solve2(adj) <<endl;
    }
    return 0;
}

#include <iostream>
#include <set>
#include <bits/stdc++.h>
#include <random>

using namespace std;

double random_uniform(double a, double b) {
    if (a > b) {
        std::swap(a, b); // Swap if a > b
    }

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(a, b);
    
    return dis(gen);
}

double find_prob(pair<int,int> p1, pair<int,int> p2)
{
    double dist = sqrt(pow(p1.first-p2.first,2) + pow(p1.second-p2.second,2));
    double prob = exp(-dist/20000);
    return prob;
}

const pair<double,double> depot_loc = {0,0};
const int num_customers = 400;
const int num_clusters = 20;
set<pair<int,int>> cluster_points;
priority_queue<pair<double,pair<int,int>>> pq;

int main()
{
    // defining the cluster points
    for(int i=0; i<num_clusters; i++)
    {
        int x = random_uniform(-500,500);
        int y = random_uniform(-500,500);
        while(cluster_points.find({x,y}) != cluster_points.end())
        {
            x = random_uniform(-500,500);
            y = random_uniform(-500,500);
        }
        cluster_points.insert({x,y});
    }

    // check through all integral points in the space
    for(int i=-500; i<=500; i++)
    {
        for(int j=-500; j<=500; j++)
        {
            if(cluster_points.find({i,j}) != cluster_points.end())
                continue;
            double point_prob = 0;
            for(auto cluster_point : cluster_points)
            {
                point_prob += find_prob({i,j},cluster_point);
            }
            pq.push({point_prob,{i,j}});
        }
    }
    // cout << "NAME : inp1.vrp" << endl;
    // cout << "COMMENT : input file for vrp" << endl;
    // cout << "TYPE : CVRP" << endl;
    // cout << "DIMENSION : " << num_customers << endl;
    // cout << "EDGE_WEIGHT_TYPE : EUC_2D" << endl;
    // cout << "CAPACITY : " << 40 << endl;
    // cout << "NODE_COORD_SECTION" << endl;
    int count=0;
    for(auto cluster_point : cluster_points)
    {
        cout << cluster_point.first << "," << cluster_point.second << endl;
        count++;
    }
    for(int i=0; i<num_customers-num_clusters; i++)
    {
        auto point = pq.top();
        pq.pop();
        cout << point.second.first << "," << point.second.second << endl;
        count++;
    }
    // cout << "DEMAND_SECTION" << endl;
    // for(int i=0; i<num_customers; i++)
    // {
    //     int rand_demand = random_uniform(1,100);
    //     cout << i+1 << " " << rand_demand << endl;
    // }
    // cout << "DEPOT_SECTION" << endl;
    // cout << 0 << endl;
    // cout << 0 << endl;
    // cout << "EOF" << endl;
    return 0;
}
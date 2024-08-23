#include <bits/stdc++.h>
#define endl "\n"

class Solution
{
public:
    std::vector<int> findOrder(int numCourses, std::vector<std::vector<int>> &prerequisites)
    {
        if (numCourses == 1)
        {
            return std::vector<int>(1, 0);
        }

        std::vector<int> ans;
        std::vector<std::vector<int>> graph(numCourses, std::vector<int>(0));
        std::vector<int> visited(numCourses, 0);
        std::stack<int> stack;
        bool cycle_detected = false;
        for (auto &v : prerequisites)
        {
            // graph[v[0]].push_back(v[1]);
            graph[v[1]].push_back(v[0]);
        }
        for (size_t i = 0; i < numCourses; i++)
        {
            if (visited[i])
                continue;
            dfs(graph, visited, stack, i, cycle_detected);
        }
        if (cycle_detected)
            return std::vector<int>(0);

        while (!stack.empty())
        {
            ans.push_back(stack.top());
            stack.pop();
        }

        return ans;
    }

    void printGraph(std::vector<std::vector<int>> &graph)
    {
        for (size_t i = 0; i < graph.size(); i++)
        {
            for (size_t j = 0; j < graph[i].size(); j++)
            {
                std::cout << graph[i][j] << " ";
            }
            std::cout << endl;
        }
    }

    void dfs(std::vector<std::vector<int>> &graph, std::vector<int> &visited, std::stack<int> &stack, int node, bool &cycle_detected)
    {
        // std::cout << "node" << node << endl;
        visited[node] = 1;

        for (size_t i = 0; i < graph[node].size(); i++)
        {
            if (cycle_detected)
            {
                return;
            }

            if (visited[graph[node][i]] == 1)
            {
                cycle_detected = true;
                return;
            }
            else if (visited[graph[node][i]] == 2)
            {
                continue;
            }

            dfs(graph, visited, stack, graph[node][i], cycle_detected);
        }

        visited[node] = 2;
        stack.push(node);
    }
};

void one_lenth_test()
{
    std::cout << "---------------- one lengt tests---------------";
    std::vector<std::vector<int>> prerequisites;
    Solution sol;
    auto ans = sol.findOrder(1, prerequisites);
    std::vector<int> actual1{0};

    assert((std::equal(ans.begin(), ans.end(), actual1.begin())));

    std::cout
        << endl;
}

void two_lenth_test()
{
    std::cout << "---------------- two length tests---------------" << endl;

    std::vector<std::vector<int>> prerequisites;
    std::vector<int> prerequisite1{0, 1};

    prerequisites.push_back(prerequisite1);

    Solution sol;
    auto ans = sol.findOrder(2, prerequisites);
    for (const auto &i : ans)
    {
        std::cout << i << " ";
    }

    std::cout << endl;

    prerequisites.clear();
    prerequisite1 = std::vector<int>{1, 0};
    prerequisites.push_back(prerequisite1);
    ans = sol.findOrder(2, prerequisites);
    for (const auto &i : ans)
    {
        std::cout << i << " ";
    }
    std::cout << endl;
}

void three_lenth_test()
{
    std::cout << "---------------- three length tests---------------" << endl;
    Solution sol;

    std::vector<std::vector<int>> prerequisites;
    std::vector<int> prerequisite1{0, 1};
    std::vector<int> prerequisite2{0, 2};
    std::vector<int> prerequisite3{2, 1};

    prerequisites.push_back(prerequisite1);
    prerequisites.push_back(prerequisite2);
    prerequisites.push_back(prerequisite3);

    auto ans = sol.findOrder(3, prerequisites);
    for (const auto &i : ans)
    {
        std::cout << i << " ";
    }

    // std::cout << endl;

    // prerequisites.clear();

    // prerequisites.push_back(std::vector<int>{1, 0});
    // prerequisites.push_back(std::vector<int>{2, 0});

    // ans = sol.findOrder(3, prerequisites);
    // for (const auto &i : ans)
    // {
    //     std::cout << i << " ";
    // }

    // std::cout << endl;

    // prerequisites.clear();

    // prerequisites.push_back(std::vector<int>{1, 0});
    // prerequisites.push_back(std::vector<int>{2, 0});
    // prerequisites.push_back(std::vector<int>{1, 2});
    // ans = sol.findOrder(3, prerequisites);

    // for (const auto &i : ans)
    // {
    //     std::cout << i << " ";
    // }

    // std::cout << endl;

    // prerequisites.clear();

    // prerequisites.push_back(std::vector<int>{1, 0});
    // prerequisites.push_back(std::vector<int>{0, 2});
    // prerequisites.push_back(std::vector<int>{2, 1});
    // ans = sol.findOrder(3, prerequisites);

    // for (const auto &i : ans)
    // {
    //     std::cout << i << " ";
    // }
    // std::cout << endl;
}

int main()
{
    three_lenth_test();

    return 0;
}

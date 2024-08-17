#include <bits/stdc++.h>
#define endl "\n"

class Solution
{
public:
    void rotate(std::vector<std::vector<int>> &matrix)
    {
        int n = matrix.size();
        // printMatrix(matrix);
        // std::cout << "------------------------------------------" << endl;
        for (size_t i = 0; i <= (n >> 1); i++)
        {
            for (size_t j = i; j < n - i - 1; j++)
            {
                int top_left = matrix[i][j];
                int top_right = matrix[j][n - i - 1];
                int bottom_right = matrix[n - i - 1][n - j - 1];
                int bottom_left = matrix[n - j - 1][i];

                matrix[j][n - i - 1] = top_left;
                matrix[n - i - 1][n - j - 1] = top_right;
                matrix[n - j - 1][i] = bottom_right;
                matrix[i][j] = bottom_left;

                // std::cout
                // << top_left << " " << top_right << " " << bottom_right << " " << bottom_left << endl;
            }
        }
        // std::cout << "------------------------------------------" << endl;
        // printMatrix(matrix);
    }

    void printMatrix(std::vector<std::vector<int>> &matrix)
    {
        for (size_t i = 0; i < matrix.size(); i++)
        {
            for (size_t j = 0; j < matrix[i].size(); j++)
            {
                std::cout << matrix[i][j] << " ";
            }
            std::cout << endl;
        }
    }
};

int main()
{
    std::vector<std::vector<int>> mat;
    int size = 6;
    for (size_t i = 0; i < size; i++)
    {
        std::vector<int> row;
        mat.push_back(row);
        for (size_t j = 0; j < size; j++)
        {
            mat[i].push_back(j + 1 + (i * size));
        }
    }

    Solution sol;
    sol.rotate(mat);

    return 0;
}

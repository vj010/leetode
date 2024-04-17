#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

class Solution
{
public:
    int maximalSquare(vector<vector<char>> &matrix)
    {
        // cout << "here" << endl;
        // cout << "size:" << matrix.size() << endl;
        if (matrix.size() == 0 || matrix[0].size() == 0)
        {
            // cout << "returning" << endl;
            return 0;
        }

        int row = matrix.size();
        int col = matrix[0].size();
        int dim = min(row, col);

        bool ***dp = new bool **[301];
        for (size_t i = 0; i < 301; i++)
        {
            dp[i] = new bool *[row];
        }

        for (size_t i = 0; i < 301; i++)
        {
            for (size_t j = 0; j < col; j++)
            {
                dp[i][j] = new bool[col];
                // dp[i][j] = {0};
            }
        }
        fill(&dp[0][0][0], &dp[0][0][0] + sizeof(dp) / sizeof(bool), false);
        size_t area = 0;
        for (size_t i = 0; i < row; i++)
        {
            for (size_t j = 0; j < col; j++)
            {
                if (matrix[i][j] == '1')
                {
                    dp[1][i][j] = true;
                    area = 1;
                }
            }
        }
        // printMatrix(matrix);

        for (size_t i = 2; i < dim + 1; i++)
        {
            // cout << "calculating" << endl;
            bool found = false;
            for (size_t j = 0; j < row; j++)
            {
                for (size_t k = 0; k < col; k++)
                {
                    int square = ceil((float)i / 2);
                    if ((j + (i / 2)) >= row || (k + (i / 2)) >= col)
                    {
                        continue;
                    }
                    dp[i][j][k] = dp[square][j][k] && dp[square][j + (i / 2)][k] && dp[square][j][k + (i / 2)] && dp[square][j + (i / 2)][k + (i / 2)];
                    if (dp[i][j][k])
                    {
                        area = max(area, i * i);
                        found = true;
                    }
                    // cout << "i:" << i << ", j:" << j << ", k:" << k << ", dp:" << dp[i][j][k] << endl;
                }
            }
            if (!found)
            {
                break;
            }
        }
        return area;
    }

    void printMatrix(vector<vector<char>> &matrix)
    {
        for (size_t i = 0; i < matrix.size(); i++)
        {
            for (size_t j = 0; j < matrix[0].size(); j++)
            {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
    }
};

int main()
{
    vector<vector<char>> matrix;
    // cout << "here1" << endl;
    vector<char> row1{'1', '0', '1', '0', '0'};
    // cout << "here2" << endl;
    vector<char> row2{'1', '0', '1', '1', '1'};
    // cout << "here3" << endl;
    vector<char> row3{'1', '1', '1', '1', '1'};
    // cout << "here4" << endl;
    vector<char> row4{'1', '0', '0', '1', '0'};
    // cout << "here5" << endl;
    matrix.push_back(row1);
    matrix.push_back(row2);
    matrix.push_back(row3);
    matrix.push_back(row4);
    Solution sol;
    cout << sol.maximalSquare(matrix);
    return 0;
}

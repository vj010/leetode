#include <bits/stdc++.h>
#define endl "\n"

class Solution
{
public:
    void nextPermutation(std::vector<int> &nums)
    {
        if (nums.size() <= 1)
        {
            // printPermutaion(nums);
            return;
        }

        int left_index = -1;

        for (int i = nums.size() - 2; i >= 0; i--)
        {
            if (nums[i] < nums[i + 1])
            {
                left_index = i;

                int right = nums.size() - 1;
                // std::cout << "value:" << *(nums.begin() + left_index) << " left_index:" << left_index << endl;
                std::vector<int>::iterator min_elem = std ::min_element(nums.begin() + left_index + 1, nums.end(), [&](const int &a, const int &b)
                                                                        { return a < b && a > nums[left_index]; });
                std::iter_swap(nums.begin() + i, min_elem);
                std::sort(nums.begin() + left_index + 1, nums.end());

                break;
            }
        }

        if (left_index == -1)
        {
            std::sort(nums.begin(), nums.end());
        }

        printPermutaion(nums);
    }

    void printPermutaion(std::vector<int> &nums)
    {
        for (auto a : nums)
        {
            std::cout << a << ",";
        }
        std::cout << endl;
    }
};

int main()
{
    std::vector<int> v1{1, 1, 5};
    std::vector<int> v2{3, 2, 1};
    std::vector<int> v3{1, 2, 3};
    std::vector<int> v4{1, 2, 3, 4, 5};
    std::vector<int> v5{1, 2, 3, 5, 4};
    std::vector<int> v6{1};
    std::vector<int> v7{1, 5, 3, 2, 4};
    std::vector<int> v8{2, 3, 1};
    std::vector<int> v9{3, 2, 1, 4};
    std::vector<int> v10{3, 2, 4, 1};
    std::vector<int> v11{3, 4, 1, 2};
    std::vector<int> v12{3, 4, 2, 1};
    std::vector<int> v13{2, 1};
    std::vector<int> v14{1, 2};
    std::vector<int> v15{4, 5, 6, 3, 2, 1};

    Solution sol;
    // sol.nextPermutation(v1);
    // sol.nextPermutation(v2);
    // sol.nextPermutation(v3);
    // sol.nextPermutation(v4);
    // sol.nextPermutation(v5);
    // sol.nextPermutation(v6);
    // sol.nextPermutation(v7);
    sol.nextPermutation(v8);
    sol.nextPermutation(v9);
    sol.nextPermutation(v10);
    sol.nextPermutation(v11);
    sol.nextPermutation(v12);
    sol.nextPermutation(v13);
    sol.nextPermutation(v14);
    sol.nextPermutation(v15);

    return 0;
}

#include <bits/stdc++.h>
#define endl "\n"

class Solution
{
public:
    int findMin(std::vector<int> &nums)
    {
        int n = nums.size();
        if (nums[0] < nums[n - 1] or nums.size() == 1)
        {
            return nums[0];
        }
        int start = 0;
        int end = n - 1;
        int mid = 0;
        while (start < end)
        {
            mid = (start + end) >> 1;
            if (found(nums, mid))
            {
                break;
            }
            if (nums[start] < nums[mid])
            {
                start = mid + 1;
            }
            else
            {
                end = mid;
            }
        }
        return nums[mid + 1];
    }

    bool found(std::vector<int> &nums, int mid)
    {
        if (mid + 1 >= nums.size() or nums[mid] < nums[mid + 1])
            return false;

        return true;
    }
};

int main()
{
    std::vector<int> nums{3, 4, 5, 1, 2};
    std::vector<int> nums2{4, 5, 6, 7, 0, 1, 2};
    std::vector<int> nums3{11, 13, 15, 17};
    std::vector<int> nums4{1};
    std::vector<int> nums5{11, 13};
    std::vector<int> nums6{13, 11};
    std::vector<int> nums7{13, 11, 12};
    std::vector<int> nums8{11, 12, 13};
    std::vector<int> nums9{5, 1, 3, 4};
    std::vector<int> nums10{4, 5, 1, 3};
    std::vector<int> nums11{3, 4, 5, 1};
    std::vector<int> nums12{2, 3, 4, 5, 1};
    std::vector<int> nums13{4, 5, 1, 2, 3};
    std::vector<int> nums14{5, 1, 2, 3, 4};

    Solution sol;

    // std::cout << sol.findMin(nums) << endl;
    // std::cout << sol.findMin(nums2) << endl;
    // std::cout << sol.findMin(nums3) << endl;
    // std::cout << sol.findMin(nums4) << endl;
    // std::cout << sol.findMin(nums5) << endl;
    // std::cout << sol.findMin(nums6) << endl;
    // std::cout << sol.findMin(nums7) << endl;
    // std::cout << sol.findMin(nums8) << endl;
    // std::cout << sol.findMin(nums9) << endl;
    // std::cout << sol.findMin(nums10) << endl;
    std::cout << sol.findMin(nums11) << endl;
    std::cout << sol.findMin(nums12) << endl;
    std::cout << sol.findMin(nums13) << endl;
    std::cout << sol.findMin(nums14) << endl;
}

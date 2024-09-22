#include <iostream>
#include <vector>

class Solution {
public:
    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
        const unsigned long lenght1 = nums1.size();
        const unsigned long lenght2 = nums2.size();
        const unsigned long pivot = (lenght1 + lenght2) / 2 + 1;
        int left_index = 0;
        int right_index = 0;
        int median = 0;
        int one_before = 0;
        for (int i =0; i < pivot; i++)
        {
            one_before = median;
            if (left_index == lenght1 || nums1[left_index] > nums2[right_index])
            {
                median = nums2[right_index];
                right_index ++;
            } else if (right_index == lenght2 || nums1[left_index] <= nums2[right_index])
            {
                median = nums1[left_index];
                left_index++;
            }
        }
        if ((lenght1 + lenght2) % 2 == 1) {
            return median;
        }
        return static_cast<double>(median + one_before) / 2;
    }
};

int main(){
    int list1[] = {0,0,0,0,0};
    std::vector<int> nums1 (list1, list1 + sizeof(list1) / sizeof(int) );
    int list2[] = {-1,0,0,0,0,0,1};
    std::vector<int> nums2 (list2, list2 + sizeof(list2) / sizeof(int) );
    Solution sol = Solution();
    std::cout<<"reuslt: "<<sol.findMedianSortedArrays(nums1, nums2);
    return 0;
};

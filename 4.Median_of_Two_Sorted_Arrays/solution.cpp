#include <iostream>
#include <vector>

class Solution {
public:
    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
        int lenght1 = nums1.size();
        int lenght2 = nums2.size();
        int pivot = (lenght1 + lenght2) / 2 + 1;
        int left_index = 0;
        int right_index = 0;
        int median = 0;
        int one_before = 0;
        for (int i =0; i < pivot; i++)
        {
            one_before = median;
            if (left_index == lenght1)
            {
                median = nums2[right_index];
                right_index ++;
            } else if (right_index == lenght2)
            {
                median = nums1[left_index];
                left_index ++;
            }
            else if (nums1[left_index] <= nums2[right_index])
            {
                median = nums1[left_index];
                left_index++;
            }
            else if (nums1[left_index] > nums2[right_index])
            {
                median = nums2[right_index];
                right_index++;
            }
        }
        if ((lenght1 + lenght2) % 2 == 1) {
            return median;
        }
        return static_cast<double>(median + one_before) / 2;
    }
};

int main(){
    int myints[] = {0,0,0,0,0};
    std::vector<int> fifth (myints, myints + sizeof(myints) / sizeof(int) );
    int myints1[] = {-1,0,0,0,0,0,1};
    std::vector<int> fifthf (myints1, myints1 + sizeof(myints1) / sizeof(int) );
    Solution sol = Solution();
    std::cout<<"reuslt: "<<sol.findMedianSortedArrays(fifth, fifthf);
    return 0;
};
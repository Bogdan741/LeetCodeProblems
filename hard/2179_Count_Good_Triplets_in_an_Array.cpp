// You are given two 0-indexed arrays nums1 and nums2 of length n, both of
// which are permutations of [0, 1, ..., n - 1].
//
// A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.
//
// Return the total number of good triplets.

// TAG: Binary index tree, Segment tree, Merge sort

#include <vector>
#include <algorithm>
#include <unordered_map>
#include <iostream>
using namespace std;
// -----------------------------------------------------
// Too slow O(n^2)
class Solution {
public:
    long long goodTriplets(const vector<int>& nums1, const vector<int>& nums2) {
        int n = nums1.size();
        unordered_map<int,int> indexes1;
        unordered_map<int,int> indexes2;
        // O(n)
        for(int i{}; i < n; i++){
            indexes1[nums1[i]] = i;
            indexes2[nums2[i]] = i;
        }
        long long count{0};
        // O(n^2)
        for(int val{}; val < n; ++val){
            int val_nums1_idx = indexes1[val];
            int val_nums2_idx = indexes2[val];
            long long count_greater{};
            long long count_lesser{};
            for(int i={0}; i < n; ++i){
                if (indexes1[i] > val_nums1_idx && indexes2[i] > val_nums2_idx){
                    ++count_greater;
                }
                if (indexes1[i] < val_nums1_idx && indexes2[i] < val_nums2_idx){
                    ++count_lesser;
                }
            }
            count += count_lesser*count_greater;
        }
        return count;
    }
};
// -----------------------------------------------------
// Solution with two bit: O(n logn)
class FenwickTree{
private:
    vector<int> bit;
    int _n;
public:
    explicit FenwickTree(int range): _n{range+1}{
        bit.resize(_n,0);
    }
    void update(int id, int val){
        while(id<_n){
            bit[id]+=val;
            id+=id & -id;
        }
    }
    long long query(int id){
        int res = 0;
        while(id > 0){
            res+=bit[id];
            id-=id & -id;
        }
        return res;
    }
};

class Solution1 {
public:
    long long goodTriplets(const vector<int>& nums1, const vector<int>& nums2) {
        int n = nums1.size();
        unordered_map<int,int> dict2;
        vector<int> indices;
        for(int i{}; i<n;++i){
            dict2[nums2[i]] = i;
        }
        for(int i{}; i<n; ++i){
            indices.push_back(dict2[nums1[i]]);
        }

        FenwickTree bit1(n);
        FenwickTree bit2(n);
        long long ans{};
        for(int i{}; i < n; ++i){
            int elem = indices[i];
            ans+=bit2.query(elem); // get number of elements less then elem 
            bit1.update(elem+1,1); // add new element
            int less = bit1.query(elem); // count number of elements less then elem
            bit2.update(elem+1, less); // set count of elements less than elem 
        }
        return ans;
    }
};
// -----------------------------------------------------


int main(){
    int i = Solution1().goodTriplets({4,0,1,3,2}, {4,1,0,2,3});
    cout << i;
}

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> setNums(nums.begin(),nums.end());
        if(nums.size() == setNums.size()){
            return false;
        } else{
            return true;
        }
    }
};
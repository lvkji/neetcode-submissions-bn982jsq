class Solution {
public:
    int trap(vector<int>& height) {
        //Greedy Two Pointer Algorithm
        int left = 0;
        int right = height.size()-1;
        int leftMax = height[left];
        int rightMax = height[right];
        int totalWater = 0;
        while(left < right){
            if(leftMax < rightMax){
                left+=1;
                //Pick local optimum on left (greedy)
                leftMax = std::max(leftMax,height[left]);
                totalWater += leftMax - height[left];
            } else if(leftMax >= rightMax){
                right-=1;
                //Pick local optimum on the right (greedy)
                rightMax = std::max(rightMax,height[right]);
                totalWater += rightMax - height[right];
            }
        }
        return totalWater;
    }
};

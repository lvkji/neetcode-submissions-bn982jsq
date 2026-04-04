class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int> countS;
        for(char ch : s){
            countS[ch]+=1;
        }
        std::unordered_map<char,int> countT;
        for(char ch : t){
            countT[ch]+=1;
        }
        if(countT == countS){
            return true;
        } else {
            return false;
        }
    }
};

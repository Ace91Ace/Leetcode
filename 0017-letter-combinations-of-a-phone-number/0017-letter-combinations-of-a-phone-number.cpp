class Solution {  
private:  
    void solve(int i, string map[], string out, string digits, vector<string> &ans) {  
        if (i >= digits.length()) {  
            ans.push_back(out);  
            return;  
        }  

        int num = digits[i] - '0';  
        string val = map[num];  

        for (int j = 0; j < val.size(); j++) {   
            out.push_back(val[j]);  
            solve(i + 1, map, out, digits, ans);
            out.pop_back(); 
        }  
    }  
public:  
    vector<string> letterCombinations(string digits) {  
        vector<string> ans;  
        string out = "";  
        
        if (digits.length() == 0) {  
            return ans;  
        }  

        string map[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};  
        solve(0, map, out, digits, ans); 
        return ans;  
    }  
};
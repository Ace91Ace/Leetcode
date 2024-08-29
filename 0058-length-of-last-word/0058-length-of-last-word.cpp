class Solution {
public:
    vector<string> split(string s)
    {
        vector<string> result;
        istringstream iss(s);
        string word;
        while( iss >> word)
        {
            result.push_back(word);
        }
        return result;
    }
    int lengthOfLastWord(string s) {
        
        vector<string> ans=split(s);
        int size=ans.size();
        string last=ans[size-1];
        return last.length();
        
    }
};
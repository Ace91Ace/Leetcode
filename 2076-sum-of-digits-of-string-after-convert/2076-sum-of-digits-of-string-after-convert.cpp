class Solution {
public:
    int getLucky(string s, int k) {
        string ascii;

        for (int i = 0; i < s.size(); i++){
            ascii.append(to_string(static_cast<int>(s[i] - 'a' + 1)));
        }
        
        for (int i = 0; i < k ; i++){
            int sum = 0;
            for (int j = 0; j < ascii.size(); j++){
                sum += ascii[j] - '0'; 
            }
            ascii = to_string(sum);
        }
        
        return stoi(ascii); 
    }
};
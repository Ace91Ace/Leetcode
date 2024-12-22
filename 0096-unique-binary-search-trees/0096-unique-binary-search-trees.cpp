class Solution {
public:
    int catalan(int n){
        if (n <= 1){
            return 1;
        }
        return 1.0*2*(2*n-1)/(n+1) * catalan(n-1);
    }
    int numTrees(int n) {
        return catalan(n);
    }
};
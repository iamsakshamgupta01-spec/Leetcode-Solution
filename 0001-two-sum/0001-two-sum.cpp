class Solution {
public:
    vector<int> twoSum(vector<int>& arr, int x) {
        vector<int> v(2);
        int n=arr.size();
        for(int i=0;i<n;i++){
            bool flag=true;
            for(int j=i+1;j<n;j++){
                if(arr[i]+arr[j]==x){
                    v[0]=i;
                    v[1]=j;
                    flag=false;
                    break;

                }
            }
            if(flag=false) break;
        }
        return v;


    }
};
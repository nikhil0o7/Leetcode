/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if(strs.length == 0) {
        return "";
    } 
    strs.sort();
    let s1 = strs[0];
    let s2 = strs[strs.length - 1];
    let i = 0;
    while(i< s1.length && i < s2.length && s1[i] == s2[i]){
        i = i+1
    }
    
    return s1.substring(0,i);
    
};
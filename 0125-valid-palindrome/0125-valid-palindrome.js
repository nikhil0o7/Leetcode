/**
 * @param {string} s
 * @return {boolean}
 */

function isAlnum(str) {
    return /^[a-z0-9]+$/i.test(str);
}

var isPalindrome = function(s) {
    let  l= 0;
    let r =s.length -1;
    
    while(l<r){
        while(l<r && !isAlnum(s[l])){
            l = l+1;
        }
        while(l<r && !isAlnum(s[r])){
            r = r-1;
        }
        while(l<r && s[l].toLowerCase() != s[r].toLowerCase()){
            return false;
        }
        l++;
        r--;
    }
    return true;
    
};
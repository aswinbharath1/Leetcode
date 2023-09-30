/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function(s) {
    let curr = 1;
    let maxp = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1]) {
            curr++;
        } else {
            curr = 1;
        }
        maxp = Math.max(maxp, curr);
    }

    return maxp;
};

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    let num = nums1.concat(nums2).sort((a, b) => a - b);
    let mid = 0;
    let n = num.length
    if (n % 2 == 0) {
        return (num[n/2 - 1] + num[n/2])/ 2;
    } else {
        return num[Math.floor(n/2)];
    }
}
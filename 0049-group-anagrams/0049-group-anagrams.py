from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_maps = defaultdict(list)
        result= []
        
        for word in strs:
            sortedWord = tuple(sorted(word))
            anagram_maps[sortedWord].append(word)
        
        for value in anagram_maps.values():
            result += [value]
            
        return result
    
def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    solObj = Solution()
    print(solObj.groupAnagrams(strs))
main()
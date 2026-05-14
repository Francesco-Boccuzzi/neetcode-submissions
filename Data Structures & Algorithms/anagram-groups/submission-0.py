class Solution:           
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize hash map
        result = defaultdict(list)
        # Iterate over the words in input array
        for word in strs:
            # For each word, create array of len = 26 keeping track of frequency
            count = [0] * 26
            # Iterate over each letter in the string
            for char in word:
                # Populate the count array
                count[ord(char)-ord("a")] += 1
            # Add key-value pair to dict
            result[tuple(count)].append(word)

        # Return set of values from the dictionary in list of lists format
        return list(result.values())
        
            
        


        
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        '''BFS'''
        if wordList == []:
            return 0

        wordList.append(beginWord)
        connection_dict = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '_' + word[i+1:]
                if pattern not in connection_dict:
                    connection_dict[pattern] = {word}
                else:
                    connection_dict[pattern].add(word)
        
        for key, val in list(connection_dict.items()):
            if len(val) == 1:
                connection_dict.pop(key)

        queue = [(beginWord, 1)]
        visited = set()

        while queue != []:
            word, length = queue.pop(0)

            for word_set in connection_dict.values():
                if word in word_set:
                    for i in word_set:
                        if i != word and i not in visited:
                            if i == endWord:
                                return length + 1
                            visited.add(i)
                            queue.append((i,length+1))

        return 0

s = Solution()
print(s.ladderLength('hit', 'cog', ['hit','hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(s.ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))

print(s.ladderLength('hot', 'dog', ["hot","cog","dog","tot","hog","hop","pot","dot"]))

print(s.ladderLength("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
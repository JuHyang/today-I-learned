class Solution {
    val countArray = listOf(1, 6, 31, 156, 781)
    val alphaArray = listOf("A","E","I","O","U")
    fun solution(word: String): Int {
        var answer = 0
        
        for (i in 0 until word.length) {
            val char = word[i].toString()
            for (j in 0 until alphaArray.indexOf(char)) {
                answer += countArray[4-i]    
            }
            answer += 1
        }
    
        return answer
    }
}
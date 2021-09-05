class Solution {
    fun solution(table: Array<String>, languages: Array<String>, preference: IntArray): String {
        var answer: String = ""
        
        val tableMap : MutableMap<String, List<String>> = mutableMapOf()
        
        for (input in table) {
            val splitInput = input.split(" ")
            val job = splitInput[0]
            val languageList : ArrayList<String> = ArrayList()
            for (i in 1 until splitInput.size) {
                languageList.add(splitInput[i])
            }
            
            tableMap[job] = languageList.toList()
        }
        
        val preferList : ArrayList<Pair<String,Int>> = ArrayList()
        for (i in 0 until languages.size) {
            preferList.add(Pair(languages[i], preference[i]))
        }
        
        var maxJob = ""
        var maxScore = 0
        for (temp in tableMap.toList()) {
            var tempScore = 0
            println(temp.second)
            for (prefer in preferList) {
                val findIndex = temp.second.indexOf(prefer.first)
                if (findIndex == -1) {
                    continue
                }
                
                val score = 5 - findIndex
                tempScore += score * prefer.second
            }
            
            if (tempScore > maxScore) {
                maxJob = temp.first
                maxScore = tempScore
            } else if (tempScore == maxScore) {
                if (maxJob > temp.first) {
                    continue
                } else {
                    maxJob = temp.first
                }
            } else {
                continue
            }
        }
        
        return maxJob
    }
}
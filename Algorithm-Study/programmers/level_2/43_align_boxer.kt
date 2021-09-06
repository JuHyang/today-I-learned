class Solution {
    fun solution(weights: IntArray, head2head: Array<String>): IntArray {
        val informList : ArrayList<IntArray> = ArrayList()
        for (i in 0 until weights.size) {
            var winCount = 0
            var loseCount = 0
            var weightCount = 0
            for (j in 0 until weights.size) {
                if (head2head[i][j] == 'W') {
                    winCount += 1

                    if (weights[i] < weights[j]) {
                        weightCount += 1
                    }
                } else if (head2head[i][j] == 'L') {
                    loseCount += 1
                } else if (head2head[i][j] == 'N') {
                    continue
                }
            }
            if (winCount == 0 && loseCount == 0) {
                winCount = 0
                loseCount = 1
            }
            informList.add(intArrayOf(winCount, loseCount, -weightCount, -weights[i], i + 1))
        }

        informList.sortWith(compareBy({-(it[0] / (it[0] + it[1]).toFloat())}, {it[2]}, {it[3]}, {it[4]}))

        return informList.map{it[4]}.toIntArray()
    }
}
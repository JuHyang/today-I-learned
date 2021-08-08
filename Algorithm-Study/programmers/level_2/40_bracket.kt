class Solution {
    fun solution(p: String): String {
        if (p.isEmpty()) {
            return ""
        }

        println(p)
        println(p.substring(1, p.length - 1))

        if (isValid(p)) {
            return p
        }

        var result = ""
        
        var leftCount = 0
        var rightCount = 0
        var u = ""
        var v = ""
        for (i in 0 until p.length) {
            val char = p[i]
            
            if (char == '(') {
                leftCount += 1
            } else {
                rightCount += 1
            }

            u += char
            if (leftCount == rightCount) {
                v = p.substring(i)

                break
            }
        }

        if (isValid(u)) {
            result += u + solution(v)
        } else {
            result += "(" + solution(v) + ")" + reverseString(u.substring(1, u.length - 1))
        }

        return result
    }

    fun isValid(brackets : String) : Boolean {
        var stackString = ""
        for (char in brackets) {
            if (char == ')') {
                if (stackString.isEmpty()) {
                    return false
                } else {
                    stackString = stackString.substring(0, stackString.length - 1)
                }
            } else {
                stackString += char
            }
        }

        return true
    }

    fun reverseString(brackets : String) : String {
        var result = ""
        for (char in brackets) {
            if (char == '(') {
                result += ')'
            } else {
                result += '('
            }
        }
        return result
    }
}